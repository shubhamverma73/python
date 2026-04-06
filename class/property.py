class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price if price > 0 else "Price should be greater than 0"

    def start(self):
        return f"{self.name} start ho gayi"

    @property # ye decorator use karne se hum method ko property bana dete hai, jise hum bina parenthesis ke call kar sakte hai
    def stop(self):
        return f"{self.name} stop ho gayi"

car = Car("BMW", "Black", 50000)
print(car.color)
print(car.price)
print(car.start())
print(car.stop)