class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno

    def Display(self):
        print('Your name is :',self.name)
        print('Your reg no is :',self.regno)

T1=teacher(input('Enter your name:'),input('Enter your reg no:'))
T2=teacher(input('Enter your name:'),input('Enter your reg no:'))

T1.Display()
T2.Display()
