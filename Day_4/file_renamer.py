import os

old_file = r"C:\Users\akshi\OneDrive\Desktop\primary track\Day_4\renamed_file.txt"
new_file = os.path.join(os.path.dirname(old_file), "file_rename.txt")
os.rename(old_file, new_file)

print("File renamed successfully!")