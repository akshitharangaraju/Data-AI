from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]
enrollments = db["enrollments"]
departments = db["departments"]

# 1️⃣ Count number of students per department
print("\n--- Count of Students per Department ---")
pipeline_students_per_dept = [
    {
        "$group": {
            "_id": "$department_id",
            "student_count": {"$sum": 1}
        }
    }
]

for result in students.aggregate(pipeline_students_per_dept):
    print(result)

# 2️⃣ Count enrollments per course
print("\n--- Enrollments per Course ---")
pipeline_enrollments_per_course = [
    {
        "$group": {
            "_id": "$course_id",
            "enrollment_count": {"$sum": 1}
        }
    }
]

for result in enrollments.aggregate(pipeline_enrollments_per_course):
    print(result)

# 3️⃣ Find average age of students
print("\n--- Average Age of Students ---")
pipeline_avg_age = [
    {
        "$group": {
            "_id": None,
            "average_age": {"$avg": "$age"}
        }
    }
]

for result in students.aggregate(pipeline_avg_age):
    print(result)

# 4️⃣ Find course with maximum enrollments
print("\n--- Course with Maximum Enrollments ---")
pipeline_max_enrollment_course = [
    {
        "$group": {
            "_id": "$course_id",
            "total_enrollments": {"$sum": 1}
        }
    },
    {
        "$sort": {"total_enrollments": -1}
    },
    {
        "$limit": 1
    }
]

for result in enrollments.aggregate(pipeline_max_enrollment_course):
    print(result)

# 5️⃣ Use $lookup to show course name with enrollments
print("\n--- Course Names with Enrollment Count ---")
pipeline_lookup = [
    {
        "$group": {
            "_id": "$course_id",
            "enrollment_count": {"$sum": 1}
        }
    },
    {
        "$lookup": {
            "from": "courses",
            "localField": "_id",
            "foreignField": "course_id",
            "as": "course_details"
        }
    },
    {
        "$project": {
            "_id": 0,
            "course_id": "$_id",
            "enrollment_count": 1,
            "course_details.course_name": 1
        }
    }
]

for result in enrollments.aggregate(pipeline_lookup):
    print(result)