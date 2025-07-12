import json
import os

# File to store student records
filename = "students.json"

# Load student records from file
def load_students():
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

# Save student records to file
def save_students(students):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)

# Add a new student
def add_student(students):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    # Check if roll number already exists
    for student in students:
        if student["roll"] == roll:
            print("Student with this roll number already exists!")
            return

    students.append({
        "roll": roll,
        "name": name,
        "age": age,
        "marks": marks
    })
    print("Student added successfully!")

# View all students
def view_students(students):
    if not students:
        print("No student records found.")
        return
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

# Search student by roll number
def search_student(students):
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student["roll"] == roll:
            print(f"Found: Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
            return
    print("Student not found.")

# Update student record
def update_student(students):
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new Name: ")
            student["age"] = input("Enter new Age: ")
            student["marks"] = input("Enter new Marks: ")
            print("Student record updated.")
            return
    print("Student not found.")

# Delete student record
def delete_student(students):
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student record deleted.")
            return
    print("Student not found.")

# Main program loop
def main():
    students = load_students()

    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save and Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            save_students(students)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
