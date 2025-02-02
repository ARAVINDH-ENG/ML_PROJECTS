import sqlite3
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Function to create database and sample data
def create_database():
    conn = sqlite3.connect("Company_Database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Department_ID INTEGER,
        Position TEXT,
        Salary INTEGER,
        Hire_Date TEXT,
        FOREIGN KEY (Department_ID) REFERENCES Departments(ID)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Manager TEXT
    )
    """)

    # Sample Data
    employees_data = [
        (1, 'Alice', 1, 'Sales Executive', 50000, '2021-01-15'),
        (2, 'Bob', 2, 'Software Engineer', 70000, '2020-06-10'),
        (3, 'Charlie', 3, 'Marketing Specialist', 60000, '2022-03-20'),
        (4, 'David', 2, 'Senior Engineer', 90000, '2018-07-01'),
        (5, 'Eve', 1, 'Sales Manager', 80000, '2019-11-22'),
        (6, 'Frank', 2, 'Lead Developer', 95000, '2021-08-13'),
        (7, 'Grace', 3, 'SEO Specialist', 55000, '2021-12-10'),
        (8, 'Hannah', 1, 'Sales Executive', 48000, '2022-02-25'),
        (9, 'Ian', 2, 'DevOps Engineer', 85000, '2020-05-09'),
        (10, 'Jack', 3, 'Content Writer', 50000, '2022-01-01')
    ]

    departments_data = [
        (1, 'Sales', 'Alice'),
        (2, 'Engineering', 'Bob'),
        (3, 'Marketing', 'Charlie')
    ]
    
    cursor.executemany("INSERT OR IGNORE INTO Employees VALUES (?, ?, ?, ?, ?, ?)", employees_data)
    cursor.executemany("INSERT OR IGNORE INTO Departments VALUES (?, ?, ?)", departments_data)
    
    conn.commit()
    conn.close()

# Extract keywords for query
def extract_keywords(user_input):
    user_input = user_input.lower()
    actions = ['who', 'list', 'show', 'tell', 'what', 'total', 'employees', 'salary', 'department']
    departments = ['sales', 'engineering', 'marketing', 'hr', 'finance', 'it', 'operations', 'admin']
    entities = ['manager', 'salary', 'employees', 'department']

    action = next((word for word in actions if word in user_input), None)
    department = next((word for word in departments if word in user_input), None)
    entity = next((word for word in entities if word in user_input), None)

    return action, department, entity

# Process query and return response
def process_query(user_input):
    action, department, entity = extract_keywords(user_input)
    if not action or not department:
        return "Sorry, I couldn't understand that. Could you please rephrase?"

    conn = sqlite3.connect("Company_Database.db")
    cursor = conn.cursor()

    department_name = department.capitalize()

    if entity == "employees":
        cursor.execute("""
            SELECT Name FROM Employees 
            WHERE Department_ID = (SELECT ID FROM Departments WHERE Name = ?)
        """, (department_name,))
        results = cursor.fetchall()
        if results:
            return [row[0] for row in results]
        else:
            return f"No employees found in the {department_name} department."

    elif entity == "manager":
        cursor.execute("""
            SELECT Manager FROM Departments WHERE Name = ?
        """, (department_name,))
        result = cursor.fetchone()
        if result:
            return f"The manager of the {department_name} department is {result[0]}."
        else:
            return f"Department {department_name} not found."

    elif entity == "salary" or 'total' in user_input:
        cursor.execute("""
            SELECT SUM(Salary) FROM Employees 
            WHERE Department_ID = (SELECT ID FROM Departments WHERE Name = ?)
        """, (department_name,))
        result = cursor.fetchone()
        if result[0]:
            return f"The total salary expense for {department_name} is ${result[0]}."
        else:
            return f"No salary data available for {department_name} department."

    return "Sorry, I didn't understand that. Please rephrase your query."

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = process_query(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    create_database()
    app.run(debug=True)
