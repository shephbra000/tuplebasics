fruit_tuple = ("apple", "banana", "cherry", "date")
print("First element:", fruit_tuple)
print("Last element:", fruit_tuple[-1])
slice_tuple = fruit_tuple[1:3]
print("Slice tuple:", slice_tuple)

num_tuple = (3, 5, 3, 2, 8, 3, 7)
count_of_3 = num_tuple.count(3)
print(f"The number 3 appears {count_of_3} times in num_tuple.")
index_of_8 = num_tuple.index(8)
print(f"The first occurrence of 8 is at index {index_of_8} in num_tuple.")

person_info = ("Alice", 28, "Engineer")
name, age, profession = person_info
print("Name:", name)
print("Age:", age)
print("Profession:", profession)