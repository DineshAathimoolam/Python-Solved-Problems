import _thread
import time
def a(msg):
    count=0
    while count<5:
        count+=1
        time.sleep(5)
        print(msg)

def b(msg):
    count=0
    while count<5:
        count+=1
        time.sleep(1)
        print(msg)        
try:
    _thread.start_new_thread(a,('Thread 1',))
    _thread.start_new_thread(b,('Thread 2',))
except:
    print('Error to start The PGM')
    while 1:
        pass
