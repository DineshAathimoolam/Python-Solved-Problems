class laptop:
    def __init__(self):
        self.ram=''
        self.processor=''
    def Display(self):
        print('ram is :',self.ram)
        print('Processor is :',self.processor)

Hp=laptop()
Dell=laptop()

Hp.ram='8 G.B'
Hp.processor='i5'

Dell.ram='16 G.b'
Dell.processor='i7'

Hp.Display()
Dell.Display()
