import threading
import time
def Display():
    for i in range(5):
        time.sleep(2)
        print('Thread started')
        
T=threading.Thread(target=display)
T.start()
