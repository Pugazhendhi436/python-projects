my_tuple=("apple", "banana", "cherry")
print("My tuple:", my_tuple)

print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Last element:", my_tuple[-1])

print(my_tuple*4)

#reverse the tuple
reversed_tuple=my_tuple[::-1]
print("Reversed tuple:", reversed_tuple)

string_tuple="#".join(my_tuple)
print("String tuple:", string_tuple)

#count the number of elements in the tuple
count=len(my_tuple)
print("Number of elements in the tuple:", count)

apple_count=my_tuple.count("apple")
print("Count of 'apple' in the tuple:", apple_count)

banana_count=my_tuple.count("banana")
print("Count of 'banana' in the tuple:", banana_count)

cherry_count=my_tuple.count("cherry")
print("Count of 'cherry' in the tuple:", cherry_count)

#sort the tuple
sorted_tuple=tuple(sorted(my_tuple))

descending_tuple=tuple(sorted(my_tuple, reverse=True))
print("Sorted tuple:", sorted_tuple)
print("Descending tuple:", descending_tuple)

tuple2=("cabbage", "date", "fig")
tuple3=my_tuple+tuple2
print("Concatenated tuple:", tuple3)

my_tuple=("apple", "banana", "cherry", "date", "fig", "grape")
#slicing the tuple
sliced_tuple=my_tuple[1:4]
print("Sliced tuple:", sliced_tuple)    

#get total number of elements in the tuple
total_elements=len(my_tuple)
print("Total elements in the tuple:", total_elements)

#find the maximum and minimum elements in the tuple
max_element=max(my_tuple)
min_element=min(my_tuple)
print("Maximum element in the tuple:", max_element)
print("Minimum element in the tuple:", min_element)

#tuple of integers
int_tuple=(5, 2, 9, 1, 7)
print("Integer tuple:", int_tuple)

#find the maximum and minimum elements in the integer tuple
max_int=max(int_tuple)
min_int=min(int_tuple)
print("Maximum element in the integer tuple:", max_int)
print("Minimum element in the integer tuple:", min_int)

#nested tuple
nested_tuple=(1, 2, (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)

#selecting elements from the nested tuple
print("third element of the nested tuple:", nested_tuple[2][1])

tuple4=(11,22,44,1,2,3,5,67,23,234)
x_greater_than_10=tuple(filter(lambda x: x > 10, tuple4))
print("Elements greater than 10:", x_greater_than_10)

#intersection of two tuples
int_tuple=(5, 2, 9, 1, 7)
tuple5=(2, 9, 1, 7, 3)
intersection=tuple(set(int_tuple) & set(tuple5))
print("Intersection of tuples:", intersection)

#nested tuple to flat tuple
nested_tuple2=(1, 2, (3, 4), (5, 6))
flat_tuple=tuple(item for sublist in nested_tuple2 for item in (sublist if isinstance(sublist, tuple) else (sublist,)))
print("Flat tuple:", flat_tuple)

