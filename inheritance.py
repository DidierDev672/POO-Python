
#? Herencia múltiples
# todo: Una clase puede heredor de varias clases.

class Flying:
    def fly(self):
        print("Puedo volar")


class Swimmer:
    def swim(self):
        print("Puedo nadar")


class Duck(Flying, Swimmer):
    pass


donald = Duck()
donald.fly()
donald.swim()
