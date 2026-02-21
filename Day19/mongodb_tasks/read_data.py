from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
students = db["students"]

print("\n--- All Students ---")
for student in students.find():
    print(student)
print("\n--- Students Older Than 20 ---")
for student in students.find({"age": {"$gt": 20}}):
    print(student)
print("\n--- Student with Email neha.reddy@gmail.com ---")
student = students.find_one({"email": "neha.reddy@gmail.com"})
print(student)
print("\n--- Students from CSE Department ---")
for student in students.find({"department_id": "CSE"}):
    print(student)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
courses = db["courses"]

print("\n--- Courses with Credits > 3 ---")
for course in courses.find({"credits": {"$gt": 3}}):
    print(course)