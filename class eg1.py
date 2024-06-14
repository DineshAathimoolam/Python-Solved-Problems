class Student:
    def __init__(self):
        self.name=""
        self.Regno=''
    def Display(self):
        print("Name :",self.name)
        print('Reg no is:',self.Regno)

s1=Student()
s2=Student()

s1.name='Dinesh'
s1.Regno='191041018'

s2.name='dinesh'
s2.Regno='19104'
s1.Display()
s2.Display()
