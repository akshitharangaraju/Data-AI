import mthsop
x=float(input("enter first number:"))
y=float(input("enter second number:"))
op=input("select operation:+,-,*,/,**, %")
if op=='+':
    sum=mthsop.add(x,y)
    print("sum of numbers:",sum)
elif op=='-':
    diff=mthsop.subtract(x,y)
    print("difference of numbers:",diff)
elif op=='*':
    product=mthsop.multiply(x,y)
    print("product of numbers:",product)
elif op=='/':
    quotient=mthsop.divide(x,y)
    print("quotient of numbers:",quotient)
elif op=='**':
    power_result=mthsop.power(x,y)
    print(f"{x} raised to the power {y}:",power_result)
elif op=='%':
    mod_result=mthsop.modulus(x,y)
    print("modulus of numbers:",mod_result)
else:
    print("invalid operation")







