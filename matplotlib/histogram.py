import matplotlib.pyplot as plt

marks = [45,55,60,65,70,72,75,78,80,82,85,90,92,95]

plt.hist(marks,bins=5,edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Marks Distribution")
plt.show()