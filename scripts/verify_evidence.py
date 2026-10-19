"""Verify packaged bytes only; this is not a model smoke test."""
from pathlib import Path
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "reproducibility/artifact_checksums.json").read_text(encoding="utf-8"))
failed = []
for relative, expected in manifest.items():
    path = root / relative
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        failed.append(relative)
if failed:
    print("Missing or changed packaged evidence:")
    print("\n".join(failed))
    sys.exit(1)
print(f"PASS: {len(manifest)} packaged evidence files match SHA-256 records.")
print("Training and metric correctness were not evaluated.")
