def get_priority():
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            return priority
        print("Invalid priority. Please enter high, medium, or low.")

def get_time_bound():
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            return time_bound
        print("Please answer with yes or no.")

def main():
    task = input("Enter your task: ").strip()
    priority = get_priority()
    time_bound = get_time_bound()

    reminder = ""

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print("\nReminder:", reminder)


if __name__ == "__main__":
    main()
