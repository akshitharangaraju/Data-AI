from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select Database
db = client["collegeDB"]

# Select Collection
courses_collection = db["courses"]

# Course documents
courses = [
    {
        "course_id": "CS101",
        "course_name": "Data Structures",
        "credits": 4,
        "instructor_id": "INS01"
    },
    {
        "course_id": "CS102",
        "course_name": "Database Management",
        "credits": 3,
        "instructor_id": "INS02"
    },
    {
        "course_id": "EC201",
        "course_name": "Digital Electronics",
        "credits": 4,
        "instructor_id": "INS03"
    },
    {
        "course_id": "IT301",
        "course_name": "Web Development",
        "credits": 3,
        "instructor_id": "INS04"
    },
    {
        "course_id": "ME101",
        "course_name": "Thermodynamics",
        "credits": 4,
        "instructor_id": "INS05"
    }
]

# Insert documents
result = courses_collection.insert_many(courses)

print("Inserted Course IDs:", result.inserted_ids)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
departments = db["departments"]

data = [
    {"department_id": "CSE", "department_name": "Computer Science"},
    {"department_id": "ECE", "department_name": "Electronics"},
    {"department_id": "IT", "department_name": "Information Technology"},
    {"department_id": "MECH", "department_name": "Mechanical"}
]

departments.insert_many(data)
print("Departments inserted successfully")

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
enrollments = db["enrollments"]

data = [
    {
        "student_id": 101,
        "course_id": "CS101"
    },
    {
        "student_id": 101,
        "course_id": "CS102"
    },
    {
        "student_id": 102,
        "course_id": "EC201"
    },
    {
        "student_id": 103,
        "course_id": "IT301"
    }
]

enrollments.insert_many(data)
print("Enrollments inserted successfully")

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]
instructors = db["instructors"]

data = [
    {"instructor_id": "INS01", "name": "Dr. Rao"},
    {"instructor_id": "INS02", "name": "Dr. Mehta"},
    {"instructor_id": "INS03", "name": "Dr. Sharma"},
    {"instructor_id": "INS04", "name": "Dr. Khan"}
]

instructors.insert_many(data)
print("Instructors inserted successfully")

from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Select Database
db = client["collegeDB"]

# Step 3: Select Collection
students_collection = db["students"]

# Step 4: Student documents
students = [
    {
        "student_id": 101,
        "name": "Aarav Sharma",
        "age": 20,
        "email": "aarav.sharma@gmail.com",
        "department_id": "CSE"
    },
    {
        "student_id": 102,
        "name": "Neha Reddy",
        "age": 21,
        "email": "neha.reddy@gmail.com",
        "department_id": "ECE"
    },
    {
        "student_id": 103,
        "name": "Rahul Verma",
        "age": 19,
        "email": "rahul.verma@gmail.com",
        "department_id": "IT"
    },
    {
        "student_id": 104,
        "name": "Pooja Singh",
        "age": 22,
        "email": "pooja.singh@gmail.com",
        "department_id": "CSE"
    },
    {
        "student_id": 105,
        "name": "Kiran Patel",
        "age": 20,
        "email": "kiran.patel@gmail.com",
        "department_id": "MECH"
    }
]

# Step 5: Insert documents
result = students_collection.insert_many(students)

print("Inserted Student IDs:", result.inserted_ids)