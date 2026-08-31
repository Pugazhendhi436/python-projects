import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [100,150,130,180,220]

plt.plot(months,sales,marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()