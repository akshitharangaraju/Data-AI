import sys
var=sys.argv[1]
bar=sys.argv[2]
print(var,bar)

import sys
print("program name:",sys.argv[0])
for i in range(1,len(sys.argv)):
    print(f"argument {i} :{sys.argv[i]}")

import sys
n=len(sys.argv)
if n>=2:
    print("program name:",sys.argv[0])
    for i in range(1,len(sys.argv)):
        print(f"argument {i} :{sys.argv[i]}")
else:
    print("please provide more than 2 arguments")

