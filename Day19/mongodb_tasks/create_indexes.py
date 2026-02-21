from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

print("\n--- Creating Indexes ---")

# Index on student email
students.create_index("email")
print("Index created on students.email")

# Index on department_id
students.create_index("department_id")
print("Index created on students.department_id")

# Index on course_id
courses.create_index("course_id")
print("Index created on courses.course_id")