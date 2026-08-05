#iterators and generators

#square generator
def square_gen(n):
    for i in range(n):
        yield i**2

for square in square_gen(5):
    print(square, end=" ")

#reverse string iterator
class ReverseString:
    def __init__(self, string):
        self.string = string
        self.index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.string[self.index]

for char in ReverseString("Hello"):
    print(char, end=" ")

#fibonacci series generator
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for fib in fibonacci_gen(10):
    print(fib, end=" ")

#manual iterator

data = [1, 2, 3, 4, 5]
manual_iter = iter(data)
while True:
    try:
        item = next(manual_iter)
        print(item, end=" ")
    except StopIteration:
        break