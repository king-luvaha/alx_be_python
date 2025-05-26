def get_task():
    task = input("Enter your task for today: ").strip()
    return task

def get_priority():
    priority = input("Enter task priority (High/Medium/Low): ").strip().capitalize()
    valid_priorities = ["High", "Medium", "Low"]
    while priority not in valid_priorities:
        print("Invalid priority. Please enter High, Medium, or Low.")
        priority = input("Enter task priority (High/Medium/Low): ").strip().capitalize()
    return priority

def get_time_bound():
    time_bound = input("Is this task time-bound? (Yes/No): ").strip().lower()
    while time_bound not in ["yes", "no"]:
        print("Please answer with Yes or No.")
        time_bound = input("Is this task time-bound? (Yes/No): ").strip().lower()
    return time_bound == "yes"

def create_reminder(task, priority, time_bound):
    match priority:
        case "High":
            priority_msg = "🔥 High Priority!"
        case "Medium":
            priority_msg = "⚡ Medium Priority"
        case "Low":
            priority_msg = "✅ Low Priority"
        case _:
            priority_msg = ""

    if time_bound:
        time_msg = "⏰ This task has a deadline. Don't forget to schedule it!"
    else:
        time_msg = "📅 No specific deadline for this task."

    reminder = (
        f"Reminder:\n"
        f"Task: {task}\n"
        f"Priority: {priority_msg}\n"
        f"{time_msg}"
    )
    return reminder

def main():
    print("=== Daily Reminder Setup ===")
    task = get_task()
    priority = get_priority()
    time_bound = get_time_bound()
    
    reminder_message = create_reminder(task, priority, time_bound)
    print("\n" + "="*30)
    print(reminder_message)
    print("="*30 + "\n")

if __name__ == "__main__":
    main()
