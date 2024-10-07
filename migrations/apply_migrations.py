import os
import sys

from config import get_db_connection

def apply_migrations():
    # Establish a database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get all the migration files in the migrations directory, sorted by filename
    migration_files = sorted(f for f in os.listdir(os.path.dirname(__file__)) if f.endswith('.sql'))

    # Apply each migration file
    for migration_file in migration_files:
        with open(os.path.join(os.path.dirname(__file__), migration_file), 'r') as file:
            sql = file.read()
            cursor.execute(sql)
            print(f"Applied migration: {migration_file}")

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    apply_migrations()
