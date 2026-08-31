import matplotlib.pyplot as plt

subjects = ["Math","Science","English","Python"]
marks = [80,75,90,95]

plt.bar(subjects,marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject Marks")
plt.show()