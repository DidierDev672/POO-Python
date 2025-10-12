class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self


ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filuo", 8)

ozzy.doginfo()
skippy.doginfo()
filou.doginfo()

# ozzy.age = 3
ozzy.birthday()
ozzy.setBuddy(filou)

print(f"Ozzy age: ", ozzy.age)
print(f"Buddy: ", ozzy.buddy.name, " age: ", ozzy.buddy.age)

print(f"Buddy of 'Filuo': ", filou.buddy.name, " age: ", filou.buddy.age)
# print(ozzy.name)
# print(ozzy.age)
# print(ozzy.bark())

# print(ozzy.name + "  is " + str(ozzy.age) + "  years(s) old.")
