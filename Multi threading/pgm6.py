import threading
import time
def worker_a():
    print('Thread1 Started')
    time.sleep(5)
    print('Thread1 Finished')
def worker_b():
    print('Thread2 Started')
    print('Thread2 Finished')
t1=threading.Thread(target=worker_a,daemon='True')
t2=threading.Thread(target=worker_b)
t1.start()
t2.start()
t1.join()
t2.join()


