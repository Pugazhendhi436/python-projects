# ==========================================
# Data Types and Variables in Python - Demo
# ==========================================

# 1️⃣ Variables (No need to declare type)
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Variables:")
print(name, age, height, is_student)

# -------------------------------------

# 2️⃣ Checking Data Types
print("\nData Types using type():")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# -------------------------------------

# 3️⃣ Basic Data Types

# Integer
a = 10
print("\nInteger:", a, type(a))

# Float
b = 3.14
print("Float:", b, type(b))

# Complex
c = 2 + 3j
print("Complex:", c, type(c))

# -------------------------------------

# 4️⃣ String
text = "Python"
print("\nString:", text, type(text))

# -------------------------------------

# 5️⃣ Boolean
flag = True
print("\nBoolean:", flag, type(flag))

# -------------------------------------

# 6️⃣ List (Mutable)
my_list = [1, 2, 3, "apple"]
print("\nList:", my_list, type(my_list))

# -------------------------------------

# 7️⃣ Tuple (Immutable)
my_tuple = (1, 2, 3)
print("\nTuple:", my_tuple, type(my_tuple))

# -------------------------------------

# 8️⃣ Set (Unique values)
my_set = {1, 2, 3, 3}
print("\nSet:", my_set, type(my_set))

# -------------------------------------

# 9️⃣ Dictionary (Key-Value pairs)
my_dict = {
    "name": "John",
    "age": 30
}
print("\nDictionary:", my_dict, type(my_dict))

# -------------------------------------

# 🔟 Type Conversion (Casting)
print("\nType Conversion:")

x = 10
y = float(x) #10.0
z = str(x) #"10"

print("int to float:", y)
print("int to string:", z)

# -------------------------------------

# 1️⃣1️⃣ Multiple Assignment
print("\nMultiple Assignment:")

a, b, c = 1, 2, 3
print(a, b, c)

# Same value to multiple variables
x = y = z = 100
print(x, y, z)

# -------------------------------------

# 1️⃣2️⃣ Dynamic Typing
print("\nDynamic Typing:")

var = 10
print(var, type(var))

var = "Now I am a string"
print(var, type(var))

# -------------------------------------

# 1️⃣3️⃣ Constants (by convention)
print("\nConstants (Convention):")

PI = 3.14
print("PI:", PI)

# -------------------------------------

print("\n--- End of Data Types & Variables Demo ---")