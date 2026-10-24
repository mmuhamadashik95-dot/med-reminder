"""med-reminder: schedule medicine reminders, list today's schedule, check what's due.
Educational/demo only — not medical advice.
"""
import json, os, sys
from datetime import datetime

DEFAULT_STORE = os.path.join(os.path.dirname(__file__), "..", "reminders.json")

def load(store):
    if os.path.exists(store):
        with open(store) as f:
            return json.load(f)
    return []

def save(store, data):
    with open(store, "w") as f:
        json.dump(data, f, indent=2)

def add_reminder(store, name, dose, times):
    """times: list of 'HH:MM' strings. Returns the new entry."""
    for t in times:
        datetime.strptime(t, "%H:%M")  # validates format
    data = load(store)
    entry = {"name": name, "dose": dose, "times": sorted(times)}
    data.append(entry)
    save(store, data)
    return entry

def todays_schedule(store):
    """All reminders, each expanded to today's dose times."""
    out = []
    for r in load(store):
        for t in r["times"]:
            out.append({"name": r["name"], "dose": r["dose"], "time": t})
    return sorted(out, key=lambda x: x["time"])

def due_now(store, now_hhmm):
    """Reminders due at or before now_hhmm today (simple due check)."""
    return [s for s in todays_schedule(store) if s["time"] <= now_hhmm]

def main(argv):
    store = os.environ.get("MED_REMINDER_STORE", DEFAULT_STORE)
    if len(argv) < 2:
        print("Usage: reminder.py add <name> <dose> <HH:MM,...> | list | due <HH:MM>")
        return 1
    cmd = argv[1]
    if cmd == "add":
        _, _, name, dose, times = argv
        e = add_reminder(store, name, dose, times.split(","))
        print(f"Added: {e['name']} {e['dose']} at {', '.join(e['times'])}")
    elif cmd == "list":
        for s in todays_schedule(store):
            print(f"{s['time']} - {s['name']} ({s['dose']})")
    elif cmd == "due":
        for s in due_now(store, argv[2]):
            print(f"DUE {s['time']} - {s['name']} ({s['dose']})")
    else:
        print("Unknown command:", cmd); return 1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
