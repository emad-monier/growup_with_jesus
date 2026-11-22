#!/usr/bin/env python3
"""Evidence-first drafting helper. Python standard library only; no AI call."""
import argparse,csv,json,pathlib,re,sqlite3
ROOT=pathlib.Path(__file__).resolve().parent
DB=ROOT/"input"/"knowledge_base_phase3c.sqlite"
OUT=ROOT/"outputs"

def brief(ch):
    with sqlite3.connect(DB) as con:
        con.row_factory=sqlite3.Row
        chapter=con.execute("SELECT * FROM chapters WHERE chapter_id=?",(ch,)).fetchone()
        if chapter is None: raise ValueError("Unknown chapter: "+ch)
        records=con.execute("""SELECT cl.claim_id,cl.claim_text,cl.classification,cl.status AS claim_status,
          e.review_status AS evidence_status,e.relation,p.passage_id,p.section_title,p.locator,
          p.source_url,p.read_status,e.quote_permission_status
          FROM chapter_claims cc JOIN claims cl ON cc.claim_id=cl.claim_id
          LEFT JOIN evidence e ON e.claim_id=cl.claim_id
          LEFT JOIN passages p ON p.passage_id=e.passage_id
          WHERE cc.chapter_id=? ORDER BY cl.claim_id,p.passage_id""",(ch,)).fetchall()
        grouped={}
        for record in records:
            r=dict(record);item=grouped.setdefault(r["claim_id"],{"id":r["claim_id"],"text":r["claim_text"],"classification":r["classification"],"status":r["claim_status"],"evidence":[]})
            if r["passage_id"]:
                item["evidence"].append({k:r[k] for k in ("passage_id","section_title","locator","source_url","read_status","evidence_status","relation","quote_permission_status")})
        grounded=[x for x in grouped.values() if x["status"]!="unverified" and any(e["relation"]=="supports" and e["read_status"]=="checked" and e["evidence_status"]=="reviewed" and e["source_url"] for e in x["evidence"])]
        leads=[x for x in grouped.values() if x not in grounded]
    coverage_file=ROOT/"input"/"COVERAGE_MATRIX_3C.csv"
    with coverage_file.open(encoding="utf-8-sig",newline="") as handle:
        coverage=[row for row in csv.DictReader(handle) if ch in str(row)]
    warnings=["No specialist review has been recorded.","Do not use direct third-party quotations without a rights review."]
    if ch=="G05": warnings.append("Menstruation and Communion: pastoral passage requires current-practice review by Coptic Orthodox clergy.")
    return {"chapter":dict(chapter),"evidence_class":"source_checked_not_expert_approved","grounded_claims":grounded,"research_leads":leads,"coverage":coverage,"editorial_warnings":warnings}

def prepare(ch):
    OUT.mkdir(exist_ok=True)
    b=brief(ch)
    (OUT/f"{ch}_EVIDENCE_BRIEF.json").write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding="utf-8")
    lines=[f"# {ch} — {b['chapter']['title']}","RESEARCH BRIEF — NOT APPROVED FOR PUBLICATION","",f"Checked claims: {len(b['grounded_claims'])}","## Evidence"]
    for claim in b["grounded_claims"]:
        lines += ["",f"### [CLM:{claim['id']}] {claim['classification']}",claim["text"]]
        for item in claim["evidence"]:
            lines.append(f"- {item['section_title']} — {item['locator']}; {item['source_url']} (review: {item['evidence_status']})")
    lines += ["","## Unverified leads — do not cite"]+[f"- {x['id']}: {x['text']}" for x in b["research_leads"]]
    lines += ["","## Open review holds"]+[f"- {x}" for x in b["editorial_warnings"]]
    (OUT/f"{ch}_EVIDENCE_BRIEF.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    instruction=f"""# Drafting instructions: {ch}
Use the chapter evidence brief and master editorial policy.
Produce original, clear, empathetic text for Coptic Orthodox teenagers aged 12–18.
Use English first; adapt to simple Modern Standard Arabic and natural German only after review.
Each source-dependent factual or theological claim must cite a permitted [CLM:<claim-id>] marker.
Do not invent medical facts, church-wide rulings, Bible wording, or patristic quotes.
Paraphrase rather than reproduce protected passages. Flag unresolved matters with [REVIEW-NEEDED: reason].
Use an original fictional introduction, explanation, Orthodox perspective, Q&A, practical advice, reflection and original prayer.
No output is expert-approved or publication-ready.
"""
    (OUT/f"{ch}_DRAFT_PROMPT.md").write_text(instruction,encoding="utf-8")
    return {"chapter":ch,"grounded":len(b["grounded_claims"]),"leads":len(b["research_leads"])}

def check(ch,path):
    text=path.read_text(encoding="utf-8")
    allowed={x["id"] for x in brief(ch)["grounded_claims"]}
    tokens=re.findall(r"\[CLM:([^\]]+)\]",text)
    missing_sections=[h for h in ["## Understanding the topic","## What our Church teaches","## Practical advice"] if h.lower() not in text.lower()]
    invalid=sorted(set(tokens)-allowed)
    report={"chapter":ch,"citation_tokens":len(tokens),"invalid_citations":invalid,"missing_sections":missing_sections,"structurally_valid":bool(tokens) and not invalid and not missing_sections,"publication_approved":False,"warning":"Structural token validation does not prove semantic support, clinical accuracy or publication rights."}
    OUT.mkdir(exist_ok=True)
    (OUT/f"{ch}_DRAFT_CHECK.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("prepare");p.add_argument("chapter_id",choices=["B04","G05"])
    p=sub.add_parser("check");p.add_argument("chapter_id",choices=["B04","G05"]);p.add_argument("draft",type=pathlib.Path)
    a=parser.parse_args()
    print(json.dumps(prepare(a.chapter_id) if a.cmd=="prepare" else check(a.chapter_id,a.draft),ensure_ascii=False,indent=2))

if __name__=="__main__": main()
