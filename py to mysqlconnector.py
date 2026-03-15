import mysql.connector
from mysql.connector import Error

def insert_mysql_row():
    try:
        # 1. Establish connection to your active MySQL server
        conn = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='admin',
            password='admin'
        )

        if conn.is_connected():
            cursor = conn.cursor()
            
            # 2. Execute the insert using parameterized queries
            sql_query = "INSERT INTO employees (name, role) VALUES (%s, %s)"
            data_tuple = ("John Smith", "Data Scientist")
            
            cursor.execute(sql_query, data_tuple)
            
            # 3. Commit the transaction
            conn.commit()
            print(f"Success: Inserted {cursor.rowcount} row into MySQL.")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # 4. Clean up connections
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    insert_mysql_row()