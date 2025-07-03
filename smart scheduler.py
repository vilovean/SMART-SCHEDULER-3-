def display_menu():
    print("\nExam Scheduler Menu")
    print("-------------------")
    print("1. Add a new exam")
    print("2. View all exams")
    print("3. Edit an exam entry")
    print("4. Delete an exam entry")
    print("5. Exit")

def add_exam(exams):
    print("\nAdd New Exam")
    name = input("Enter exam name: ").strip()
    date = input("Enter exam date (YYYY-MM-DD): ").strip()
    time = input("Enter exam time (HH:MM): ").strip()
    room = input("Enter assigned room: ").strip()

    exam = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }
    exams.append(exam)
    print(f"Exam '{name}' added successfully.")

def view_exams(exams):
    print("\nAll Scheduled Exams")
    if not exams:
        print("No exams scheduled.")
        return
    for idx, exam in enumerate(exams, start=1):
        print(f"{idx}. {exam['name']} - Date: {exam['date']}, Time: {exam['time']}, Room: {exam['room']}")

def edit_exam(exams):
    if not exams:
        print("\nNo exams to edit.")
        return
    view_exams(exams)
    try:
        idx = int(input("\nEnter the exam number to edit: "))
        if idx < 1 or idx > len(exams):
            print("Invalid exam number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    exam = exams[idx - 1]
    print(f"\nEditing Exam '{exam['name']}' (Leave blank to keep current value)")

    name = input(f"Enter new exam name [{exam['name']}]: ").strip()
    date = input(f"Enter new exam date [{exam['date']}]: ").strip()
    time = input(f"Enter new exam time [{exam['time']}]: ").strip()
    room = input(f"Enter new assigned room [{exam['room']}]: ").strip()

    if name:
        exam['name'] = name
    if date:
        exam['date'] = date
    if time:
        exam['time'] = time
    if room:
        exam['room'] = room

    print("Exam updated successfully.")

def delete_exam(exams):
    if not exams:
        print("\nNo exams to delete.")
        return
    view_exams(exams)
    try:
        idx = int(input("\nEnter the exam number to delete: "))
        if idx < 1 or idx > len(exams):
            print("Invalid exam number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    removed_exam = exams.pop(idx - 1)
    print(f"Exam '{removed_exam['name']}' deleted successfully.")

def main():
    exams = []
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            add_exam(exams)
        elif choice == '2':
            view_exams(exams)
        elif choice == '3':
            edit_exam(exams)
        elif choice == '4':
            delete_exam(exams)
        elif choice == '5':
            print("Exiting Exam Scheduler. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
