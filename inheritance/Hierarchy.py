class a():
    def features(self):
        print('Feature 1 is working')
    def features2(self):
        print('Feature 2 is working')

class b(a):
    def features3(self):
        print('Feature 3 is working')
    def features4(self):
        print('Feature 4 is working')

class c(a):
    def features5(self):
        print('Feature 5 is working')
        
class d(b,c):
    def features6(self):
        print('Feature 6 is Working')

a1=a()
a1.features()
a1.features2()

b1=b()
b1.features3()
b1.features4()

c1=c()
c1.features5()

d1=d()
d1.features6()
        
