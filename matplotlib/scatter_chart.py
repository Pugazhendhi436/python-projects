import matplotlib.pyplot as plt

age = [20,21,22,23,24,25]
salary = [25000,28000,30000,35000,40000,45000]

plt.scatter(age,salary)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.show()