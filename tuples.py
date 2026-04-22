# Tuples in Python - Single File Example

# 1. Creating tuples
t1 = (10, 20, 30, 40)
t2 = (1, "Python", 3.5)

print("Tuple t1:", t1)
print("Tuple t2:", t2)

# 2. Accessing elements
print("\nAccessing elements:")
print("First element of t1:", t1[0])
print("Last element of t1:", t1[-1])

# 3. Tuple is immutable
# t1[0] = 100   # ❌ This will cause an error if uncommented

# 4. Tuple operations
t3 = (5, 6, 7)

print("\nTuple concatenation:", t1 + t3)
print("Tuple repetition:", t3 * 2)

# 5. Membership test
print("\nMembership test:")
print(20 in t1)   # True
print(100 in t1)  # False

# 6. Tuple methods
t4 = (1, 2, 2, 3, 2)

print("\nCount of 2 in t4:", t4.count(2))
print("Index of 3 in t4:", t4.index(3))

# 7. Length of tuple
print("\nLength of t1:", len(t1))

# 8. Tuple unpacking
a, b, c, d = t1
print("\nTuple unpacking:")
print(a, b, c, d)

# 9. Real-life example (coordinates)
location = (12.9716, 77.5946)
print("\nCoordinates:")
print("Latitude:", location[0])
print("Longitude:", location[1])