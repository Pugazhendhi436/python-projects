new_set = set()
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