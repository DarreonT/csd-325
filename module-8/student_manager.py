import json

# Load student list from JSON file
with open('students.json', 'r') as file:
    students = json.load(file)

# Function to print students
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Notify original list
print("Original Student List:\n")
print_students(students)

# Append your info
new_student = {
    "F_Name": "Darreon",
    "L_Name": "Tolen",
    "Student_ID": 112100,
    "Email": "datolen@my365.bellevue.edu"
}
students.append(new_student)

# Notify updated list
print("\nUpdated Student List:\n")
print_students(students)

# Write the updated list back to JSON file
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)

# Notify file update
print("\nJSON file has been updated.")
