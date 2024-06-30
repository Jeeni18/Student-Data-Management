from file_management import read_file, write_to_file, append_to_file
from exceptions import NoMatchingNameError

STUDENT_FILE = "data_file/student.json"

def load_json(file_path):
    """Load JSON data from a file.

    Args:
        file_path (str): The path to the JSON file

    Returns:
        list: The data loaded from the file, or an empty list if the file is not found.
    """
    return read_file(file_path)

def dump_json(file_path, data):
    """Write JSON data to a file.

    Args:
        file_path (str): The path to the JSON file.
        data (list): The data to write to the file
    """
    write_to_file(file_path, data)

class Student:

    def __init__(self, name, roll_number, email, phone_number, marks, address):
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.phone_number = phone_number
        self.marks = marks
        self.address = address

    @classmethod
    def accept(cls):
        """
        Accept student information from the user
        """
        name = input("Enter name: ")
        roll_number = input("Enter roll number: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")

        marks = {}
        subjects = ["English", "Maths", "Science", "Social Studies"]
        for subject in subjects:
            marks[subject] = int(input(f"Enter marks for {subject}: "))

        address = input("Enter address: ")

        student = cls(name, roll_number, email, phone_number, marks, address)
        append_to_file(STUDENT_FILE, student.__dict__)

    @staticmethod
    def display_all():
        """
        Displays information of all student
        """
        students = load_json(STUDENT_FILE)
        for student in students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Email: {student['email']}, Phone: {student['phone_number']}, Marks: {student['marks']}, Address: {student['address']}")

    @staticmethod
    def search(name):
        """Search for a student by name and display full details.

        Args:
            name (string): Student name to be searched

        Raises:
            NoMatchingNameError: If no student with the given name is found.

        """
        students = load_json(STUDENT_FILE)
        for student in students:
            if student['name'] == name:
                print(student)
                return student
        raise NoMatchingNameError(f"No matching record for name: {name}")

    @staticmethod
    def pass_fail_determination():
        """Determine and display the pass/fail status of each student.
        """
        students = load_json(STUDENT_FILE)
        for student in students:
            if all(mark >= 40 for mark in student['marks'].values()):
                print(f"{student['name']} has passed.")
            else:
                print(f"{student['name']} has failed.")

    @staticmethod
    def highest_and_lowest_scores():
        """Display the highest and lowest scores among all students.
        """
        students = load_json(STUDENT_FILE)
        if not students:
            print("No students found.")
            return
        
        highest = max(students, key=lambda x: max(x['marks'].values()))
        lowest = min(students, key=lambda x: min(x['marks'].values()))

        print(f"Highest Scorer: {highest['name']}, Marks: {max(highest['marks'].values())}")
        print(f"Lowest Scorer: {lowest['name']}, Marks: {min(lowest['marks'].values())}")

    @staticmethod
    def percentage(name):
        """Display the percentage of a student

        Args:
            name (string): Name of student whose details is to be searched
        """
        students = load_json(STUDENT_FILE)
        for student in students:
            if student['name'] == name:
                total_marks = sum(student['marks'].values())
                percentage = total_marks / len(student['marks'])
                print(f"Percentage for {student['name']}: {percentage}%")
                return
        print(f"No student found with name: {name}")

    @staticmethod
    def rank_calculation():
        """Calculate and display the rank of each student.
        """
        students = load_json(STUDENT_FILE)
        students.sort(key=lambda x: sum(x['marks'].values()), reverse=True)
        rank = 1
        for student in students:
            print(f"Rank {rank}: {student['name']}, Total Marks: {sum(student['marks'].values())}")
            rank += 1


