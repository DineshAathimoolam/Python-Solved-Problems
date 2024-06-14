class laptop:
    charger_type='C-Type'
    def __init__(self):
        self.Brand=""
        self.Price=12000
        
    def setprice(self,price):
        self.price=price
    def Getprice(self):
        print(self.price)

    def change_charger_type(cls):
        cls.charger_type='B-Type'
        print('Laptop charger changed to B')


hp=laptop()
hp.setprice(9000)
hp.Getprice()       
laptop.change_charger_type(laptop)             
