touple = (1, 2, 3, 4, 5)
print(touple)
print(type(touple))
#--------------------------------

touple2 = "shubham", 25, "verma"
print(touple2)
print(type(touple2))
# --------------------------------

def functionwithtouple(name, age, surname):
    return name, age, surname

functiontouple = functionwithtouple("shubham", 25, "verma")
print(functiontouple)
print(type(functiontouple))

#--------------------------------
name, age, surname = functionwithtouple("shubham", 25, "verma")
print(name)
print(age)
print(surname)

#--------------------------------
touple3 = tuple(range(1, 6))
print(touple3)
print(type(touple3))