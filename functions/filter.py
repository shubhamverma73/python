list1 = [1, 2, 3, 4, 5]

#--------------------------------
def getOdd(num):
    oddNum = []
    for i in num:
        if i % 2 != 0:
            oddNum.append(i)
    return oddNum
print(getOdd(list1))  # Output: [1, 3, 5]

#--------------------------------
# Using filter with a function to get odd numbers from the list
def is_odd(num):
    return num % 2 != 0
odd_numbers = filter(is_odd, list1)
print(list(odd_numbers))  # Output: [1, 3, 5]

#--------------------------------
# Using filter to get even numbers from the list
even_numbers = filter(lambda num: num % 2 == 0, list1)
print(list(even_numbers))  # Output: [2, 4]

#--------------------------------
# Using list comprehension to get odd numbers from the list
odd_numbers = [num for num in list1 if num % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5]
