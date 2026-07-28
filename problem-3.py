my_dict={"name":"John", "age":30, "city":"New York"}

my_dict1={"address":"123 Main St", "phone":"555-1234"}
#method 1:
#merged_dict={**my_dict, **my_dict1}

#method 2:
merged_dict=my_dict.copy()
merged_dict.update(my_dict1)
print("Merged dictionary:", merged_dict)

#method 3:
combined_dict=my_dict | my_dict1
print("Combined dictionary:", combined_dict)

nested_dict={"person": {"name":"John", "age":30, "city":"New York"}, "contact": {"address":"123 Main St", "phone":"555-1234"}}
print("Nested dictionary:", nested_dict)

print("age:", nested_dict["person"]["age"])
print("phone:", nested_dict["contact"]["phone"])

my_dict={"old_name":"John", "age":30, "city":"New York"}
#rename "old_name" to "new_name"
my_dict["new_name"] = my_dict.pop("old_name")
print("Updated dictionary:", my_dict)   

my_dict={"name":"John", "age":30, "city":"New York"}

for key, value in my_dict.items():
    print(key, ":", value)

for key in my_dict.keys():
    print("Key:", key)
    
for value in my_dict.values():
    print("Value:", value)

keys=["name", "age", "city"]
values=["John", 30, "New York"]

#combine keys and values into a dictionary
combined_dict=dict(zip(keys, values))
print("Combined dictionary:", combined_dict)

#clear the dictionary
my_dict.clear()
print("Cleared dictionary:", my_dict)

my_dict={"name":"John", "age":30, "city":"New York"}
#remove "age" from the dictionary
my_dict.pop("age")
print("Dictionary after removing 'age,name':", my_dict)

remove_keys=["name", "city"]
for key in remove_keys:
    my_dict.pop(key, None)
print("Dictionary after removing specified keys:", my_dict)

list1=["brand", "model", "year"]
list2=["Lamborghini", "Aventador", 2020]

#combine two lists into a dictionary
combined_dict=dict(zip(list1, list2))
print("Combined dictionary:", combined_dict)

#create a dictionary with squares of numbers from 1 to 10
squares={x: x**2 for x in range(1, 11)}
print("Squares dictionary:", squares)

fruits_dict={"apple": 5, "banana": 10, "cherry": 15}
print("Fruits dictionary:", fruits_dict)

#get the max value in the dictionary
max_value=max(fruits_dict.values())
print("Max value in the dictionary:", max_value)

#get the min value in the dictionary
min_value=min(fruits_dict.values())
print("Min value in the dictionary:", min_value)

#list of tuples
tuples_list=[("name", "John"), ("age", 30), ("city", "New York")]
#convert list of tuples to dictionary   
combined_dict=dict(tuples_list)
print("Combined dictionary:", combined_dict)

fruits_dict2={"apple": 5, "banana": 10, "watermelon": 15}

#union of two dictionaries
union_dict={**fruits_dict, **fruits_dict2}
print("Union dictionary:", union_dict)

#intersection of two dictionaries
intersection_dict={k: fruits_dict[k] for k in fruits_dict if k in fruits_dict2}
print("Intersection dictionary:", intersection_dict)

#common keys in two dictionaries
common_keys=set(fruits_dict.keys()) & set(fruits_dict2.keys())
print("Common keys:", common_keys)

#common values in two dictionaries
common_values=set(fruits_dict.values()) & set(fruits_dict2.values())
print("Common values:", common_values)