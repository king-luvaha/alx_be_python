# daily_reminder.py

# Get task description (no empty input)
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a task.")

# Get priority with validation
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in {"high", "medium", "low"}:
        break
    print("Please enter one of the following: high, medium, low")

# Get time-bound with validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in {"yes", "no"}:
        break
    print("Please enter 'yes' or 'no'.")

# Process priority with match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(f"Reminder: {reminder}")
