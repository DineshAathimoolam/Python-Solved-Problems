import threading
import time
def Display(i):
    time.sleep(i)
    return
t1=threading.Thread(target=Display,args=(4,),name='Dinesh1')
t1.start()
t2=threading.Thread(target=Display,args=(3,),name='dinesh2')
t2.start()
for x in range(5):
    time.sleep(x+0.5)
    print('[',time.ctime(),t1.name,t1.is_alive(),']')
    print('[',time.ctime(),t1.name,t2.is_alive(),']')

    
