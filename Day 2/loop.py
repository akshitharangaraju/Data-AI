#rectangle pattern
print("rectangular pattern")
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#z pattern
print("z pattern")
n=int(input("enter size:" ))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#reverse z pattern
print("reverse z pattern")
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#right angled triangle
print("right angled triangle")
n = int(input("Enter size: "))
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#inverted right angled triangle
print("inverted right angled triangle")
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

#triangular number pyramid
print("triangular number pyramid")
n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(i, end=" ")
    print()

list
final=[]
while(True):
    user=input("enter item(enter done at the end):")
    if(user=="done"):
        break
    final.append(user)
print(final)


