def sum(a,b):
    return a+b
print(sum(1,2))

#--------------------------------
minus = lambda a,b: a-b
print(minus(5,3))

#--------------------------------
print((lambda a,b: a*b)(2,3))

#--------------------------------
isEven = lambda val: val % 2 == 0
print(isEven(4))  # Output: True
print(isEven(5))  # Output: False


#--------------------------------
def ifElseCondition():
    if 5 > 3:
        return True
    else:
        return False
print(ifElseCondition())

#--------------------------------
isGreater = lambda: True if 5 > 3 else False
print(isGreater())  # Output: True

#--------------------------------
withoutIfElse = lambda: 5 > 3
print(withoutIfElse())  # Output: True