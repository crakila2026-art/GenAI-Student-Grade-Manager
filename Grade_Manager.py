
# Student Grade Manager
# Week 1 - Day 2 Assignment

# Store all student records in a list of dictionaries
students = []


# Function 1: Calculate grade based on marks
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Function 2: Add a new student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    try:
        mark = float(input("Enter student marks (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Marks must be between 0 and 100.")
            return

        grade = get_grade(mark)

        student = {
            "name": name,
            "mark": mark,
            "grade": grade
        }

        students.append(student)

        print(f"Student {name} added successfully!")
        print(f"Grade: {grade}")

    except ValueError:
        print("Error: Please enter a valid number for marks.")


# Function 3: Display student results
def show_results():
    print("\n========== STUDENT RESULTS ==========")

    if not students:
        print("No student records available.")
        print("Please add students first.")
        return

    # Display table heading
    print("-" * 42)
    print(f"{'Name':<20} {'Mark':>8} {'Grade':>8}")
    print("-" * 42)

    # Display each student's details
    for student in students:
        print(
            f"{student['name']:<20} "
            f"{student['mark']:>8.1f} "
            f"{student['grade']:>8}"
        )

    print("-" * 42)

    # Calculate class statistics
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Average : {average:.1f}")
    print(f"Highest : {highest:.1f}")
    print(f"Lowest  : {lowest:.1f}")

    print("=" * 42)


# Function 4: Main menu
def main():
    while True:
        print("\n====== STUDENT GRADE MANAGER ======")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("\nThank you for using Student Grade Manager!")
            print("Program exited successfully.")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Program execution starts here
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram terminated safely.")
