import threading
import time
def demo():
    print('Welcome')
t=threading.Timer(3.0,demo)
t.start()
#time.sleep(2)
