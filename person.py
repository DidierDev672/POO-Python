class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and have {self.age} age.")


# ? Crear un objecto
person = Person("Didier", 28)
person.greet()
