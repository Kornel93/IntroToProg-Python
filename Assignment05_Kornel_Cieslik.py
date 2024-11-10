# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Kornel Cieslik, 11/8/2024, Created Script
# ------------------------------------------------------------------------------------------ #

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # dictionary of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    with open(FILE_NAME, "r") as file:
        for row in file.readlines():
        # Transform the data from the file
            student_data = row.strip().split(',')
            student_data = {"FirstName": student_data[0],
                            "LastName": student_data[1],
                            "CourseName": student_data[2].strip()}
    # Load it into our collection (list of lists)
            students.append(student_data)
except FileNotFoundError:
    print(f"Error: The File '{FILE_NAME}' was not found. Please ensure it exists in the correct directory")


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            #check to see if the user is putting in alphanumeric keys or not
            if not student_first_name.isalpha():
            #if the user is putting in anything other than alphanumeric, it will raise this ValueError
                raise ValueError ("The first name should only contain letter characters")
            student_last_name = input("Enter the student's last name: ")
            # check to see if the user is putting in alphanumeric keys or not
            if not student_last_name.isalpha():
            # if the user is putting in anything other than alphanumeric, it will raise this ValueError
                raise ValueError ("The last name should only contain letter characters")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        #Prints out various error messages depending on the error that occurs
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue



    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                if students:
                    for student in students:
                        if 'FirstName' in student and 'LastName' in student and 'CourseName' in student:
                            csv_data = f"{student['FirstName']},{student['LastName']},{student['CourseName']}\n"
                            file.write(csv_data)
                        else:
                            #Inform the user if a key is missing
                            print("Error: There is missing student information. Skipping...")
                    print("The following data was saved to file!")
                else:
                    print("No student data available")
        except IOError as e:
            print(f"Error: Could not write to file '{FILE_NAME}'")
        except Exception as e:
            print(f"An unexpected error occurred while saving data: {e}")
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
