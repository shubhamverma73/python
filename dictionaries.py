dict1 = {"name": "shubham", "age": 25, "city": "delhi"}
print(dict1)
print(type(dict1))
#--------------------------------

dict2 = dict(pincode=110001, nationality="Indian", region="delhi")
print(dict2)
print(type(dict2))

#--------------------------------
dict1.update(dict2)
print(dict1)

#--------------------------------
dict3 = {"name": "shubham", "age": 25, "city": "delhi"}
dict3["age"] = 26
print(dict3)


#--------------------------------
dict4 = {"name": "Vishwash", "age": 30, "city": "Bhadohi"}
dict5 = dict4.copy()
print(dict4)
dict5["name"] = "Shubham" # changing the name in dict5 should not affect dict4
print(dict5)