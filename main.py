from file_management import read_file, write_to_file, append_to_file
from teacher import Teacher
from student import Student
from exceptions import NoMatchingNameError, AuthenticationError,NoMatchingIdError

def add_student():
    """
    Adds a new student by collecting user input and calling the accept method of the Student class.
    """
    try:
        if Teacher.authenticate():
            Student.accept()
            print("Student added successfully.")
    except NoMatchingNameError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_teacher():
    """Adds a new teacher by collecting user input and calling the accept method of the Teacher class.
    """
    try:
        Teacher.accept()
        print("Teacher added successfully.")
    except NoMatchingIdError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_students():
    """
    Displays all student records.
    """
    try:
        Student.display_all()
    except Exception as e:
        print(f"An error occurred: {e}")

def view_teachers():
    """
    Displays all teacher records.
    """
    try:
        Teacher.display_all()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to display the menu and handle user choices.
    """
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Add Teacher")
        print("4. View Teachers")
        print("5. Pass/Fail Determination")
        print("6. Highest and Lowest Scores")
        print("7. Percentage Calculation")
        print("8. Rank Calculation")
        print("9. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            add_teacher()
        elif choice == 4:
            view_teachers()
        elif choice == 5:
            Student.pass_fail_determination()
        elif choice == 6:
            Student.highest_and_lowest_scores()
        elif choice == 7:
            name = input("Enter student's name: ")
            Student.percentage(name)
        elif choice == 8:
            Student.rank_calculation()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

