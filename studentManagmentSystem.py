students = []

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    students.append({"name": name, "id": student_id})
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for student in students:
        print(f"Name: {student['name']}, ID: {student['id']}")
    print()

def search_student():
    search_id = input("Enter student ID to search: ")
    for student in students:
        if student["id"] == search_id:
            print(f"Student found: {student['name']}\n")
            return
    print("Student not found.\n")

def delete_student():
    delete_id = input("Enter student ID to delete: ")
    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")

def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()