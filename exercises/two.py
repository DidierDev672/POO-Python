
# todo: Crea una clase Empleado y una clase hija Gerente que herede de ella.

class Employee():
    def __init__(self, name, age, profession, jobTitle):
        self.name = name
        self.age = age
        self.profession = profession,
        self.jobTitle = jobTitle

    def description(self):
        return f"I'm {self.name} have {self.age} old and i am professional {self.profession}, I am in charge of the area of {self.jobTitle}"


class Manager(Employee):
    def __init__(self, name, age, profession, jobTitle, timeInOffice, salary):
        super().__init__(name, age, profession, jobTitle)
        self.timeInOffice = timeInOffice
        self.salary = salary

    def information(self):
        base = super().description()
        return f"Information {base} the manager is in office {self.timeInOffice} it has the salary {self.salary}"


empl = Manager("Didier", 28, "Software developer",
               "Software developer", 3, 1000000)
print(empl.information())
