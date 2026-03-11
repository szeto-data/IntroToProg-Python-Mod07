# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Andrew Szeto,03/09/2026,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Create a Person Class
class Person:
    """
    A class representing person data.

    Properties:
    - first_name: str: The person's first name.
    - last_name: str: The person's last name.

    ChangeLog:
    - Andrew Szeto, 03/09/2026: Created the class.
    """

    # Add first_name and last_name properties to the constructor
    def __init__(self, first_name: str = '', last_name: str = ''):
        """
        Constructor for first_name and last_name.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the constructor.

        :param first_name: string for first name
        :param last_name: string for last name
        """
        self.first_name = first_name
        self.last_name = last_name

    # Create a getter and setter for the first_name property
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        """
        Getter for the first_name property.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the property.

        :return: string for first name
        """
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        """
        Setter for the first_name property

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the property.

        :param value: string to assign the first name

        :return: None
        """
        if value.isalpha():  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should be alphabetic and not empty.")

    # Create a getter and setter for the last_name property
    @property
    def last_name(self):
        """
        Getter for the last_name property.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the property.

        :return: string for last name
        """
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        """
        Setter for the last_name property

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the property.

        :param value: string to assign the last name

        :return: None
        """
        if value.isalpha():  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should be alphabetic and not empty.")

    # Override the __str__() method to return Person data
    def __str__(self):
        """
        Override for the __str__ method.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created an override method.

        :return: string of comma-separated first and last name
        """
        return f'{self.first_name},{self.last_name}'


# Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection data about students.

    Properties:
    - course_name (str): The name of the course.

    ChangeLog: (Who, When, What)
    Andrew Szeto,03/09/2026,Created Class
    """

    # Call to the Person constructor and pass it the first_name and last_name data
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        """
        Constructor for first_name and last_name.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the constructor.

        :param first_name: string for first name
        :param last_name: string for last name
        :param course_name: string for course name
        """
        super().__init__(first_name=first_name, last_name=last_name)

        # Add an assignment to the course_name property using the course_name parameter
        self.course_name = course_name

    # Add the getter for course_name
    @property
    def course_name(self):
        """
        Getter for the course_name property.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the property.

        :return: string for course name
        """
        return self.__course_name

    # Add the setter for course_name
    @course_name.setter
    def course_name(self, value: str):
        """
        Setter for the course_name property

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created the property.

        :param value: string to assign the course name

        :return: None
        """
        if value != "":
            self.__course_name = value
        else:
            raise ValueError("The course name should not be empty.")

    # Override the __str__() method to return the Student data
    def __str__(self):
        """
        Override for the __str__ method.

        ChangeLog:
        - Andrew Szeto, 03/09/2026: Created an override method.

        :return: string of comma-separated first, last, and course name
        """
        result = super().__str__()
        return f'{result},{self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    Andrew Szeto,03/09/2026,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a JSON file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows of Students

        :return: list
        """
        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            for student in json_students:
                list_of_student_data = Student(first_name=student['FirstName'],
                                               last_name=student['LastName'],
                                               course_name=student['CourseName'])
                student_data.append(list_of_student_data)

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a JSON file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file = None

        try:
            # Add code to convert Student objects into dictionaries
            list_of_dictionary_data: list = []

            for student in student_data:
                student_json = {'FirstName': student.first_name,
                                'LastName': student.last_name,
                                'CourseName': student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file, indent=2)

            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Andrew Szeto,03/09/2026,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            # Add code to access Student object data instead of dictionary data
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

        for student in student_data:
            # Add code to show a string of comma-separated values for each row
            print(student)
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Andrew Szeto,03/09/2026,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")

            # Replace this code to use a Student objects instead of a dictionary objects
            student = Student(first_name=student_first_name,
                              last_name=student_last_name,
                              course_name=course_name)

            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
