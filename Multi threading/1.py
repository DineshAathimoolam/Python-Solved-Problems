import threading
import time
def display(x):
    for i in range(5):
        time.sleep(x+1.5)
        print(threading.current_thread().getName())
        print("Thread Started")
for p in range(5):
    t=threading.Thread(target=display,args=(p,))
    t.setName("thread"+str(p))
    t.start()
