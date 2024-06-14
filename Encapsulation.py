class Base():
    def __init__(self):
        self._a=2
        
class Derived (Base):
    def __init__(self):
        Base.__init__(self)
        print('Calling Protected Member of the Base Class: ',self._a)

        self._a=3
        print('calling Modified Protected Member outside class: ',self._a)

obj=Derived()
obj1=Base()


    
