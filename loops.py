# ==========================================
# Loops in Python 
# ==========================================

# 1️⃣ FOR LOOP
print("FOR LOOP:")

for i in range(5):
    print(i)

# Loop through a list
fruits = ["apple", "banana", "mango"]
print("\nLoop through list:")
for fruit in fruits:
    print(fruit)

# -------------------------------------

# 2️⃣ WHILE LOOP
print("\nWHILE LOOP:")

i = 0
while i < 5:
    print(i)
    i += 1

# -------------------------------------

# 3️⃣ BREAK (Stops loop)
print("\nBREAK Example:")

for i in range(10):
    if i == 5:
        break
    print(i)

# -------------------------------------

# 4️⃣ CONTINUE (Skip iteration)
print("\nCONTINUE Example:")

for i in range(5):
    if i == 2:
        continue
    print(i)

# -------------------------------------

# 5️⃣ PASS (Do nothing)
print("\nPASS Example:")

for i in range(5):
    if i == 3:
        pass  # placeholder, does nothing
    print(i)

# -------------------------------------

# 6️⃣ WHILE with BREAK (do-while style)
print("\nWHILE with BREAK (do-while simulation):")

i = 0
while True:
    print(i)
    i += 1

    if i == 5:
        break

# -------------------------------------

# 7️⃣ WHILE with CONTINUE
print("\nWHILE with CONTINUE:")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# -------------------------------------

print("\n--- End of Loops Demo ---")