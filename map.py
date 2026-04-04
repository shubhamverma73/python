list1 = [1, 2, 3, 4, 5]

def multiplyWith2(num):
    return num * 2

# Using map to apply the function to each element in the list
result = map(multiplyWith2, list1)
print(result)  # Output: <map object at 0x7f8b8c8d9e50>
print(list(result))  # Output: [2, 4, 6, 8, 10]

#--------------------------------
# Using map with a lambda function
result = map(lambda num: num * 2, list1)
print(list(result))  # Output: [2, 4, 6, 8

#--------------------------------
#using list comprehension to achieve the same result
result = [num * 2 for num in list1]
print(result)  # Output: [2, 4, 6, 8, 10]