# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: Using constants, variables, print statements to display msgs
# about student registration. Similar to last assignment program, 04
# Max Mikos, Sept25, 2024, Created Script
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
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user. 
student_data: dict[str,str] = {} #a table of student data
students: list = []  # a table of student data
parts:list[str] #temp variable to store keys



# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        
        # Transform the data from the file
        parts = row.strip().split(',')
        student_first_name = parts[0]
        student_last_name = parts[1]
        course_name = parts[2]
        student_data = {
            'first_name': student_first_name,
            'last_name': student_last_name,
            'course_name': course_name
            }
        
        # Load it into our collection (list of lists)
        students.append(student_data)
    
except FileNotFoundError:
        print("File not found.Creating a new file.")
        file =open(FILE_NAME, "w") #open file to write
        file.close() #close file right after its made
    
except Exception as e: #show an error msg and at last close file if it wasn't closed
    print("unknown error! ", e)
            
finally:
        if file and not file.closed: 
            file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data and force proper data entry (not empty and no spaces)
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ").strip()
        while not student_first_name: #is user input's empty
            print("You need to actually enter a valid name")
            student_first_name = input("Enter the student's first name: ").strip()
            
        student_last_name = input("Enter the student's last name: ").strip()
        while not student_last_name: #empty user input
            print("You need to actually enter a valid Last Name")
            student_last_name = input("Enter the student's last name: ").strip()
       
        course_name = input("Please enter the name of the course: ").strip()
        while not course_name: #empty user input
            print("You need to actually enter a Course Name")
            course_name = input("Please enter the name of the course: ").strip()
            
        student_data = {
                        'first_name': student_first_name,
                        'last_name': student_last_name,
                        'course_name': course_name
                        }
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("\n Current Enrollment Data ")
        print("-"*50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['first_name']},{student['last_name']},{student['course_name']}\n"
                file.write(csv_data)
                
            print("\nThe following data was saved to file: \n")
         
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}.")

        #show an error msg and at last close file if it wasn't closed
        except Exception as e: 
            print("error saving data to file! ", e)
    
        finally:
            if file and not file.closed: 
                file.close()
                

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, 4.")

print("Program Ended. You may close this window!")

