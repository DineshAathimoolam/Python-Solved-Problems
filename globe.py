globvar=10
def read1():
    print(globvar)
def write1():
    global globvar
    globevar=5
def write2():
    globevar=15

read1()
write1()
read1()
write2()
read1()
    
