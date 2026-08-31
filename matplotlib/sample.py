import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name":["Asha","Rahul","John","Priya","David","Sara","Mike","Anu","Ravi","Neha"],
    "Age":[22,25,21,24,26,23,27,22,25,24],
    "Department":["IT","HR","IT","Finance","IT","HR","Finance","IT","HR","Finance"],
    "Salary":[50000,45000,60000,55000,70000,48000,65000,58000,52000,62000]
}

df = pd.DataFrame(data)

salary = df["Salary"].to_numpy()

print("Average Salary:", np.mean(salary))
print("Maximum Salary:", np.max(salary))
print("Minimum Salary:", np.min(salary))
print("Standard Deviation:", np.std(salary))

print("\nFirst 5 Employees\n", df.head())
print("\nSalary >55000\n", df[df["Salary"] > 55000])
print("\nSorted Salary\n", df.sort_values("Salary", ascending=False))
print("\nAverage by Department\n", df.groupby("Department")["Salary"].mean())
print("\nHighest Paid Employee\n", df.loc[df["Salary"].idxmax()])
print("\nDepartment Count\n", df["Department"].value_counts())

plt.figure()
plt.bar(df["Name"], df["Salary"])
plt.xticks(rotation=45)
plt.title("Employee Salary")
plt.tight_layout()
plt.show()

avg = df.groupby("Department")["Salary"].mean()
plt.figure()
plt.bar(avg.index, avg.values)
plt.title("Department Average Salary")
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.show()

plt.figure()
plt.hist(df["Salary"], bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.show()

counts = df["Department"].value_counts()
plt.figure()
plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
plt.title("Employees by Department")
plt.show()