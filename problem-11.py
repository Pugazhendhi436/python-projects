#lambda functions
square = lambda x: x ** 2
print(square(5))  # Output: 25

#lambda with sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(key=lambda x: -x)  # Sort in descending order
print(numbers)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

numbers.sort(key=lambda x: x) #sort in ascending order
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

#lambda with map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 1, 4, 9, 16, 25, 36, 81]

#lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

#lambda with reduce
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 31

#conditional lambda
max_value = lambda x, y: x if x > y else y
print(max_value(10, 5))  # Output: 10

#lambda with partial
from functools import partial
double = partial(lambda x: x * 2)
print(double(5))  # Output: 10

