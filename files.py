file = open("example.txt", "r")  # "r" means read mode
content = file.read()
print(content)
file.close()

file = open("example.txt", "r+")  # "r+" means read and write mode
content = file.read()   
print(content)    
for line in file:
   print(line)
file.close()

file = open("example.txt", "w")  # "w" means write mode will overwrite the file
file.write("Hello, world!")
file.close()

file = open("example.txt", "a") # "a" means append mode will add to the end of the file
file.write("\nNew line added")
file.close()
# Using 'with' statement to handle files (automatically closes the file)
with open("example.txt", "r") as file:
   content = file.read()
   print(content)
with open("example.txt", "w") as file:
   file.write("Hello again!")