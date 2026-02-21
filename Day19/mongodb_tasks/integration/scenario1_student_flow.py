from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
enrollments = db["enrollments"]

print("\n===== SCENARIO 1: STUDENT FLOW =====")

# 1️⃣ Register student
student = {
    "student_id": 401,
    "name": "Integration Student",
    "age": 21,
    "email": "integration@student.com",
    "department_id": "CSE"
}
students.insert_one(student)
print("Student registered")

# 2️⃣ Enroll in course
enrollments.insert_one({
    "student_id": 401,
    "course_id": "CS101"
})
print("Student enrolled in course CS101")

# 3️⃣ Update profile
students.update_one(
    {"student_id": 401},
    {"$set": {"email": "updated@student.com"}}
)
print("Student profile updated")

# 4️⃣ Drop course
enrollments.delete_one({
    "student_id": 401,
    "course_id": "CS101"
})
print("Student dropped course")