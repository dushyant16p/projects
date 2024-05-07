import os

# Path to desktop directory
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
workout_log_file = os.path.join(desktop_path, 'tst1.txt')

def save_logs(workout_logs):
    with open(workout_log_file, 'w') as file:
        for day, logs in workout_logs.items():
            file.write(f"{day.capitalize()} Workouts:\n")
            for log in logs:
                file.write(f"\nDay {log['day_number']}:\n")
                for exercise in log['exercises']:
                    file.write(f"{exercise['name']}:\n")
                    for set_info in exercise['sets']:
                        file.write(f"Set {set_info['set_number']}: {set_info['weight']} kg x {set_info['reps']} reps\n")
                file.write("\n")

workout_logs = {}

while True:
    print("\n1. Add Workout Log\n2. View Workout Logs\n3. Save Workout Logs\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        day = input("Enter workout day (e.g., push, pull, leg): ").lower()
        day_number = input("Enter day number: ")
        num_exercises = int(input("Enter number of exercises: "))
        workout = {'day': day, 'day_number': day_number, 'exercises': []}

        for _ in range(num_exercises):
            exercise_name = input("Enter exercise name: ")
            sets = int(input("Enter number of sets: "))
            exercise = {'name': exercise_name, 'sets': []}

            for i in range(sets):
                set_number = i + 1
                weight = float(input(f"Enter weight (kg) for Set {set_number}: "))
                reps = int(input(f"Enter reps for Set {set_number}: "))
                exercise['sets'].append({'set_number': set_number, 'weight': weight, 'reps': reps})

            workout['exercises'].append(exercise)

        if day not in workout_logs:
            workout_logs[day] = []
        workout_logs[day].append(workout)
        print("Workout log added successfully.")

    elif choice == '2':
        if not workout_logs:
            print("No workout logs available.")
        else:
            print("Workout Logs:")
            for day, logs in workout_logs.items():
                print(f"\n{day.capitalize()} Workouts:")
                for log in logs:
                    print(f"\nDay {log['day_number']}:")
                    for exercise in log['exercises']:
                        print(f"{exercise['name']}:")
                        for set_info in exercise['sets']:
                            print(f"Set {set_info['set_number']}: {set_info['weight']} kg x {set_info['reps']} reps")

    elif choice == '3':
        save_logs(workout_logs)
        print(f"Workout logs saved to {workout_log_file}")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please choose again.")
