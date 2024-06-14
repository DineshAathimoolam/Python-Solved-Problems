class Circle:
    def __init__(self, radius):
        self.__radius = radius  

    def area(self):
        return 3.14 * self.__radius ** 2

circle = Circle(3)
print(circle.area())

