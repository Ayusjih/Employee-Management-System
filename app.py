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
    def update_employee():
        print("\n--- UPDATE EMPLOYEE ---")
    try:
        emp_id = int(input("Enter Employee ID to update: "))
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
        row = cursor.fetchone()

        if not row:
            print("Employee not found.")
            conn.close()
            return

        print(f"Updating details for: {row['name']} (Press Enter to keep current value)")
        
        # Name Update
        new_name = input(f"New Name [{row['name']}]: ").strip()
        final_name = new_name if new_name else row['name']

        # Email Update (Check for unique constraints if changed)
        while True:
            new_email = input(f"New Email [{row['email']}]: ").strip()
            if not new_email:
                final_email = row['email']
                break
            elif not is_email_valid(new_email):
                print("Invalid email format.")
            elif email_exists(new_email, emp_id):
                print("This email is already taken by another employee.")
            else:
                final_email = new_email
                break

        # Dept Update
        new_dept = input(f"New Department [{row['department']}]: ").strip()
        final_dept = new_dept if new_dept else row['department']

        # Salary Update
        while True:
            new_salary_str = input(f"New Salary [{row['salary']}]: ").strip()
            if not new_salary_str:
                final_salary = row['salary']
                break
            try:
                final_salary = float(new_salary_str)
                break
            except ValueError:
                print("Salary must be numeric.")

        # Execute Update
        cursor.execute("""
            UPDATE employees 
            SET name = ?, email = ?, department = ?, salary = ? 
            WHERE emp_id = ?
        """, (final_name, final_email, final_dept, final_salary, emp_id))
        
        conn.commit()
        conn.close()
        print("Success: Employee details updated.")

    except ValueError:
        print("Invalid ID format.")
    except sqlite3.Error as e:
        print(f"Database Error: {e}")

def delete_employee():
    print("\n--- DELETE EMPLOYEE ---")
    try:
        emp_id = int(input("Enter Employee ID to delete: "))
        if not id_exists(emp_id):
            print("Employee not found.")
            return

        confirm = input(f"Are you sure you want to delete Employee {emp_id}? (yes/no): ").lower()
        if confirm == 'yes':
            conn = database.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))
            conn.commit()
            conn.close()
            print("Success: Employee deleted.")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Invalid ID format.")

# --- Main Menu System ---

def main_menu():
    # Ensure table exists before starting
    database.create_table()
    
    while True:
        print("\n=== EMPLOYEE MANAGEMENT SYSTEM ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()