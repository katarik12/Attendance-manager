import os
from datetime import datetime

STUDENT_FILE = "students.txt"
ATTENDANCE_FILE = "attendance.txt"


# Create text files
def create_files():

    if not os.path.exists(STUDENT_FILE):
        open(STUDENT_FILE, "w").close()

    if not os.path.exists(ATTENDANCE_FILE):
        open(ATTENDANCE_FILE, "w").close()


# Load student data
def load_students():

    students = []

    with open(STUDENT_FILE, "r") as file:

        for line in file:
            data = line.strip().split(",")

            if len(data) == 3:
                students.append(data)

    return students


# Load attendance data
def load_attendance():

    attendance = []

    with open(ATTENDANCE_FILE, "r") as file:

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                attendance.append(data)

    return attendance


# Add student
def add_student():

    students = load_students()

    roll = input("Enter Roll Number: ").strip()

    if roll == "":
        print("Roll Number cannot be empty!")
        return

    for student in students:

        if student[0].lower() == roll.lower():
            print("Student already exists!")
            return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch/Section: ").strip()

    if name == "" or branch == "":
        print("Name and Branch cannot be empty!")
        return

    with open(STUDENT_FILE, "a") as file:
        file.write(roll + "," + name + "," + branch + "\n")

    print("Student added successfully!")


# View all students
def view_students():

    students = load_students()

    if len(students) == 0:
        print("No students registered!")
        return

    print("\n------- STUDENT LIST -------")

    for student in students:

        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Branch:", student[2])
        print("----------------------------")


# Mark attendance
def mark_attendance():

    students = load_students()
    attendance = load_attendance()

    if len(students) == 0:
        print("Please add students first!")
        return

    subject = input("Enter Subject Name/Code: ").strip()

    if subject == "":
        print("Subject cannot be empty!")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    for record in attendance:

        if record[1].lower() == subject.lower() and record[2] == date:
            print("Attendance already marked for this date!")
            return

    print("\nEnter P for Present and A for Absent")

    records = []

    for student in students:

        while True:

            status = input(
                student[1] + " (" + student[0] + "): "
            ).strip().upper()

            if status == "P" or status == "A":
                break

            print("Invalid input! Enter P or A.")

        records.append(
            student[0] + "," + subject + "," + date + "," + status + "\n"
        )

    with open(ATTENDANCE_FILE, "a") as file:

        for record in records:
            file.write(record)

    print("Attendance marked successfully!")


# Main menu
def main_menu():

    create_files()

    while True:
        print(" COLLEGE ATTENDANCE MANAGER")

        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            mark_attendance()

        elif choice == "4":
            print("Thank you for using College Attendance Manager!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start program
main_menu()
