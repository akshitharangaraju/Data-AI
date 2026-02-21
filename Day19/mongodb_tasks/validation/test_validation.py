from pymongo import MongoClient
from pymongo.errors import WriteError

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
students = db["students"]

print("\n===== DATA VALIDATION TESTING =====")

# ✅ Valid Insert
print("\nTest 1: Valid student insert")
try:
    students.insert_one({
        "student_id": 301,
        "name": "Valid Student",
        "age": 22,
        "email": "validstudent@gmail.com",
        "department_id": "CSE"
    })
    print("Actual Result: Inserted")
    print("Status: PASS")
except Exception as e:
    print("Actual Result:", e)
    print("Status: FAIL")

# ❌ Invalid Age
print("\nTest 2: Invalid age (below 16)")
try:
    students.insert_one({
        "student_id": 302,
        "name": "Invalid Age",
        "age": 10,
        "email": "invalidage@gmail.com",
        "department_id": "ECE"
    })
    print("Actual Result: Inserted")
    print("Status: FAIL")
except Exception as e:
    print("Actual Result: Rejected")
    print("Status: PASS")

# ❌ Invalid Email
print("\nTest 3: Invalid email format")
try:
    students.insert_one({
        "student_id": 303,
        "name": "Invalid Email",
        "age": 25,
        "email": "invalid-email",
        "department_id": "IT"
    })
    print("Actual Result: Inserted")
    print("Status: FAIL")
except Exception as e:
    print("Actual Result: Rejected")
    print("Status: PASS")

# ❌ Missing Name
print("\nTest 4: Missing name field")
try:
    students.insert_one({
        "student_id": 304,
        "age": 24,
        "email": "noname@gmail.com",
        "department_id": "MECH"
    })
    print("Actual Result: Inserted")
    print("Status: FAIL")
except Exception as e:
    print("Actual Result: Rejected")
    print("Status: PASS")