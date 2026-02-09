string = "ShUbHaM"
print(string.lower()) # shubham
print(string.upper()) # SHUBHAM
print(len(string)) # 7
print(string[0]) # S
print(string.title()) # Shubham, Make frist letter capital and rest small
print(string.capitalize()) # Shubham, Make frist letter capital and rest small
print(string.count("h")) # 2, count the number of times h is present in string
print(string.find("h")) # 2, find the index of first occurrence of h

# Excersise - Take name from user and one character, print length of name and count of that character in name either in lower case or upper caseone
'''
name = input("What is your name? ")
one_character = input("Input one character: ")
print(len(name))
print(name.lower().count(one_character.lower()))
'''