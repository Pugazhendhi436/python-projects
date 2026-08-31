import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
#shape
print(matrix.shape)
#size
print(matrix.size)
#number of dimensions
print(matrix.ndim)
#data type
print(matrix.dtype)
zeroes = np.zeros((2, 3))
print(zeroes)
numbers = np.arange(10)
print(numbers)

#operations
arr1 = np.array([1, 2, 3])
arr2 = arr1.sum()
print(arr2)

avg = arr1.mean()
print(avg)

max_value = arr1.max()
print(max_value)

min_value = arr1.min()
print(min_value)

std_dev = arr1.std()
print(std_dev)

#indexing and slicing

arr = np.array([10,20,30,40,50])

print("Original:", arr)
print("30 =", arr[2])
print("Last =", arr[-1])
print("20,30,40 =", arr[1:4])
print("Reverse =", arr[::-1])

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nMatrix:\n", matrix)
print("Center:", matrix[1,1])
print("First row:", matrix[0])
print("Last column:", matrix[:,2])
print("5,6,8,9:\n", matrix[1:,1:])

#reshaping

arr = np.arange(1,13)
print("Original:", arr)

print("\n3 x 4")
print(arr.reshape(3,4))

print("\n4 x 3")
print(arr.reshape(4,3))

prices = np.array([100,200,300,400])
tax = 0.18

print("\nPrices:", prices)
print("With Tax:", prices + prices * tax)

