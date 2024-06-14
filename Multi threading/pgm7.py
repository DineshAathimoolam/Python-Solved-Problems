#current_thread()
import threading
import time
def worker_a():
    print('Thread started')
    print(threading.current_thread())
    time.sleep(5)
for i in range(5):
    t1=threading.Thread(target=worker_a)
    t1.start()
    time.sleep(1)
    print(threading.enumerate())
    print('total thread count')
    print(threading.active_count())
