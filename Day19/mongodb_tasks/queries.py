from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

# 1️⃣ Find students aged between 18 and 25
print("\n--- Students aged between 18 and 25 ---")
for student in students.find({
    "$and": [
        {"age": {"$gt": 18}},
        {"age": {"$lt": 25}}
    ]
}):
    print(student)

# 2️⃣ Find courses with credits 2, 3, or 4
print("\n--- Courses with credits 2, 3, or 4 ---")
for course in courses.find({
    "credits": {"$in": [2, 3, 4]}
}):
    print(course)

# 3️⃣ Find students NOT in a specific department
print("\n--- Students not in CSE Department ---")
for student in students.find({
    "department_id": {"$ne": "CSE"}
}):
    print(student)


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

# 1️⃣ Show only student name and email
print("\n--- Student Name and Email Only ---")
for student in students.find(
    {},
    {"name": 1, "email": 1, "_id": 0}
):
    print(student)

# 2️⃣ Hide student_id field
print("\n--- Students without student_id ---")
for student in students.find(
    {},
    {"student_id": 0}
):
    print(student)

# 3️⃣ Show only course name
print("\n--- Course Name Only ---")
for course in courses.find(
    {},
    {"course_name": 1, "_id": 0}
):
    print(course)