from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
courses = db["courses"]

print("\n--- Delete Courses with 0 Credits ---")

result = courses.delete_many({"credits": 0})

print("Courses deleted:", result.deleted_count)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
enrollments = db["enrollments"]

print("\n--- Delete Enrollments for Student 101 ---")

result = enrollments.delete_many({"student_id": 101})

print("Enrollments deleted:", result.deleted_count)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
students = db["students"]

print("\n--- Delete Student ---")

result = students.delete_one({"student_id": 105})

print("Students deleted:", result.deleted_count)