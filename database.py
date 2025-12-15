import sqlite3

DB_NAME = "employees.db"

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    """Creates the employees table if it does not exist."""
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS employees (
                emp_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            );
            """
            cursor.execute(query)
            conn.commit()
            conn.close()
            print("Database setup completed successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    create_table()