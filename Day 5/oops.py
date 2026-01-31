# class Student:
#     def hello(self):
#         print("Hello, I am a student.")
# s1=Student()
# s2=Student()
# s3=Student()
# s1.hello()
# s2.hello()
# s3.hello()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Name:{self.name},Age{self.age}")
# name=input("enter name:")
# age=int(input("enter age:"))
# s1=Student(name,age)
# s1.display()

# class Employee:
#     def __init__(self, emp_id, name, department, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
#         self.salary = salary
#     def display_details(self):
#         print("\n--- Employee Details ---")
#         print("Employee ID :", self.emp_id)
#         print("Name        :", self.name)
#         print("Department  :", self.department)
#         print("Salary      :", self.salary)
# employees = []   
# for i in range(3):
#     print(f"\nEnter details for Employee {i+1}")
#     emp_id = int(input("Enter Employee ID: "))
#     name = input("Enter Employee Name: ")
#     department = input("Enter Department: ")
#     salary = float(input("Enter Salary: "))
#     emp = Employee(emp_id, name, department, salary)
#     employees.append(emp)
# for emp in employees:
#     emp.display_details()

# class Demo:
#     def show(self,*args):
#         if len(args)==1:
#             print("one argument")
#         elif len(args)==2:
#             print("2 arguments")
# obj=Demo()
# obj.show(1)
# obj.show(1,2)

# class Employee: 
#     def display(self,*args):
#         self.id=id
#         self.name=name
#         self.department=department
#         if len(args)==2:
#             print(f"employee ID : {self.id}")
#             print(f"employee Name : {self.name}")
#         elif len(args)==1:
#             print(f"employee department : {self.department}")
# id=input("enter the employee id :")  
# name=input("enter the employee name :")    
# department=input("enter the employee department :")
# s1=Employee()
# s2=Employee()
# s1.display(id,name)
# s2.display(department)

# class Animal:
#     def sound(self):
#         print("some generic sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# class Cat(Animal):
#     def sound(self):
#         print("meow")
# for animal in [Dog(),Cat()]:
#     animal.sound()

# class Display:
#     def show(self,*args):
#         if len(args)==1:
#             if isinstance(args[0],str):
#                 print("name:",args[0])
#             elif isinstance(args[0],int):
#                 print("Age:",args[0])
#             else:
#                 print("unknown type")
#         elif len(args)==2:
#             name,age=args
#             print("name:",name,"age:",age)
#         else:
#             print("no args")
# d=Display()
# d.show("akki")
# d.show("rab",20)
# d.show(30)

# class Pycharm:
#     def execute(self):
#         print("compiling+running")
# class VScode:
#     def execute(self):
#         print("runnning+linting")
# def code(editor):
#     editor.execute()
# code(Pycharm())
# code(VScode())
    
# class Father:
#     def drive(self):
#         print("Father can drive")
# class Son(Father):
#     def play(self):
#         print("son can play")
# s=Son()
# s.drive()
# s.play()

# class Grandfather:
#     def wisdom(self):
#         print("Grandfather shares wisdom")
# class Father(Grandfather):
#     def drive(self):
#         print("Father can drive")
# class Son(Father):
#     def play(self):
#         print("son can play")
# s=Son()
# s.drive()
# s.play()
# s.wisdom()

# class Mother:
#     def cook(self):
#         print("Mother cooks well")
# class Daughter(Mother):
#     def dance(self):
#         print("Daughter can dance")
# class Son(Mother):
#     def play(self):
#         print("son can play")
# s=Son()
# s.play()
# s.cook()
# s1=Daughter()
# s1.cook()
# s1.dance()

# class Father:
#     def drive(self):
#         print("Father drives")
# class Mother:
#     def cook(self):
#         print("Mother cooks")
# class Child(Father,Mother):
#     def play(self):
#         print("child plays")
# c=Child()
# c.drive()
# c.cook()
# c.play()

# class A:
#     def method_a(self):
#         print("A")
# class B(A):
#     def method_b(self):
#         print("B")
# class C(A):
#     def method_c(self):
#         print("C")
# class D(B,C):
#     def method_bc(self):
#         print("D")
# s=D()
# s.method_a()
# s.method_b()
# s.method_c()
# s.method_bc()

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started")
# c=Car()
# c.start_engine()

# class Parent:
#     def __init__(self):   
#         self.public_var = "Public"
#         self._protected_var = "Protected"
#         self.__private_var = "Private"
#     def access_from_same_class(self):
#         print("Inside Parent class:")
#         print("Public     :", self.public_var)
#         print("Protected  :", self._protected_var)
#         print("Private    :", self.__private_var)
# class Child(Parent):
#     def access_from_subclass(self):
#         print("Inside Child class (Subclass):")
#         print("Public     :", self.public_var)        
#         print("Protected  :", self._protected_var)   
#         print("Private    :", self._Parent__private_var)
# c = Child()
# c.access_from_same_class()
# print()
# c.access_from_subclass()
