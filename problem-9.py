#functions,packages,modules
#user defined functions
from maths.calculations import squareroot,fraction,percentage,factorial

result1 = squareroot(256)
result2 = fraction(10, 2)
result3 = percentage(50, 200)
result4 = factorial(5)

print("Square root of 256:", result1)
print("Fraction of 10 divided by 2:", result2)
print("Percentage of 50 with respect to 200:", result3)
print("Factorial of 5:", result4)

from maths import calculations as calc

result5 = calc.squareroot(144)
result6 = calc.fraction(20, 4)
result7 = calc.percentage(30, 150)
result8 = calc.factorial(6)

print("Square root of 144:", result5)
print("Fraction of 20 divided by 4:", result6)
print("Percentage of 30 with respect to 150:", result7)
print("Factorial of 6:", result8)

import maths.calculations as calc_module

result9 = calc_module.squareroot(100)
result10 = calc_module.fraction(30, 6)
result11 = calc_module.percentage(40, 200)
result12 = calc_module.factorial(7)

print("Square root of 100:", result9)
print("Fraction of 30 divided by 6:", result10)
print("Percentage of 40 with respect to 200:", result11)
print("Factorial of 7:", result12)

#built-in functions
#abs() function
print("Absolute value of -5:", abs(-5))

import math
print("Square root of 16:", math.sqrt(16))

import random
print("Random number between 1 and 10:", random.randint(1, 10))