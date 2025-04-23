# Problem:- Write a python program to print the contents of a directory using the os module.Search online for the function which does that


import os

# Specify the directory you want to list
directory_path = '/'

#List all files and directories in the specified path using os module
contents = os.listdir(directory_path)

#Print each file and directory name
for item in contents:
     print(item)