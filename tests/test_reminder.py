import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from reminder import add_reminder, todays_schedule, due_now

class TestReminder(unittest.TestCase):
    def setUp(self):
        self.store = os.path.join(tempfile.mkdtemp(), "r.json")
    def test_add_and_list(self):
        add_reminder(self.store, "Paracetamol", "500mg", ["08:00", "20:00"])
        sched = todays_schedule(self.store)
        self.assertEqual(len(sched), 2)
        self.assertEqual(sched[0]["time"], "08:00")
    def test_due(self):
        add_reminder(self.store, "Amoxicillin", "250mg", ["08:00", "14:00"])
        due = due_now(self.store, "09:00")
        self.assertEqual([d["time"] for d in due], ["08:00"])
    def test_bad_time_rejected(self):
        with self.assertRaises(ValueError):
            add_reminder(self.store, "X", "1mg", ["25:00"])
    def test_sorted(self):
        add_reminder(self.store, "Y", "1mg", ["21:00", "07:00"])
        self.assertEqual([s["time"] for s in todays_schedule(self.store)], ["07:00", "21:00"])

if __name__ == "__main__":
    unittest.main()
