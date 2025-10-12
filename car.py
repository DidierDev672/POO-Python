class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, count):
        self.speed += count

    def curb(self, descrement):
        self.speed -= descrement

    def state(self):
        print(f"{self.model} {self.brand} va a {self.speed} km/h")


car = Car("Toyota", "Corolla")
car.accelerate(50)
car.state()
car.curb(20)
car.state()
