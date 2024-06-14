import threading
import time
def display(x,s,name):
    for i in range(x):
        time.sleep(s)
        print(name,'Thread started')

t=threading.Thread(target=display,args=(6,2,'Dinesh',))
t.start()
t1=threading.Thread(target=display,args=(3,1,'Monoj',))
t1.start()
 
