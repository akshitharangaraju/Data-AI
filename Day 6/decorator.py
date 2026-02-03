# def my_decorator(func):
#     def wrapper():
#         print("before the function call")
#         func()
#         print("after the function call")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello!")
# say_hello()
# say_hello=my_decorator(say_hello)

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("before thee function call")
#         result=func(*args,**kwargs)
#         print("after the function call")
#         return result
#     return wrapper
# @decorator
# def add(a,b):
#     return a+b
# print(add(3,5)) 

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator
# @repeat(10)
# def greet():
#     print("hi")
# greet()

# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Mathutils.add(3,5))

# obj=Mathutils()
# print(obj.add(4,6))

# class Student:
#     school_name="ABC School"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def change_school_name(cls,new_name):
#         cls.school_name=new_name
# print(Student.school_name)
# Student.change_school_name("XYZ School")
# print(Student.school_name)

# def designation(func):
#     def wrapper():
#         print("designation: lawyer.")
#         func()
#     return wrapper
        
# def salary(func):
#     def wrapper():
#         print("salary : rs500000.")
#         func()
#     return wrapper
# @designation
# @salary
# def emp():
#     print("information")
    
# emp()


