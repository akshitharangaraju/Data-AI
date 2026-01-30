# a=10
# b=20
# result=a/b
# print("the result is:")
# print(result)

try:
    a=int(input("enter value of a "))
    b=int(input("enter value of b "))
    res=a/b
    print(res)
#except ZeroDivisionError:
 #   print("Error: Division by zero is not allowed")
except Exception as e:
    print("Unexpected error:", e)  
finally:
    print("Program ended")
    