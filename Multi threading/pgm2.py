import threading
import time
def display():
    for i in range(5):
        time.sleep(1)
        print('Thread started')
t=threading.Thread(target=display)
t.start()
