#list_operations.py

foods=["pizza", "burger", "pasta"]
my_list=[1,2,3,4,5,6,7,8,9,10]
original_list=[1,2,3,4,5,6,7,8,9,10,1,2,3]

# Convert to set and back to list
unique_list = list(set(original_list))

print("Original foods:", foods)
print("Unique list:", unique_list)

for i in range(len(foods)):
    print("Food at index", i, "is", foods[i])

#sort the list
foods.sort()
print("\nSorted ascending:", foods)

foods.sort(reverse=True)
print("Descending:", foods)

print("\nMax:", max(my_list))
print("Min:", min(my_list))
print("Sum:", sum(my_list))

foods.append("grape")
foods.insert(1, "mango")
foods.extend(["kiwi", "pear"])
foods.insert(0, "biryani")
print("\nAfter adding:", foods)
    
if "grape" in foods: 
    print("Grape is in the list")

else:
    print("Grape is not in the list")

words=["biryani","pizza","burger","pasta","grape","mango","kiwi","pear"]
longest_word=max(words, key=len)
print("Longest word:", longest_word)

my_list=[1,2,3,4,5,6,7,8,9,10]
squared=[x**2 for x in my_list]
print("Squared list:", squared)

my_list=[1,2,3,4,5,6,7,8,9,10]
original_list=[1,2,3,4,5,6,7,8,9,10,1,2,3]
combined=my_list+original_list
print("Combined list:", combined)

my_list=[1,2,3,4,5,6,7,8,9,10]
my_list.reverse()
print("Reversed list:", my_list)

