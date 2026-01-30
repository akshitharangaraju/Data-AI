#functions-calculator
a=int(input("enter the first number:"))
b=int(input("enter second number:"))
op=input("enter an operator(+,-,*,/):")
def calculator(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b!=0:
            return a/b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"
result=calculator(a,b,op)
print("The result is:",result)
