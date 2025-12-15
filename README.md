# Employee Management System (CRUD + DB)

## Project Overview
This is an Intermediate Level Python application designed to manage employee records using a **CRUD** (Create, Read, Update, Delete) approach. The application utilizes **SQLite** for persistent data storage, ensuring that records remain saved even after the application closes.

## Features
* **Database Integration:** Automatically creates and connects to an SQLite database (`employees.db`).
* **Add Employee:** Validates unique IDs, unique emails, and numeric salaries before insertion.
* **View Employees:** Displays all records in a formatted table.
* **Search:** Find specific employees using their unique ID.
* **Update:** Modify specific fields (Name, Email, Dept, Salary) while keeping others unchanged. Includes validation to prevent duplicate emails during updates.
* **Delete:** Remove records with a confirmation prompt to prevent accidental deletions.
* **Input Validation:** Robust error handling for invalid data types and empty inputs.

## Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite3 (Standard Python Library)
* **Interface:** Command Line Interface (CLI)

## Project Structure
```text
employee_management/
│
├── app.py           # Main application logic and Menu UI
├── database.py      # Database connection and table setup
├── employees.db     # SQLite database file (auto-generated on first run)
└── README.md        # Project documentation

<img width="975" height="645" alt="image" src="https://github.com/user-attachments/assets/fe97bc4e-8384-4ca8-bffb-ed14162b629d" />
<img width="1003" height="690" alt="image" src="https://github.com/user-attachments/assets/6a6a97cb-0d6a-4930-a01e-2c6d427ea54a" />
<img width="967" height="664" alt="image" src="https://github.com/user-attachments/assets/67f8d8de-ddeb-4633-ae9a-44a51a91e7d9" />
<img width="1170" height="664" alt="image" src="https://github.com/user-attachments/assets/967f1f94-e142-40f2-b906-d4d5c271a6b7" />
<img width="1080" height="683" alt="image" src="https://github.com/user-attachments/assets/bf2173d9-aa5b-4d7d-b95f-2dc4fd51f1cd" />

<img width="1001" height="709" alt="image" src="https://github.com/user-attachments/assets/0d4de3f3-f983-4df3-aebd-f19300fca5e5" />



