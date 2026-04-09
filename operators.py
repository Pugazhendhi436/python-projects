# =====================================
# Operators in Python - Single File Demo
# =====================================

# 1️⃣ Arithmetic Operators
print("Arithmetic Operators:")
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# -------------------------------------

# 2️⃣ Comparison (Relational) Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# -------------------------------------

# 3️⃣ Assignment Operators
print("\nAssignment Operators:")
x = 5
print("x =", x)

x += 3
print("x += 3:", x)

x -= 2
print("x -= 2:", x)

x *= 2
print("x *= 2:", x)

x /= 2
print("x /= 2:", x)

x //= 2
print("x //= 2:", x)

x %= 2
print("x %= 2:", x)

x **= 3
print("x **= 3:", x)

# -------------------------------------

# 4️⃣ Logical Operators
print("\nLogical Operators:")
p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# -------------------------------------

# 5️⃣ Bitwise Operators
print("\nBitwise Operators:")
m = 5   # 0101
n = 3   # 0011

print("m & n:", m & n)   # AND
print("m | n:", m | n)   # OR
print("m ^ n:", m ^ n)   # XOR
print("~m:", ~m)         # NOT
print("m << 1:", m << 1) # Left shift
print("m >> 1:", m >> 1) # Right shift

# -------------------------------------

# 6️⃣ Membership Operators
print("\nMembership Operators:")
text = "Python"

print("'P' in text:", 'P' in text)
print("'z' not in text:", 'z' not in text)

# -------------------------------------

# 7️⃣ Identity Operators
print("\nIdentity Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)

# -------------------------------------

print("\n--- End of Operators Demo ---")