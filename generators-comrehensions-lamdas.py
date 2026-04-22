# features_demo.py

print("🔹 1. GENERATOR EXAMPLE")

# Generator function
def numbers_generator(n):
    for i in range(1, n + 1):
        yield i  # produces values one by one

gen = numbers_generator(5)

for value in gen:
    print(value)


print("\n🔹 2. COMPREHENSIONS EXAMPLE")

# List Comprehension
list_comp = [x for x in range(10)]
print("List:", list_comp)

# Even numbers using condition
even_comp = [x for x in range(10) if x % 2 == 0]
print("Even List:", even_comp)

# Dictionary Comprehension
dict_comp = {x: x * x for x in range(5)}
print("Dictionary:", dict_comp)

# Set Comprehension
set_comp = {x % 3 for x in range(10)}
print("Set:", set_comp)


print("\n🔹 3. LAMBDA EXPRESSIONS")

# Simple lambda
add = lambda a, b: a + b
print("Addition:", add(5, 3))

# Lambda with map()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)

# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)