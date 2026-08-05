#exception handling

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An unexpected error occurred:", str(e))


numbers=[10, 20, 30, 40, 50]
try:
    index = int(input("Enter the index of the number you want to access (0-4): "))
    print("Number at index", index, "is:", numbers[index])    
except IndexError:
    print("Error: Index out of bounds.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

my_dict = {"a": 1, "b": 2, "c": 3}
try:
    key = input("Enter the key you want to access (a, b, c): ")
    print("Value for key", key, "is:", my_dict[key])
except KeyError:
    print("Error: Key not found.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

import math
def sqrt(num):
    try:
        if num < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.hypot(num, 0)
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", str(e))
    else:
        print("Square root of", num, "is:", math.sqrt(num))


def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print("File loaded successfully.")
            return data
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                print("File loaded successfully.")
                return data
        except FileNotFoundError:
            print("Error: File not found.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

#raise an exception
def divide_numbers(num1, num2):
    try:
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", str(e))

#finally block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = divide_numbers(num1, num2)
    print("Result:", result)    
finally:
    print("Execution completed.")