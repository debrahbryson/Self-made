import csv
import numpy as np

LOG_FILE = "logs/log.csv"

def analyze_data():
    hours = []

    try:
        with open(LOG_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                hours.append(float(row["hours"]))

        data = np.array(hours)

        print("\n📊 Productivity Analysis")
        print(f"Total hours: {np.sum(data):.2f}")
        print(f"Average per entry: {np.mean(data):.2f}")
        print(f"Max session: {np.max(data):.2f}")
        print(f"Standard deviation: {np.std(data):.2f}")

    except FileNotFoundError:
        print("No logs found. Log some activities first.")
