class Car:
    def __init__(self, model, carbrand):
        self.model = model
        self.carbrand = carbrand

MyCar = Car("Elantra", "Hyundai")

print(f'My car is made by {MyCar.carbrand} and is an {MyCar.model}')