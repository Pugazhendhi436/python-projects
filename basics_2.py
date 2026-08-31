import pandas as pd

#series
s = pd.Series([1, 2, 3, 4, 5])
print(s)

max_value = s.max()
print(max_value)

min_value = s.min()
print(min_value)

mean_value = s.mean()
print(mean_value)

marks = pd.Series([80,65,90,75,88], index=["A","B","C","D","E"])

print(marks)
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Average:", marks.mean())
print("Above 75:\n", marks[marks > 75])

#dataframe
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print(df)

#data selection
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print(df["Name"])
print(df["City"])
print(df[["Name","City"]])
print("First row loc:\n", df.loc[0])
print("First row iloc:\n", df.iloc[0])
print("First 3 rows:\n", df.iloc[:3])

#filtering
print("\Alice\n", df[df["Name"] == "Alice"])
print("\nAge >23\n", df[df["Age"] > 23])

#sorting
print("Ascending\n", df.sort_values("Age"))
print("\nDescending\n", df.sort_values("Age", ascending=False))
print("\nTop 3\n", df.nlargest(3,"Age"))
print("\nBottom 2\n", df.nsmallest(2,"Age"))

#csv files

df = pd.DataFrame({
    "Name":["Asha","Rahul","John","Priya","David"],
    "Marks":[85,72,91,68,88]
})

df.to_csv("students.csv", index=False)

data = pd.read_csv("students.csv")

print(data)
print("\nFiltered\n", data[data["Marks"] > 80])
print("\nSorted\n", data.sort_values("Marks", ascending=False))
print("\nStatistics\n", data.describe())

data["Bonus"] = 5
data.to_csv("students_modified.csv", index=False)
print("\nSaved students_modified.csv")

#missing values
print(df)
print("\nMissing:\n", df.isnull())

#group by
df = pd.DataFrame({
    "Department":["IT","HR","IT","Finance","HR","IT"],
    "Employee":["A","B","C","D","E","F"],
    "Salary":[50000,40000,60000,55000,45000,70000]
})

print("Average\n", df.groupby("Department")["Salary"].mean())
print("\nMaximum\n", df.groupby("Department")["Salary"].max())
print("\nMinimum\n", df.groupby("Department")["Salary"].min())
print("\nCount\n", df.groupby("Department")["Employee"].count())
