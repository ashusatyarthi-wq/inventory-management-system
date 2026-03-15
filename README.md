Console-Based Inventory Management SystemA lightweight Command Line Interface (CLI) application built with Python and MySQL. This project demonstrates foundational CRUD (Create, Read, Update, Delete) operations by connecting a Python script to a relational database to manage inventory records.FeaturesAdd New Items: Insert new products into the database with their quantity and price.View Inventory: Fetch and display all current stock from the database.Update Stock: Modify the quantity or details of existing items.Delete Items: Remove discontinued or out-of-stock products from the system.Persistent Storage: Unlike in-memory lists, all data is safely stored in MySQL, preventing data loss between sessions.Tech StackLanguage: Python 3.xDatabase: MySQLLibrary: mysql-connector-pythonPrerequisitesBefore running this script, ensure you have the following installed:Python 3.xMySQL Server (XAMPP, MySQL Workbench, or CLI)Setup and Installation1. Clone the repositorygit clone [https://github.com/ashusatyarthi-wq/inventory-management-system.git](https://github.com/ashusatyarthi-wq/inventory-management-system.git)
cd inventory-management-system
2. Install required Python librariespip install mysql-connector-python
3. Set up the DatabaseOpen your MySQL client and run the following SQL commands to create the database and table:CREATE DATABASE inventory_db;
USE inventory_db;

CREATE TABLE products (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
4. Configure Database CredentialsOpen main.py (or whatever your Python file is named) and update the database connection variables to match your local MySQL setup:mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin", # <-- Update this
  database="inventory_db"
)
How to RunExecute the Python script in your terminal:python main.py
Follow the on-screen menu prompts to interact with the database.
