#sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 natural numbers:", total)
print("Sum of first 10 natural numbers using for loop:", total)
#nested loop
for i in range(1, 5):#rows
  
    for j in range(1, i+1):#columns
     
        print("*", end=" ")


#loop from 1 to 11
n=10
while n>0 and n<=10:
  total += n

print("Sum of first 10 natural numbers using while loop:", total)

