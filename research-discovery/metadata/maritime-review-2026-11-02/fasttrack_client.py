"""Read-only FastTrack MCP queries, with raw responses retained for reproducibility."""
import concurrent.futures
import json
import pathlib
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
URL = "https://literature.researchfasttrack.com/mcp"

def run(job):
    payload = {"jsonrpc": "2.0", "id": job["id"], "method": "tools/call",
               "params": {"name": job["tool"], "arguments": job["arguments"]}}
    request = urllib.request.Request(URL, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=100) as response:
                raw = response.read().decode()
            (ROOT / (job["id"] + ".raw.txt")).write_text(raw, encoding="utf-8")
            data = json.loads(raw) if raw.lstrip().startswith("{") else json.loads(next(
                line[6:] for line in raw.splitlines() if line.startswith("data: ")))
            result = data.get("result", data)
            content = result.get("content", [])
            parsed = []
            for block in content:
                if block.get("type") == "text":
                    try:
                        parsed.append(json.loads(block["text"]))
                    except ValueError:
                        parsed.append(block["text"])
            output = {"request": job, "result": parsed or result}
            (ROOT / (job["id"] + ".json")).write_text(json.dumps(output, indent=2), encoding="utf-8")
            return {"id": job["id"], "saved": True, "bytes": len(raw), "error": result.get("isError", False)}
        except Exception as exc:
            if attempt == 2:
                return {"id": job["id"], "saved": False, "error": str(exc)}
            time.sleep(2)

if __name__ == "__main__":
    jobs = json.loads((ROOT / sys.argv[1]).read_text(encoding="utf-8"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for outcome in pool.map(run, jobs):
            print(json.dumps(outcome), flush=True)
