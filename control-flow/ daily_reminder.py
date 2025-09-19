#Create a simplified Python script that uses conditional statements, 
# Match Case, and loops to remind the user about a single, 
# priority task for the day based on time sensitivity.


task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task that requires attention during the week!")     
        
elif priority == "medium":
    if time_bound == "yes":
        print(f"Just remember to do it before time is up.")
    else:
        print(f"Do it at your own pace.")
else:
    if time_bound == "yes":
        print(f"Note: '{task}' is a low priority task. Consider completing aweek or day before the deadline.")
    else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
