from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

print("\n--- Creating Student Validation Rules ---")

db.command({
    "collMod": "students",
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "email", "age", "department_id"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "Name must be a string"
                },
                "email": {
                    "bsonType": "string",
                    "pattern": "^.+@.+\\..+$",
                    "description": "Email must be valid"
                },
                "age": {
                    "bsonType": "int",
                    "minimum": 16,
                    "maximum": 60,
                    "description": "Age must be between 16 and 60"
                },
                "department_id": {
                    "bsonType": "string"
                }
            }
        }
    },
    "validationLevel": "strict",
    "validationAction": "error"
})

print("Student validation rules applied successfully")