food_obj={"pizza", "burger", "pasta"}
new_set=set()
#length of the set
set_length=len(food_obj)
print("Length of the set:", set_length)

#union of two sets
set1={"apple", "banana", "cherry"}
set2={"date", "elderberry", "fig"}
union_set=set1 | set2
print("Union of sets:", union_set)

#intersection of two sets
intersection_set=set1 & set2
print("Intersection of sets:", intersection_set)

#difference of two sets
difference_set=set1 - set2
print("Difference of sets:", difference_set)

#symmetric difference of two sets
symmetric_difference_set=set1 ^ set2
print("Symmetric difference of sets:", symmetric_difference_set)

#find maximum and minimum elements in the set
max_element=max(set1)
min_element=min(set1)
print("Maximum element in the set:", max_element)
print("Minimum element in the set:", min_element)

#find sum of elements in the set
set4={1, 2, 3, 4, 5}
sum_elements=sum(set4)
print("Sum of elements in the set:", sum_elements)

set={3,6,9,12,15,18,21,24,27,30}
#keep only perfect squares in the set
perfect_squares={x for x in set if (x**0.5).is_integer()}
print("Perfect squares in the set:", perfect_squares)

#create a set of squares of numbers from 1 to 10
squares_set={x**2 for x in range(1, 11)}    
print("Set of squares from 1 to 10:", squares_set)


# join set to string
fruit_set = {"apple", "banana", "cherry"}
print("Joined set to string:", ", ".join(fruit_set))
print(new_set)
object_6 = {1, 8, 27, 64, 125}
object_7 = {1, 2, 27, 4, 5}

for item in object_6:
    if item in object_7:
        print(item, "is a duplicate")
    else:
        print(item, "is unique")
        new_set.add(item)
print(new_set)
