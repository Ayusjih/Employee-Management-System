mport database
import sqlite3

# --- validation Helper Functions ---
def is_email_valid(email):
    """Checks if email contains '@'."""
    return "@" in email

def id_exists(emp_id):
    """Checks if an Employee ID already exists in the DB."""
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM employees WHERE emp_id = ?", (emp_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def email_exists(email, current_emp_id=None):
    """
    Checks if an email exists. 
    current_emp_id is used during updates to ignore the user's own email.
    """
    conn = database.get_db_connection()
    cursor = conn.cursor()
    if current_emp_id:
        cursor.execute("SELECT 1 FROM employees WHERE email = ? AND emp_id != ?", (email, current_emp_id))
    else:
        cursor.execute("SELECT 1 FROM employees WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# --- CRUD Functions ---

def add_employee():
    print("\n--- ADD NEW EMPLOYEE ---")
    try:
        # ID Validation
        while True:
            try:
                emp_id = int(input("Enter Employee ID: "))
                if id_exists(emp_id):
                    print("Error: This Employee ID already exists. Try another.")
                else:
                    break
            except ValueError:
                print("Invalid input. ID must be an integer.")

        # Name Validation
        while True:
            name = input("Enter Name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        # Email Validation
        while True:
            email = input("Enter Email: ").strip()
            if not is_email_valid(email):
                print("Error: Invalid email format (must contain '@').")
            elif email_exists(email):
                print("Error: This email is already registered.")
            else:
                break

        # Department Validation
        while True:
            department = input("Enter Department: ").strip()
            if department:
                break
            print("Department cannot be empty.")

        # Salary Validation
        while True:
            try:
                salary = float(input("Enter Salary: "))
                if salary < 0:
                    print("Salary must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Salary must be numeric.")

        # Insert into DB
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (emp_id, name, email, department, salary) VALUES (?, ?, ?, ?, ?)",
                       (emp_id, name, email, department, salary))
        conn.commit()
        conn.close()
        print("Success: Employee added successfully!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_employees():
    print("\n--- VIEW ALL EMPLOYEES ---")
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No records found.")
    else:
        # Formatting output
        print(f"{'ID':<10} {'Name':<20} {'Email':<25} {'Dept':<15} {'Salary':<10}")
        print("-" * 80)
        for row in rows:
            print(f"{row['emp_id']:<10} {row['name']:<20} {row['email']:<25} {row['department']:<15} {row['salary']:<10}")

def search_employee():
    print("\n--- SEARCH EMPLOYEE ---")
    try:
        search_id = int(input("Enter Employee ID to search: "))
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (search_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            print("\nEmployee Found:")
            print(f"ID: {row['emp_id']}")
            print(f"Name: {row['name']}")
            print(f"Email: {row['email']}")
            print(f"Department: {row['department']}")
            print(f"Salary: {row['salary']}")
        else:
            print("Not Found: No employee with that ID.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")