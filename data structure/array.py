# This code demonstrates basic operations on lists (arrays) in Python.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

# Removing the last element from the list
numbers = [1, 2, 3, 4, 5]
numbers.pop()
print(numbers)

# Accessing elements in a list
print(fruits[0])  # Output: apple

# Slicing a list
print(fruits[1:3])  # Output: ['banana', 'cherry']

# Iterating through a list
for fruit in fruits:
    print(fruit)

# add number in list at first position
numbers.insert(0, -1)
print(numbers)  # Output: [-1, 1, 2, 3, 4, 5]


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
# Concatenating two lists
arr3 = arr1 + arr2
print(arr3)  # Output: [1, 2, 3, 4, 5, 6]


arr3 = ['a', 'b', 'c']
arr3.remove('b')
print(arr3)  # Output: ['a', 'c']

arr4 = [1, 2, 3, 4, 5, 9, 10, 6]
arr4.sort()
print(arr4)  # Output: [1, 2, 3, 4, 5, 6, 9, 10]