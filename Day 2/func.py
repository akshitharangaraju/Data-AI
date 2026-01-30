def greet(name):
    print(f"welcome to {name}")
greet("uber")

def add(a,b):
    return a+b
res=add(5,10)
print(res)

def add_all(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add_all(1,2,3,4,5)) 
# multiple unnamed value

def print_data(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_data(name="akshi",age=20)
# args takes as tuples and kwargs takes as dictionary

name = input("Enter name: ").strip()
age = int(input("Enter age: "))
city = input("Enter city: ")
phone = input("Enter phone number: ")   
gender = input("Enter gender: ")
if len(phone) != 10 or not phone.isdigit():
    print("Invalid phone number")
else:
    lst = []
    def user(**kwargs):
        return kwargs   
    lst.append(user(name=name,age=age,city=city,mobile_number=phone,gender=gender))
    print(lst)

def greet(name="akki"):
    print(f"welcome to {name}")
greet()
greet("uber")

name = input("Enter name: ").strip()
place = input("Enter the place visited: ").strip()
res=input("Enter restaurant name: ").strip( )
phone=input("Enter phone number: ")
masked=phone[:2] + "******" + phone[-2:]
num = int(input("Enter the number of bills you have: "))
bills = []
i = 1
while i <= num:
    bill = float(input("Enter the bill amount: "))
    bills.append(bill)
    i += 1
def total_bill(**kwargs):
    sum=0
    for amount in kwargs['bills']:
        sum+=amount
    return sum
print("-----BILL SUMMARY-----")
print(f" Customer Named {name} visited {res} restaurant located in {place}. Customer's phone number is {masked}. The total bill amount is {total_bill(bills=bills)}.")

