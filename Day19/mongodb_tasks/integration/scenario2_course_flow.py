from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

instructors = db["instructors"]
courses = db["courses"]
enrollments = db["enrollments"]

print("\n===== SCENARIO 2: COURSE FLOW =====")

# 1️⃣ Create instructor
instructors.insert_one({
    "instructor_id": "INS99",
    "name": "Integration Instructor"
})
print("Instructor created")

# 2️⃣ Create course
courses.insert_one({
    "course_id": "CS999",
    "course_name": "Integration Testing",
    "credits": 3,
    "instructor_id": "INS99"
})
print("Course created")

# 3️⃣ Assign instructor (already done via course creation)
print("Instructor assigned to course")

# 4️⃣ Enroll students
enrollments.insert_many([
    {"student_id": 101, "course_id": "CS999"},
    {"student_id": 102, "course_id": "CS999"}
])
print("Students enrolled in course")