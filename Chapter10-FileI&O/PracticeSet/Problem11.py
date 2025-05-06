#Write a program to rename a file to "renamed_by_python.txt"



with open("name.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

#Deleting the name.txt file with the help of os modules
import os

file_path = "name.txt"  

# Check if file exists, then delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")

