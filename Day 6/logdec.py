# login=True

# def login_info(func):
#     def wrapper():
#         if login:
#             print("Login successful")
#             #print("Salary: Rs 500000")
#             func()
#         else:
#             print("Login failed")
#     return wrapper


# @login_info
# def emp():
#     print("Employee Information")


# emp()

# def login_requiredd(func):
#     def wrapper():
#         user_authenticated = True
#         if user_authenticated:
#             return func()
#         else:
#             print("User not authenticated. Please log in.")
#     return wrapper
# @login_requiredd
# def view_dashboard():
#     print("Welcome to your dashboard!")
# view_dashboard()

# def validate_registration(func):
#     def wrapper(name, email, phone):

#         if name == "":
#             print("Invalid Name")
#             return

#         if "@" not in email:
#             print("Invalid Email")
#             return

#         if len(str(phone)) != 10:
#             print("Invalid Phone Number")
#             return

#         print("Validation Successful")
#         func(name, email, phone)

#     return wrapper


# @validate_registration
# def register_user(name, email, phone):
#     print("Registration Successful!")
#     print("Name:", name)
#     print("Email:", email)
#     print("Phone:", phone)
# register_user("akki","akshitha@gmail.com",2345678901)

