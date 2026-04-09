# ==========================================
# if, elif, else in Python - Single File Demo
# ==========================================

# 1️⃣ Basic if
print("Basic if:")
age = 18

if age >= 18:
    print("You are eligible to vote")

# -------------------------------------

# 2️⃣ if...else
print("\nif...else:")
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# -------------------------------------

# 3️⃣ if...elif...else
print("\nif...elif...else:")
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# -------------------------------------

# 4️⃣ Multiple Conditions (and, or)
print("\nMultiple Conditions:")
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")

# -------------------------------------

# 5️⃣ Nested if
print("\nNested if:")
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative number")

# -------------------------------------

# 6️⃣ Short-hand (Ternary Operator)
print("\nTernary Operator:")

age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# -------------------------------------

# 7️⃣ Real-time Example (User Input)
print("\nUser Input Example:")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# -------------------------------------

print("\n--- End of Conditional Statements Demo ---")