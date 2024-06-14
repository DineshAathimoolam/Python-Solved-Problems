class laptop():
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print('Ram is :',self.ram)
        print('Processor is :',self.processor)
hp=laptop()
hp.ram=input("Enter the Ram of your Laptop: ")
hp.processor=input("Enter the Processor of your Laptop:")
hp.display()
