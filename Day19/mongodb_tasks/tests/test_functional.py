from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
students = db["students"]

print("\n===== FUNCTIONAL TESTING =====")

# TC1: Insert valid student
print("\nTC1: Insert valid student")
student_tc1 = {
    "student_id": 201,
    "name": "Test User",
    "age": 22,
    "email": "testuser@gmail.com",
    "department_id": "CSE"
}

try:
    students.insert_one(student_tc1)
    print("Actual Result: Student inserted")
    print("Status: PASS")
except Exception as e:
    print("Actual Result:", e)
    print("Status: FAIL")


# TC2: Insert student with missing fields
print("\nTC2: Insert student with missing fields")
student_tc2 = {
    "student_id": 202,
    "age": 20
}

try:
    students.insert_one(student_tc2)
    print("Actual Result: Inserted (No validation)")
    print("Status: FAIL")
except Exception as e:
    print("Actual Result:", e)
    print("Status: PASS")


# TC3: Insert duplicate email
print("\nTC3: Insert duplicate email")

try:
    students.insert_one({
        "student_id": 203,
        "name": "Duplicate Email",
        "age": 21,
        "email": "testuser@gmail.com",  # duplicate
        "department_id": "ECE"
    })
    print("Actual Result: Inserted duplicate")
    print("Status: FAIL")
except Exception as e:
    print("Actual Result: Duplicate prevented")
    print("Status: PASS")


# TC4: Update non-existing student
print("\nTC4: Update non-existing student")

result = students.update_one(
    {"student_id": 999},
    {"$set": {"email": "noone@gmail.com"}}
)

print("Matched Count:", result.matched_count)
if result.matched_count == 0:
    print("Status: PASS")
else:
    print("Status: FAIL")


# TC5: Delete existing student
print("\nTC5: Delete existing student")

result = students.delete_one({"student_id": 201})

print("Deleted Count:", result.deleted_count)
if result.deleted_count == 1:
    print("Status: PASS")
else:
    print("Status: FAIL")