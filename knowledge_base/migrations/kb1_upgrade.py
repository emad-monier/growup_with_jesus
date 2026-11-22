#!/usr/bin/env python3
"""KB-1 non-destructive upgrade. Never modifies source DB in place."""
import argparse,hashlib,json,shutil,sqlite3
from datetime import datetime,timezone
from pathlib import Path

DDL = """
CREATE TABLE IF NOT EXISTS kb_schema_migrations (
 version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL, source_sha256 TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS kb_source_versions (
 version_id TEXT PRIMARY KEY,
 source_id TEXT NOT NULL REFERENCES sources(source_id),
 edition_id TEXT REFERENCES editions(edition_id),
 observed_at TEXT NOT NULL, publication_date TEXT,
 version_label TEXT, canonical_url TEXT,
 source_checksum TEXT, rights_status TEXT NOT NULL DEFAULT 'unknown',
 supersedes_version_id TEXT REFERENCES kb_source_versions(version_id),
 notes TEXT
);
CREATE TABLE IF NOT EXISTS kb_claim_revisions (
 revision_id TEXT PRIMARY KEY,
 claim_id TEXT NOT NULL REFERENCES claims(claim_id),
 claim_text TEXT NOT NULL,
 recorded_at TEXT NOT NULL,
 text_sha256 TEXT NOT NULL,
 source_version_id TEXT REFERENCES kb_source_versions(version_id)
);
CREATE TABLE IF NOT EXISTS kb_passage_provenance (
 provenance_id TEXT PRIMARY KEY,
 passage_id TEXT NOT NULL REFERENCES passages(passage_id),
 source_version_id TEXT REFERENCES kb_source_versions(version_id),
 exact_locator TEXT NOT NULL,
 retrieval_date TEXT NOT NULL,
 allowed_excerpt TEXT,
 excerpt_rights TEXT NOT NULL DEFAULT 'unknown',
 curator_note TEXT
);
CREATE TABLE IF NOT EXISTS kb_review_decisions (
 decision_id TEXT PRIMARY KEY,
 claim_revision_id TEXT NOT NULL REFERENCES kb_claim_revisions(revision_id),
 review_domain TEXT NOT NULL CHECK(review_domain IN ('theological','medical','safeguarding','language','rights','editorial','source')),
 reviewer_identifier TEXT,
 reviewer_role TEXT,
 decision TEXT NOT NULL CHECK(decision IN ('pending','approved','changes_requested','rejected')),
 decided_at TEXT, rationale TEXT,
 CHECK(decision <> 'approved' OR (reviewer_identifier IS NOT NULL AND decided_at IS NOT NULL))
);
CREATE TABLE IF NOT EXISTS kb_chapter_requirements (
 requirement_id TEXT PRIMARY KEY, chapter_id TEXT NOT NULL REFERENCES chapters(chapter_id),
 requirement_text TEXT NOT NULL, required_review_domain TEXT,
 critical INTEGER NOT NULL DEFAULT 0 CHECK(critical IN (0,1))
);
CREATE INDEX IF NOT EXISTS idx_kb_revision_claim ON kb_claim_revisions(claim_id);
CREATE INDEX IF NOT EXISTS idx_kb_decision_revision ON kb_review_decisions(claim_revision_id);
CREATE INDEX IF NOT EXISTS idx_kb_provenance_passage ON kb_passage_provenance(passage_id);
"""
CORE=("chapters","works","sources","passages","claims","evidence","chapter_claims","reviews","translations","phase2_source_discovery")

def counts(db):
    return {name:db.execute(f'SELECT count(*) FROM "{name}"').fetchone()[0] for name in CORE}

def upgrade(src,dst):
    src,dst=Path(src).resolve(),Path(dst).resolve()
    if src==dst: raise ValueError("Source and destination must differ")
    if dst.exists(): raise FileExistsError(dst)
    dst.parent.mkdir(parents=True,exist_ok=True)
    source_bytes=src.read_bytes()
    checksum=hashlib.sha256(source_bytes).hexdigest()
    with sqlite3.connect(src.as_posix()) as original:
        expected={"chapters":{"chapter_id","book","title"},"claims":{"claim_id","claim_text","status"},"sources":{"source_id","work_id"},"passages":{"passage_id","source_id","locator"},"evidence":{"evidence_id","claim_id","passage_id"},"reviews":{"review_id","decision"}}
        for table,columns in expected.items():
            actual={row[1] for row in original.execute(f'PRAGMA table_info("{table}")')}
            if not columns.issubset(actual):
                raise ValueError(f"Not the expected project schema: {table} missing {sorted(columns-actual)}")
        before=counts(original)
        if original.execute("PRAGMA integrity_check").fetchone()[0]!="ok": raise RuntimeError("Invalid source DB")
        # SQLite online backup gives a complete transaction-consistent copy.
        with sqlite3.connect(dst.as_posix()) as target:
            original.backup(target)
    try:
        with sqlite3.connect(dst.as_posix()) as db:
            db.execute("PRAGMA foreign_keys=ON")
            with db:
                db.executescript(DDL)
                db.execute("INSERT OR IGNORE INTO kb_schema_migrations VALUES (?,?,?)",(1,datetime.now(timezone.utc).isoformat(),checksum))
            after=counts(db)
            integrity=db.execute("PRAGMA integrity_check").fetchone()[0]
            fk=db.execute("PRAGMA foreign_key_check").fetchall()
            if before!=after or integrity!="ok" or fk: raise RuntimeError("Migration preservation/integrity check failed")
        return {"status":"migrated","source_sha256":checksum,"counts_preserved":before,"integrity":integrity,"foreign_key_errors":len(fk),"output":str(dst)}
    except BaseException:
        dst.unlink(missing_ok=True)
        raise

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--source",required=True);p.add_argument("--output",required=True)
    args=p.parse_args()
    print(json.dumps(upgrade(args.source,args.output),indent=2))
