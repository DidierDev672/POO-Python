class Student():
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career

    def presenter(self):
        return f"I'm {self.name}, have {self.age} old and estudy {self.career}"


class University(Student):
    def __init__(self, name, age, career, semester):
        super().__init__(name, age, career)
        self.semester = semester

    def presenter(self):
        base = super().presenter()
        return f"{base} and I'm in the semester {self.semester}"


u = University("Sofia", 20, "Engineering", 5)
print(u.presenter())
