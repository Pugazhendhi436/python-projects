try:
   a = 10
   b = 0
   print(a / b)
except ZeroDivisionError:
   print("Cannot divide by zero")

try:
   num = int(input("Enter a number: "))
   result = 10 / num
except ZeroDivisionError:
   print("Cannot divide by zero")
except ValueError:
   print("Enter a valid number")
else:
   print("Result:", result)
finally:
   print("Program ended")

#arguments in except block can be used to get more information about the error
try:
   raise Exception("File not found", 404)
except Exception as e:
   print("Message:", e.args[0])
   print("Code:", e.args[1])

# Custom exception
class MyError(Exception):
   pass

try:
   raise MyError("Something went wrong")
except MyError as e:
   print(e)
#raising an exception with a custom message
try:
   num = int(input("Enter number: "))
   if num == 0:
       raise ZeroDivisionError("Number cannot be zero")
except ZeroDivisionError as e:
   print("Error:", e)