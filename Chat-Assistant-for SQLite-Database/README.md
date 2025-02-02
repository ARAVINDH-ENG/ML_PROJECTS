# Chat Assistant for SQLite Database

## Objective
This project is a Python-based chat assistant that interacts with an SQLite database to answer user queries. The assistant converts natural language queries into SQL commands and fetches relevant data from the database.

## Features
- Accepts natural language queries.
- Converts queries into SQL commands.
- Fetches and returns structured responses from the database.
- Handles errors gracefully, including invalid queries and missing data.

## Database Schema
The SQLite database contains two tables:

### Employees Table
| ID | Name  | Department  | Salary | Hire_Date  |
|----|-------|------------|--------|------------|
| 1  | Alice | Sales      | 50000  | 2021-01-15 |
| 2  | Bob   | Engineering| 70000  | 2020-06-10 |
| 3  | Charlie | Marketing | 60000  | 2022-03-20 |

### Departments Table
| ID | Name        | Manager |
|----|------------|---------|
| 1  | Sales      | Alice   |
| 2  | Engineering| Bob     |
| 3  | Marketing  | Charlie |

## Supported Queries
The chat assistant can handle queries like:
- "Show me all employees in the [department] department."
- "Who is the manager of the [department] department?"
- "List all employees hired after [date]."
- "What is the total salary expense for the [department] department?"

## Setup and Installation
### Prerequisites
- Python 3.8+
- SQLite
- Flask or FastAPI (for deployment)

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/ARAVINDH-ENG/ML_PROJECTS/new/main/Chat-Assistant-for%20SQLite-Database
   cd chat-assistant-sqlite
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the assistant:
   ```bash
   python app.py
   ```
4. Access the chat assistant in your browser at `http://127.0.0.1:5000`

## Deployment
The assistant can be deployed using Flask/FastAPI and hosted on services like Heroku, Vercel, or AWS Lambda.

## Error Handling
- Handles incorrect department names and invalid input formats.
- Provides meaningful responses when no results are found.
- Ensures SQL injection safety.

## Known Limitations & Future Improvements
- Currently supports only predefined query types.
- Does not support complex conversational flows.
- Future enhancements may include machine learning-based NLP processing.

## License
This project is open-source and available under the MIT License.

## Author
Developed by Aravindh R.
