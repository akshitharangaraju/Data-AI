#hello world program
print("hello world!")
#if statement
a=True
if a==True:
    print("akki")
#data types and typecasting
a=10
print(a)
print(type(a))
b=20.5
print(b)
print(type(b))
c= "akki"
print(c)
print(type(c))
d=True
print(d)
print(type(d))
e=[1,2,3,4,5]
print(e)
print(type(e))
f=(1,2,3,4,5)
print(f)
print(type(f))
g={1,2,3,4,5}
print(g)
print(type(g))
h={"name":"akki","age":22}
print(h)
print(type(h))
#typecasting
i=input()
print(i)
print(type(i))
j=int(input())
print(j)
print(type(j))
#functions-factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter a number: "))
result=fact(num)
print(result)
#functions-power
def power(a, b):
    if b == 0:      
        return 1
    else:
        return a * power(a, b - 1)
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(result)
#functions-prime check
def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n=int(input("Enter a number: "))
if prime_check(n):
    print(n, "is a prime.")
else:
    print(n, "is not a prime.")
