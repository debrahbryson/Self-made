import csv
from datetime import datetime
import os

LOG_FILE = "logs/log.csv"

def log_activity():
    activity = input("Activity name: ")
    duration = float(input("Duration (hours): "))
    date = datetime.now().strftime("%Y-%m-%d")

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["date", "activity", "hours"])

        writer.writerow([date, activity, duration])

    print("✅ Activity logged successfully")
