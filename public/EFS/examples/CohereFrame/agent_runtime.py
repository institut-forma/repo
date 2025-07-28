# agent_runtime.py
# Light agent sync + summary runtime tool for CohereFrame
# Optional, safe to delete — CLI tool for system ops or agent lead

import yaml
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TODAY = date.today().isoformat()

# === Load role definitions
with open(ROOT / "role_definitions.md", "r", encoding="utf-8") as f:
    roles = [line.strip() for line in f if line.startswith("## ")]

# === Load active tasks
with open(ROOT / "task_registry.yaml", "r", encoding="utf-8") as f:
    tasks = yaml.safe_load(f)

# === Print summary report
print("\n📋 Weekly Agent Sync Summary —", TODAY)
print("-" * 42)
print(f"Active Roles: {len(roles)}")
print(f"Active Tasks: {len(tasks)}")
print("Sample Tasks:")
for t in tasks[:3]:
    print(f" - [{t['id']}] {t['title']} ({', '.join(t['owners'])})")
print("-" * 42)

# === Optional: create a stub weekly summary
stub = {
    "week_of": TODAY,
    "themes": [],
    "key_movements": [],
    "reflections": [],
    "field_status": {
        "clarity": "unknown",
        "energy": "unknown",
        "friction": "unknown",
        "trust": "unknown"
    },
    "next_focus": [],
    "compiled_by": "agent_runtime.py"
}

out_path = ROOT / "weekly_summary.yaml"
with open(out_path, "w", encoding="utf-8") as f:
    yaml.dump(stub, f, sort_keys=False)

print(f"\n📁 Stub written to: {out_path}")
