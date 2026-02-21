from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]

# Test query: find student by email
query = {"email": "neha.reddy21@gmail.com"}

print("\n--- Performance Test ---")

start_time = time.time()
result = students.find_one(query)
end_time = time.time()

print("Query Result:", result)
print("Time taken:", end_time - start_time, "seconds")