from pymongo import MongoClient
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
enrollments = db["enrollments"]
courses = db["courses"]

print("\n===== TRANSACTION TESTING =====")

# ---------- SUCCESSFUL TRANSACTION ----------
print("\n--- Successful Transaction ---")

with client.start_session() as session:
    try:
        with session.start_transaction():

            students.insert_one(
                {
                    "student_id": 501,
                    "name": "Transaction Student",
                    "age": 23,
                    "email": "transaction@student.com",
                    "department_id": "CSE"
                },
                session=session
            )

            enrollments.insert_one(
                {"student_id": 501, "course_id": "CS101"},
                session=session
            )

            courses.update_one(
                {"course_id": "CS101"},
                {"$inc": {"enrollment_count": 1}},
                session=session
            )

        print("Transaction committed successfully")

    except PyMongoError as e:
        print("Transaction failed:", e)


# ---------- FAILED TRANSACTION (ROLLBACK) ----------
print("\n--- Failed Transaction (Rollback) ---")

with client.start_session() as session:
    try:
        with session.start_transaction():

            students.insert_one(
                {
                    "student_id": 502,
                    "name": "Rollback Student",
                    "age": 22,
                    "email": "rollback@student.com",
                    "department_id": "CSE"
                },
                session=session
            )

            # ❌ Force error (invalid course_id)
            enrollments.insert_one(
                {"student_id": 502, "course_id": None},
                session=session
            )

            courses.update_one(
                {"course_id": "INVALID"},
                {"$inc": {"enrollment_count": 1}},
                session=session
            )

        print("Transaction committed (should not happen)")

    except PyMongoError as e:
        print("Transaction failed, rolled back:", e)