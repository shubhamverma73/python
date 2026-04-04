def sum(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j

print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# --------------------------------
def sumWithArgs(*args):
    total = 0
    for value in args:
        total += value
    return total

print(sumWithArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#--------------------------------
def showNumWithArgs(num, *args):
    print("num:", num)
    print("args:", args)
    print("Type of num:", type(num))
    print("Type of args:", type(args))

showNumWithArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#-------------------------------
def passListAsArgs(*args):
    print("args:", args)

my_list = [1, 2, 3, 4, 5, 1]
passListAsArgs(*my_list)  # Unpacking the list into individual arguments