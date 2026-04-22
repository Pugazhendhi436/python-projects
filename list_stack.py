# stack_example.py

# LIFO (Last In, First Out) # 10, 20,30

# Create an empty stack
stack = []

# PUSH operations
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

# PEEK (view top element)
if stack:
    print("Top element:", stack[-1])

# POP operations
popped_item = stack.pop()
print("Popped item:", popped_item)

print("Stack after pop:", stack)

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

# Pop all elements
while stack:
    print("Removing:", stack.pop())

print("Final stack:", stack)