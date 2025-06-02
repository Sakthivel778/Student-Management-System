import sqlite3

# Connect to database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)''')

conn.commit()
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("✅ Student added successfully.\n")
from tabulate import tabulate

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        headers = ["ID", "Name", "Age", "Course"]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No records found.\n")

def search_student():
    student_id = input("Enter student ID to search: ")
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("❌ Student not found.\n")
def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("New name: ")
    age = input("New age: ")
    course = input("New course: ")
    cursor.execute("UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
                   (name, age, course, student_id))
    conn.commit()
    print("✅ Student updated.\n")
def delete_student():
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("🗑️ Student deleted.\n")
def menu():
    while True:
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()
