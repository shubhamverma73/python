class Car:
    count_instances = 0
    def __init__(self, name, color):
        Car.count_instances += 1
        self.name = name
        self.color = color

    def start(self, action=None):
        print(self.name + " start ho gayi" + str(action))

    def stop(self):
        return f"{self.name} stop ho gayi"

car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")
car3 = Car("Tata", "Purple")
car4 = Car("M&M", "Blue")
print(Car.count_instances)