#built in modules
import math


print(math.sqrt(16))
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))



from packages.module1 import add

print(add(2, 3))


# import module
# import module as m
# from module import function
# from package import module
# from package.module import function