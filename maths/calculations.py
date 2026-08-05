def squareroot(x):
    """Returns the square root of a number x."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5

def fraction(a,b):
    """Returns the fraction of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def percentage(part, whole):
    """Returns the percentage of part with respect to whole."""
    if whole == 0:
        raise ValueError("Whole cannot be zero.")
    return (part / whole) * 100

def factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    