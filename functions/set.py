arr = [1, 2, 3, 4, 5, 1, 2, 3]
# Using set to remove duplicates
unique_arr = set(arr)
print(unique_arr)  # Output: {1, 2, 3, 4, 5}

# --------------------------------
# Using set to find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print(common_elements)  # Output: {3, 4}

#--------------------------------
# Using set to find unique elements in a list
tuple = (1, 2, 2, 3, 4, 4, 5)
unique_elements = set(tuple)
print(unique_elements)  # Output: {1, 2, 3, 4, 5}

#--------------------------------
dict1 = {"name": "shubham", "age": 25, "city": "delhi", "name": "vishwash", "age": 30, "city": "bhadohi"}
print(dict1)  # Output: {'name': 'vishwash', 'age': 30, 'city': 'bhadohi'}