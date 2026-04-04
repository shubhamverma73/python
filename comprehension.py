list = [1, 2, 3, 4, 5]
squares1 = []
for x in list:
    squares1.append(x**2)
print(squares1)  # Output: [1, 4, 9, 16, 25]

# Using list comprehension to create a new list with squares of the original list
squares = [x**2 for x in list]
print(squares)  # Output: [1, 4, 9, 16, 25]