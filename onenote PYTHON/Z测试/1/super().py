class Animal:
    def __init__(self):
        self.name = "DingDing"
        self.age = 8
        self.food = "rice"

    def eat(self):
        print(f"{self.name.title()} is eating {self.food}.")

    def old(self):
        if self.age == 1:
            print(f"{self.name.title()} is {self.age} year old.")
        else:
            print(f"{self.name.title()} is {self.age} years old.")


class Communicate(Animal):
    def answer(self):
        super(Communicate, self).old()


An = Animal()
print("===" * 10)

Communicate().answer()
