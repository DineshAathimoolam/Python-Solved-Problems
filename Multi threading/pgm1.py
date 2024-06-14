import threading
import time
def display(x,t1):
    for i in range(x):
        time.sleep(t1)
        print('Thread started')
t=threading.Thread(target=display,args=(10,2,))
t.start()
        
