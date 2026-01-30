name=input("enter the name:")
age=input("enter the age:")
email=input("enter the email:")
pwd=input("enter the password(6 characters only)")
def form1(name,age):
    if name.isalpha():
        if age.isdigit():
            return True
        else:
            return False
    else:
        return False
def form(email,pwd):
    if "@" in email and "." in email:
        if len(pwd)==6:
            return "valid form. It can be submitted"
        else:
            return "password must be exactly 6 characters"
    else:
        return "invalid email"
if form1(name, age):
    print(form(email, pwd))
else:
    print("Name and age must be in correct format")
