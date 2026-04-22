# list_operations.py

# 🔹 Creating a List
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

print("Original fruits:", fruits)

# 🔹 Accessing Elements
print("\nAccessing:")
print("First:", fruits[0])
print("Last:", fruits[-1])
print("Slice:", fruits[0:2])

# 🔹 Modifying Elements
fruits[1] = "orange"
print("\nAfter modifying:", fruits)

# 🔹 Adding Elements
fruits.append("grape")
fruits.insert(1, "mango")
fruits.extend(["kiwi", "pear"])
print("\nAfter adding:", fruits)

# 🔹 Removing Elements
fruits.remove("apple")     # remove by value
fruits.pop()               # remove last
fruits.pop(1)              # remove by index
print("\nAfter removing:", fruits)

# 🔹 Looping
print("\nLooping:")
for fruit in fruits:
    print(fruit)

# 🔹 Enumerate
print("\nWith index:")
for i, fruit in enumerate(fruits):
    print(i, fruit)

# 🔹 List Comprehension
squares = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
print("\nSquares:", squares)
print("Even numbers:", even_numbers)

# 🔹 Sorting
nums = [3, 1, 4, 2]
nums.sort()
print("\nSorted:", nums)

nums.sort(reverse=True)
print("Descending:", nums)

# 🔹 Reverse
nums.reverse()
print("Reversed:", nums)

# 🔹 Other Methods
print("\nCount of 2:", nums.count(2))
print("Index of 4:", nums.index(4))

# 🔹 Copying Lists
a = [1, 2, 3]
b = a              # reference
c = a.copy()       # actual copy

a.append(4)
print("\nOriginal:", a)
print("Reference copy:", b)
print("Actual copy:", c)

# 🔹 Nested List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix element [1][2]:", matrix[1][2])

# 🔹 Built-in Functions
print("\nMax:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# 🔹 Check existence
if 3 in numbers:
    print("3 exists in numbers")

# 🔹 Real-world Example (Employee Salary)
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Jane", "salary": 60000}
]

for emp in employees:
    emp["salary"] *= 1.1

print("\nUpdated Employees:")
for emp in employees:
    print(emp)

# 🔹 Clear list
fruits.clear()
print("\nAfter clearing fruits:", fruits)