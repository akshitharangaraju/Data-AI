📌 Objective
To verify that the MongoDB-based system works correctly for all database operations including CRUD operations, validation, transactions, integration scenarios, indexing, and backup & restore.

📌 Scope
Testing includes:
Students, Courses, Departments, Instructors, Enrollments collections
CRUD operations
Query operations
Aggregation and indexing
Data validation
Transactions
Backup and restore
Application integration scenarios

📌 Out of Scope
UI testing
Cloud deployment testing

📌 Tools Used
MongoDB Community Server
MongoDB Database Tools (mongodump, mongorestore)
MongoDB Shell (mongosh)
Python (PyMongo)
VS Code
Windows OS

📌 Test Environment
Database: collegeDB
MongoDB: Local instance
Programming Language: Python
Operating System: Windows

📌 Test Data
🔹 Valid Student Data
{
  "student_id": 101,
  "name": "Aarav Sharma",
  "age": 20,
  "email": "aarav@gmail.com",
  "department_id": "CSE"
}
🔹 Invalid Student Data
{
  "student_id": 102,
  "age": 10,
  "email": "invalidemail"
}
🔹 Course Data
{
  "course_id": "CS101",
  "course_name": "Data Structures",
  "credits": 4,
  "instructor_id": "INS01"
}

📌 Execution Summary
All planned test cases were executed
All critical functionalities passed
System behaved as expected for both valid and invalid inputs

📌 Bug Report
🐞 Bug 1
Bug ID: BUG-01
Description: Student record was inserted without email during early testing
Cause: Schema validation was not implemented
Severity: Medium
Status: Fixed
✔ Fix Implemented
Added MongoDB JSON Schema validation to students collection
Enforced email format and age constraints

📌 Conclusion
The MongoDB system was thoroughly tested using functional testing, validation testing, transaction testing, integration testing, and backup & restore testing.
All issues identified during testing were resolved, and the system is stable and ready for real-world usage.