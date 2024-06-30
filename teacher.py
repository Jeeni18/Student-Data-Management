import re
from file_management import read_file, write_to_file, append_to_file
from exceptions import NoMatchingNameError, AuthenticationError

TEACHER_FILE = "data_file/teacher.json"
STUDENT_FILE = "data_file/student.json"

def load_json(file_path):
    return read_file(file_path)

def dump_json(file_path, data):
    write_to_file(file_path, data)

class Teacher:
    def __init__(self, name, subject, id, address, email, phone_number):
        self.name = name
        self.subject = subject
        self.id = id
        self.address = address
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def validate_email(email):
        """Checks if the email format is correct or not

        Args:
            email (string) 

        Returns:
            string: returns email if the format is correct
        """
        return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

    @staticmethod
    def validate_phone_number(phone_number):
        """Checks if the phone number format is correct or not

        Args:
            phone_number (int)

        Returns: whether an object is an instance of a class or of a subclass thereof.
        """
        return isinstance(phone_number, int) and len(str(phone_number)) == 10

    @classmethod
    def authenticate(cls):
        print("Verfify as a teacher to add new record")
        name = input("Enter your name: ")
        id = input("Enter your ID: ")
        teachers = load_json(TEACHER_FILE)
        for teacher in teachers:
            if teacher['name'] == name and teacher['id'] == id:
                print("Authentication successful.")
                return True
        raise AuthenticationError("Authentication failed.")

    @classmethod
    def accept(cls):
        """Accept new teacher details from the user and store them in the file.

            Raises:   AuthenticationError: If the authentication fails.
        """
        name = input("Enter name: ")
        subject = input("Enter subject: ")
        id = input("Enter ID: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        while not cls.validate_email(email):
            print("Invalid email. Please enter again.")
            email = input("Enter email: ")
        phone_number = int(input("Enter phone number: "))
        while not cls.validate_phone_number(phone_number):
            print("Invalid phone number. Please enter again.")
            phone_number = int(input("Enter phone number: "))

        teacher = cls(name, subject, id, address, email, phone_number)
        append_to_file(TEACHER_FILE, teacher.__dict__)

    @staticmethod
    def display_all():
        """
            Display general public information of all teachers.
        """
        teachers = load_json(TEACHER_FILE)
        for teacher in teachers:
            print(f"Name: {teacher['name']}, Email: {teacher['email']}, Phone: {teacher['phone_number']}, Subject: {teacher['subject']}")

    @staticmethod
    def search(name):
        """Search and display full details of a teacher by name.

        Args:
            name (string): Name of the teacher to be searched

        Raises:
            NoMatchingNameError: If no matching record is found.

        """
        teachers = load_json(TEACHER_FILE)
        for teacher in teachers:
            if teacher['name'] == name:
                print(teacher)
                return teacher
        raise NoMatchingNameError(f"No matching record for name: {name}")

    @staticmethod
    def delete(name):
        """Delete the record of a teacher by name.

        Args:
            name (string): Name of the teacher to be deleted
        """
        teachers = load_json(TEACHER_FILE)
        updated_teachers = [teacher for teacher in teachers if teacher['name'] != name]
        dump_json(TEACHER_FILE, updated_teachers)


