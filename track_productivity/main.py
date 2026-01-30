from scripts.logger import log_activity
from scripts.analyzer import analyze_data
from scripts.visualizer import plot_summary

def main():
    print("=== Productivity Tracker ===")
    print("1. Log activity")
    print("2. Analyze data")
    print("3. Visualize data")

    choice = input("Choose an option: ")

    if choice == "1":
        log_activity()
    elif choice == "2":
        analyze_data()
    elif choice == "3":
        plot_summary()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
