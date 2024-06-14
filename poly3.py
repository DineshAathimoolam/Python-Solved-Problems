class Animal():
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return('The sound of Dog is Woof!')

class Cat(Animal):
    def sound(self):
        return('The Sound of Cat is Meow')

Animals=[Dog(),Cat()]
for animals in Animals:
    print(animals.sound())

