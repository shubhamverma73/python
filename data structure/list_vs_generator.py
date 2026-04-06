listCreate = [n for n in range(1, 11)]
print(type(listCreate))  # Output: <class 'list'>
print(listCreate)
# List ek collection hoti hai jo saare elements ko memory me ek saath store karti hai.
# List 👉 Jaise aapne ek baar me 1000 photos download kar li

#--------------------------------------
generatorCreate = (n for n in range(1, 11))
print(type(generatorCreate))  # Output: <class 'generator'>
print(generatorCreate)
for x in generatorCreate:
    print(x)
# Generator ek aisa object hai jo values ko ek-ek karke generate karta hai (on demand), na ki sab ek saath.
# Generator 👉 Jaise aap scroll karte jao aur photos load hoti jaye

# Kab kya use kare?
# ✅ List → jab data chhota ho aur baar-baar use karna ho
# ✅ Generator → jab data bada ho ya streaming type ho

'''
| Feature   | List        | Generator                       |
| --------- | ----------- | ------------------------------- |
| Memory    | Zyada use   | Bahut kam use                   |
| Execution | Immediate   | Lazy (jab chahiye tab)          |
| Syntax    | `[]`        | `()`                            |
| Speed     | Fast access | Thoda slow per memory efficient |
| Use case  | Chhota data | Large data / streams            |
'''