import pickle

data = {"name": "Arun", "age": 20, "marks": [85, 90, 88]}

with open("data.pkl", "wb") as file:
   pickle.dump(data, file)

with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
print(loaded_data)


# multiple objects in a single file
with open("multi.pkl", "wb") as file:
   pickle.dump([1, 2, 3], file)
   pickle.dump("Hello", file)

with open("multi.pkl", "rb") as file:
   print(pickle.load(file))
   print(pickle.load(file))