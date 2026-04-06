class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price if price > 0 else "Price should be greater than 0"

    def start(self):
        return f"{self.name} start ho gayi"

    def stop(self):
        return f"{self.name} stop ho gayi"
    

class Tata(Car): # ye inheritance hai, jisme hum ek class ke properties aur methods ko dusre class me use kar sakte hai
    def __init__(self, name, color, price, country):
        super().__init__(name, color, price)
        self.country = country

    def start(self): # ye overriding hai, jisme hum parent class ke method ko child class me dubara define kar dete hai
        return f"{self.name} start ho gayi, country is {self.country}"
    
    def owner(self, owner_name):
        return f"{self.name} ke owner ka naam {owner_name} hai"

tata = Tata("Tata", "White", 30000, "India")
print(tata.color)
print(tata.start())
print(tata.stop())
print(tata.country)
print(tata.owner("Ratan Tata"))