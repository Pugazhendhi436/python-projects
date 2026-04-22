x = int(input("Enter a number: "))
def greeting():
    global x
    x=x+5
    print("welcome")
    print(x)
greeting()

b = int(input("Enter a number: "))
def calculate():
    a=5
    c=lambda a,b:a+b
    print(c(a,b))
calculate()