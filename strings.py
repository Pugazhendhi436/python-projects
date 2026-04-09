# =====================================
# Strings in Python - Single File Demo
# =====================================

# 1️⃣ Creating Strings
s1 = 'Hello'
s2 = "World"
s3 = """This is
a multi-line string"""

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# -------------------------------------

# 2️⃣ Indexing
text = "Python"

print("\nIndexing:")
print(text[0])  # P
print(text[1])  # y

# -------------------------------------

# 3️⃣ Negative Indexing
print("\nNegative Indexing:")
print(text[-1])  # n
print(text[-2])  # o

# -------------------------------------

# 4️⃣ Slicing
print("\nSlicing:")
print(text[0:3])  # Pyt
print(text[2:])   # thon
print(text[:4])   # Pyth

# -------------------------------------

# 5️⃣ String Immutability
print("\nImmutability:")
# text[0] = "J"  # ❌ This will give error
new_text = "J" + text[1:]
print(new_text)

# -------------------------------------

# 6️⃣ Concatenation
print("\nConcatenation:")
a = "Hello"
b = "World"
print(a + " " + b)

# -------------------------------------

# 7️⃣ Repetition
print("\nRepetition:")
print("Hi " * 3)

# -------------------------------------

# 8️⃣ String Methods
print("\nString Methods:")
sample = "python programming"

print(sample.upper())
print(sample.lower())
print(sample.capitalize())
print(sample.title())

# -------------------------------------

# 9️⃣ Searching
print("\nSearching:")
print(sample.find("programming"))
print("python" in sample)

# -------------------------------------

# 🔟 Replace
print("\nReplace:")
print(sample.replace("python", "Java"))

# -------------------------------------

# 1️⃣1️⃣ Splitting
print("\nSplitting:")
data = "apple,banana,mango"
print(data.split(","))

# -------------------------------------

# 1️⃣2️⃣ Joining
print("\nJoining:")
words = ["Python", "is", "fun"]
print(" ".join(words))

# -------------------------------------

# 1️⃣3️⃣ String Formatting
print("\nFormatting:")
name = "Alice"
age = 25

# f-string
print(f"My name is {name} and I am {age}")

# -------------------------------------

# 1️⃣4️⃣ Escape Characters
print("\nEscape Characters:")
print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Hi\"")

# -------------------------------------

# 1️⃣5️⃣ Length of String
print("\nLength:")
print(len(text))

# -------------------------------------

# 1️⃣6️⃣ Looping through String
print("\nLooping:")
for ch in text:
    print(ch)

# -------------------------------------

print("\n--- End of String Demo ---")