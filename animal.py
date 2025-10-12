class Animal:
    def __init__(self, name):
        self.name = name

    def speek(self):
        print(f"The animal makes a sound")


class Dog(Animal):
    def speek(self):
        print(f"Guau!")


class Cat(Animal):
    def speek(self):
        print("Miau!")


dog = Dog("Firulais")
cat = Cat("Mishi")

dog.speek()
cat.speek()

# ? Polimorfismo
# TODO: Significa "Muchas formas": distintos objectos pueden usar el mismo método de forma diferente.

animales = [Dog("Boddy"), Cat("Luna")]

for animal in animales:
    animal.speek()
