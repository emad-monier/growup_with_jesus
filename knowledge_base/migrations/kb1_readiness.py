#!/usr/bin/env python3
"""Evidence-readiness metrics: structural only, not clinical/theological approval."""
import argparse,json,sqlite3
from pathlib import Path

def report(path):
  with sqlite3.connect(path) as db:
    db.row_factory=sqlite3.Row
    result={"database":str(path),"integrity":db.execute("PRAGMA integrity_check").fetchone()[0],
            "foreign_key_errors":len(db.execute("PRAGMA foreign_key_check").fetchall()),"chapters":{}}
    for cid in ("B04","G05"):
      q="""SELECT c.claim_id,c.status,COUNT(DISTINCT CASE WHEN e.relation='supports' AND e.review_status='reviewed' AND p.read_status='checked' THEN e.evidence_id END) checked_links
        FROM chapter_claims cc JOIN claims c ON cc.claim_id=c.claim_id
        LEFT JOIN evidence e ON e.claim_id=c.claim_id
        LEFT JOIN passages p ON p.passage_id=e.passage_id
        WHERE cc.chapter_id=? GROUP BY c.claim_id,c.status"""
      rows=db.execute(q,(cid,)).fetchall()
      supported=sum(1 for row in rows if row["checked_links"]>0)
      verified=sum(1 for row in rows if row["status"]=="verified")
      approvals=db.execute("""SELECT COUNT(*) FROM reviews r JOIN chapter_claims cc ON r.object_id=cc.claim_id
        WHERE cc.chapter_id=? AND r.object_type='claim' AND r.decision='approved'""",(cid,)).fetchone()[0]
      result["chapters"][cid]={"mapped_claims":len(rows),"source_checked_claims":supported,"claims_marked_verified":verified,
        "approved_review_entries":approvals,"publication_ready":False,
        "holds":["Expert review not confirmed","Exact passage text and rights require verification",
                 "Learning-objective coverage must be manually audited"]}
    return result

if __name__=="__main__":
  p=argparse.ArgumentParser();p.add_argument("database",type=Path);p.add_argument("--output",type=Path)
  args=p.parse_args();data=report(args.database)
  output=json.dumps(data,indent=2)
  if args.output: args.output.write_text(output+"\n",encoding="utf-8")
  print(output)
