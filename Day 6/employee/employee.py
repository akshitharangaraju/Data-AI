class Employee:
    def __init__(self, emp_id, name, department, salary, phone, email, location, doj):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.phone = phone
        self.email = email
        self.location = location
        self.doj = doj

    def display(self):
        print("\n----- Employee Details -----")
        print("Employee ID     :", self.emp_id)
        print("Name            :", self.name)
        print("Department      :", self.department)
        print("Salary          :", self.salary)
        print("Phone           :", self.phone)
        print("Email           :", self.email)
        print("Location        :", self.location)
        print("Date of Joining :", self.doj)


# Employee objects
emp1 = Employee(101, "Akshitha", "HR", 45000,
                "9876543210", "akshitha@gmail.com", "Hyderabad", "12-06-2022")

emp2 = Employee(102, "Ravi", "IT", 60000,
                "9123456780", "ravi@gmail.com", "Bangalore", "03-01-2021")

emp3 = Employee(103, "Sita", "Finance", 52000,
                "9988776655", "sita@gmail.com", "Chennai", "18-09-2023")

employee_list = [emp1, emp2, emp3]
