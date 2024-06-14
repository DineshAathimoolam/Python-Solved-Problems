import threading
import time
def display(x):
    for i in range(5):
        time.sleep(x+1.5)
        print(threading.current_thread().getName())
        print('Thread started')
        
for p in range(5):
    t=threading.Thread(target=display,args=(p,))
    t.setName('Thread'+str(p))
    t.start()
