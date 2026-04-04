list = ["apple", "banana", "cherry"]
num = 0
for fruit in list:
    print(f"position {num}: Value  => {fruit}")
    num += 1

#--------------------------------
list2 = ["delhi", "mumbai", "kolkata"]
for position, fruit in enumerate(list2):
    print(f"position {position}: Value  => {fruit}")