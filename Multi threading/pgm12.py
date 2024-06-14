import threading

def Threading_fun():
    for i in range(3):
        print('Hello')


def Threading_fun1():
    for i in range(4):
        print('Hi')

t1=threading.Thread(target=Threading_fun)
t2=threading.Thread(target=Threading_fun1)

t1.start()
t2.start()

t1.join()
t2.join()

        
