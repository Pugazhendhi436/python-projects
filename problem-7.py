name = input("Enter your name: ")

with open("user.txt", "a") as f:
    f.write(name)

print("Name written to user.txt")

with open("user.txt", "r") as f:
    content = f.read()

print(content)

with open("user.txt", "r") as f:
    for line in f:
        print(line, end="")



#check if file is empty
with open("user.txt", "r") as f:
    content = f.read()
    if not content:
        print("File is empty.")
    else:
        print("File is not empty.")

import os

if os.path.exists("data.txt"):
    print("File exists.")
else:
    print("File does not exist.")

try:
    with open("missing.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")

#find number of lines in a file
with open("user.txt", "r") as f:
    lines = f.readlines()
    num_lines = len(lines)
    print("Number of lines in the file:", num_lines)




with open("user.txt", "w") as f:
    pass

print("File content cleared.")
text_save="Python is great.I love Python.Python makes file handling easy."
with open("user.txt", "r+") as f:
    f.write(text_save)
    f.seek(0)
    content = f.read()
    print("File content after writing:", content)
    
#occurences of a word
word_to_find = "Python"

with open("user.txt", "r") as f:
    content = f.read()

count = content.count(word_to_find)
print(f"Occurrences of '{word_to_find}':", count)

#find file size

import os

filename = "user.txt"
size_bytes = os.path.getsize(filename)
size_kb = size_bytes / 1024

print(f"File size: {size_kb} KB")

#Rename a file
import os

old_name = "user.txt"
new_name = "info.txt"
try:
    os.rename(old_name, new_name)
    print("File renamed successfully.")
except FileNotFoundError:
    print(f"Error: '{old_name}' not found.")

