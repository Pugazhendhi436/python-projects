#counter

from collections import Counter

text = "hello world hello"
words = text.split()
word_count = Counter(words)
print(word_count)

items = ["apple", "banana", "apple", "cherry", "banana", "apple",
         "date", "cherry", "banana", "apple"]

item_count = Counter(items)

print("Top 3 most common elements:")
for item, count in item_count.most_common(3):
    print(f"  {item}: {count}")

sentence = "the cat sat on the mat the cat sat"
words = sentence.lower().split()

word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")

#defaultdict

from collections import defaultdict

group=defaultdict(list)
for word in items:
    key = word[0].lower()
    group[key].append(word)

for key, words in group.items():
    print(f"{key}: {words}")

#orderedDict

from collections import OrderedDict
pairs = [("apple", 3), ("banana", 1), ("cherry", 4), ("date", 2)]
ordered_dict = OrderedDict(pairs)


for key, value in ordered_dict.items():
    print(f"{key}: {value}")

#reverse orderedDict

reversed_dict = OrderedDict(reversed(list(ordered_dict.items())))
for key, value in reversed_dict.items():
    print(f"{key}: {value}")

#dequeue

from collections import deque

dq = deque([2, 3, 4])
print(f"Initial              : {list(dq)}")

dq.append(5)
print(f"After append(5)      : {list(dq)}")

dq.appendleft(1)
print(f"After appendleft(1)  : {list(dq)}")

right = dq.pop()
print(f"After pop()  -> {right}   : {list(dq)}")

left = dq.popleft()
print(f"After popleft() -> {left} : {list(dq)}")

dq.extend([6, 7])
print(f"After extend([6,7])  : {list(dq)}")

dq.extendleft([0, -1])
print(f"After extendleft([0,-1]): {list(dq)}")

#named tuple

from collections import namedtuple
import math

Point = namedtuple("Point", ["x", "y"])

p1 = Point(3, 7)
p2 = Point(10, 4)

# Attribute access
print(f"p1 - x: {p1.x}, y: {p1.y}")
print(f"p2 - x: {p2.x}, y: {p2.y}")

# Index access (namedtuples are still tuples)
print(f"p1 via index  - [0]: {p1[0]}, [1]: {p1[1]}")

# Unpacking (works like a regular tuple)
x, y = p2
print(f"p2 unpacked   - x={x}, y={y}")

# Distance calculation
distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
print(f"Distance p1 to p2: {distance:.2f}")

Employee = namedtuple("Employee", ["name", "department", "salary"])

employees = [
    Employee("Alice",   "Engineering", 95000),
    Employee("Bob",     "Marketing",   72000),
    Employee("Charlie", "Engineering", 88000),
    Employee("Diana",   "HR",          65000),
    Employee("Eve",     "Engineering", 102000),
]

target_dept = "Engineering"
print(f"Employees in {target_dept}:")

dept_employees = [e for e in employees if e.department == target_dept]

for emp in dept_employees:
    print(f"  {emp.name:10s} | Salary: £{emp.salary:,}")

print(f"\nTotal in {target_dept}: {len(dept_employees)}")
avg = sum(e.salary for e in dept_employees) / len(dept_employees)
print(f"Average salary     : £{avg:,.0f}")

