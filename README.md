# Student-Management-System
To develop a Python-based Student Management System that allows users to perform essential CRUD (Create, Read, Update, Delete) operations on student data through a command-line interface. The system ensures efficient data handling and presents records in a tabular format using an SQLite database.



🧩 Key Features:



Add Student – Input and store new student information.

View Students – Display all student records in a neat table format.

Search Student – Find a student by their unique ID.

Update Student – Modify existing student details.

Delete Student – Remove a student record by ID.

Persistent Storage – Uses SQLite to save and retrieve data permanently.



🛠️ Modules/Libraries:



sqlite3 – For database operations

tabulate – For pretty console output

os (optional) – For file operations




🏗️ System Workflow:

User launches the app via terminal.

Menu-driven interface appears with options (Add, View, Search, Update, Delete, Exit).

User selects an operation.

The program performs the action and confirms the result.

Loop continues until user chooses to exit.
