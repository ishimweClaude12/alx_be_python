# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Simple loop to ensure priority input is valid
while priority not in ["high", "medium", "low"]:
    print("Invalid input. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").strip().lower()

# Process the task with Match Case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# Modify message if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

# Output the customized reminder
print("\nReminder:", message)
