# Tuple ek fixed collection hai jo memory me poora store hota hai.
t = (1, 2, 3, 4)
print(type(t))  # Output: <class 'tuple'>
print(t)        # Output: (1, 2, 3, 4)

# 📌 Features:
# Immutable (change nahi kar sakte)
# Saari values ek saath memory me hoti hain
# Direct access possible (t[0])


# ---------------------------------------
# Generator values ko store nahi karta, balki generate karta hai jab zarurat ho.
# Generator ek aisa object hai jo values ko ek-ek karke generate karta hai (on demand), na ki sab ek saath.
g = (x for x in range(4))
print(type(g))  # Output: <class 'generator'>
print(g)        # Output: <generator object <genexpr> at 0x...>
for value in g:
    print(value)  # Output: 0, 1, 2, 3 (one by one)

# 📌 Features:
# Lazy evaluation (on demand)
# Memory efficient
# Ek baar iterate kar liya → khatam

# ----------------------------------
t = (1, 2, 3)          # tuple
g = (x for x in range(3))  # generator

# 👉 Dono me () use ho raha hai, isliye confusion hota hai
# 👉 But difference andar ke syntax se aata hai:

# Simple values → Tuple
# for loop inside → Generator