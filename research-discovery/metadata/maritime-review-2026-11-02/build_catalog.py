"""Build a source-linked selected-record catalogue; do not infer study eligibility."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS = ROOT.parent.parent / "reports"
records = [(f.stem, json.loads(f.read_text(encoding="utf-8"))["result"][0])
           for f in sorted(ROOT.glob("P*.json"))]
lines = ["# Selected FastTrack records: small-boat detection", "",
         "Retrieved 2 November 2026. These 20 selected records are a reading catalogue, not a final included-study set. "
         "Connector document-type labels and citation counts are metadata, not quality judgements. "
         "Author lists below are abbreviated where the returned record contains fewer names than the stated author count.", ""]
for key, record in records:
    authors = record.get("authors", [])
    author_text = ", ".join(authors)
    if record.get("author_count", len(authors)) > len(authors):
        author_text += ", et al."
    lines.extend([f"**{key}. {author_text} ({record.get('year')}).** "
                  f"[{record['title']}]({record['url']}). "
                  f"{record.get('venue', {}).get('name', '')}. "
                  f"[Cite]({record['cite_url']})", ""])
ids = [r["doi"] for _, r in records]
assert len(ids) == len(set(ids)) == 20
url = "https://literature.researchfasttrack.com/zotero?ids=" + ",".join(ids)
lines.extend([f"[Import all {len(ids)} records into Zotero or download for EndNote]({url}).", "",
              "[Return to the literature review](maritime-small-boats-literature-review-2026-11-02.md).", ""])
(REPORTS / "maritime-small-boats-selected-records-2026-11-02.md").write_text("\n".join(lines), encoding="utf-8")
searches = [json.loads(f.read_text(encoding="utf-8")) for f in sorted(ROOT.glob("S*.json"))]
hits = [r for s in searches for r in s["result"][0].get("results", [])]
summary = {"date": "2026-11-02", "connector": "FastTrack Literature", "endpoint": "https://literature.researchfasttrack.com/mcp",
           "search_calls": len(searches), "duplication_calls": len(list(ROOT.glob("D*.json"))),
           "saturation_calls": len(list(ROOT.glob("G*.json"))), "selected_paper_retrievals": len(records),
           "search_result_occurrences": len(hits),
           "identifier_unique_records": len({str(r.get("doi") or r.get("id")).lower() for r in hits}),
           "warning": "Identifier deduplication is not study-family deduplication. Ranked search results are not eligible-study counts. This is a preliminary review, not a completed systematic review.",
           "selected_ids": ids}
(ROOT / "search-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary))
