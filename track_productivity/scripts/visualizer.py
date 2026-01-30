import csv
import matplotlib.pyplot as plt

LOG_FILE = "logs/log.csv"

def plot_summary():
    activities = {}

    try:
        with open(LOG_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                activity = row["activity"]
                hours = float(row["hours"])
                activities[activity] = activities.get(activity, 0) + hours

        plt.bar(activities.keys(), activities.values())
        plt.title("Time Spent per Activity")
        plt.xlabel("Activity")
        plt.ylabel("Hours")
        plt.show()

    except FileNotFoundError:
        print("No logs available to plot.")
