class parrot:
    def fly(self):
        print('Parrot can fly')
    def swim(self):
        print("Parrtot can't Swim")

class penguin:
    def fly(self):
        print('penguin cannot fly')
    def swim(self):
        print("penguin can Swim")

blue=parrot()
pen=penguin()

for bird in (blue,pen):
    bird.fly()
    bird.swim()
