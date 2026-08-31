import matplotlib.pyplot as plt

expenses = [3000,5000,2000,4000]
categories = ["Food","Rent","Travel","Shopping"]

plt.pie(expenses,labels=categories,autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()