from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
courses = db["courses"]

print("\n--- Increase Course Credits by 1 ---")

result = courses.update_many(
    {},
    {"$inc": {"credits": 1}}
)

print("Courses updated:", result.modified_count)
print("\n--- Change Instructor for Course CS101 ---")

result = courses.update_one(
    {"course_id": "CS101"},
    {"$set": {"instructor_id": "INS10"}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
students = db["students"]

print("\n--- Update Student Email ---")

result = students.update_one(
    {"student_id": 102},
    {"$set": {"email": "neha.reddy21@gmail.com"}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)
print("\n--- Update Department Name ---")

result = students.update_many(
    {"department_id": "IT"},
    {"$set": {"department_id": "INFORMATION_TECH"}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)
