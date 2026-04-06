class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self, action=None):
        print(self.name + " start ho gayi" + str(action))

    def stop(self):
        return f"{self.name} stop ho gayi"

car1 = Car("BMW", "Black")
print(car1.color)
car1.start(" aur chal bhi di hai")
print(car1.stop())