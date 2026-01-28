import time
from datetime import datetime

DATA_FILE = "study_sessions.txt"


class SessionFile:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a+")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class StudySession:
    def __init__(self, subject, focus_level):
        self.subject = subject
        self.focus_level = focus_level
        self.start_time = datetime.now()
        self.end_time = None

    def end(self):
        self.end_time = datetime.now()

    @property
    def duration_minutes(self):
        delta = self.end_time - self.start_time
        return round(delta.total_seconds() / 60, 2)

    def serialize(self):
        return f"{self.subject},{self.start_time},{self.end_time},{self.duration_minutes},{self.focus_level}\n"


def session_stream(filename=DATA_FILE):
    try:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip().split(",")
    except FileNotFoundError:
        return


class StudyTracker:
    def __init__(self):
        self.current_session = None

    def start_session(self):
        subject = input("📚 Subject: ").strip()
        focus = input("🎯 Focus level (1–10): ").strip()

        self.current_session = StudySession(subject, focus)
        print(f"⏱ Started studying {subject}...")

    def end_session(self):
        if not self.current_session:
            print("❌ No active session")
            return

        self.current_session.end()

        with SessionFile() as file:
            file.write(self.current_session.serialize())

        print(
            f"✅ Session ended — {self.current_session.duration_minutes} minutes"
        )

        self.current_session = None

    def show_summary(self):
        total_time = {}
        sessions = 0

        for subject, _, _, duration, _ in session_stream():
            duration = float(duration)
            total_time[subject] = total_time.get(subject, 0) + duration
            sessions += 1

        print("\n📊 Study Summary")
        for subject, minutes in total_time.items():
            print(f"{subject}: {round(minutes / 60, 2)} hours")

        print(f"Total sessions: {sessions}\n")


def main():
    tracker = StudyTracker()

    while True:
        print("""
1. Start study session
2. End study session
3. View summary
4. Exit
""")
        choice = input("Choose: ").strip()

        if choice == "1":
            tracker.start_session()
        elif choice == "2":
            tracker.end_session()
        elif choice == "3":
            tracker.show_summary()
        elif choice == "4":
            print("👋 Keep grinding.")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
