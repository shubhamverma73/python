def canUserPlayGame(age):
    if age < 18:
        return "You are not old enough to play this game."
    else:
        return "You can play the game."
    
try:
    print(canUserPlayGame(int(input("Enter your age: "))))
except ValueError as e:
    print(f"{e}: Please enter a valid number for age.")

#print(canUserPlayGame(int(input("Enter your age: "))))