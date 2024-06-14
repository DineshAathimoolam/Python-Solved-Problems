class demo():
    def sum(self,a=None,b=None,c=None):
        if a!=Nonen and b!=None and c!=None:
            c=a+b+c
        elif a!=None and b!=None:
            c=a+b
        else:
            c=a
        print(c)
obj=demo()
obj.sum()
obj.sum(10)
