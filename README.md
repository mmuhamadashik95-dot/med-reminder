# med-reminder

A small Python CLI to schedule medicine reminders: add a medicine with its dose
and daily times, list today's schedule, and check what is due.

> ⚠️ Educational/demo only — not medical advice. Always consult your pharmacist or doctor.

## Usage

```bash
python src/reminder.py add Paracetamol 500mg 08:00,20:00
python src/reminder.py list
python src/reminder.py due 09:00
```

Reminders are stored in `reminders.json` (override with `MED_REMINDER_STORE`).
A `.gitignore` keeps personal reminder data out of git.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Author

M.Muhamad Ashik — Founder @ Prescripsy · Contact: prescripsy@prescripsy.space
