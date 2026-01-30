file=open("notes.txt","w")
file.write("Hello, welcome to file handling in Python!\n")
file.write("This is your first file operation.\n")
file.close()

file=open("notes.txt","r")
content=file.read()
print("File Content:")
print(content)
file.close()

file=open("notes.txt","a")
file.write("Appending a new line to the file.\n")
file=open("notes.txt","r")
content=file.read()
print("File Content:")
print(content)
file.close()

with open("notes.txt","r") as file:
    content=file.read()
    print("File Content:")
    print(content)

feedback=input("Please provide your feedback for the ride:")
with open("feedback.txt","a",encoding="utf-8") as file:
    file.write(feedback + "\n")
print("Thank you for your feedback!")

with open("data.txt","r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())

with open("data.txt","r") as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line.strip())

with open("data.txt","r") as file:
    for line in file:
        print(line.strip())
        