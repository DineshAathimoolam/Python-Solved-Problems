import threading
class ThreadDemo(threading.Thread):
    def __init__(self,args=(),kwargs=None):
        threading.Thread.__init__(self)
        self.args=args
        self.kwargs=kwargs
    def run(self):
        print('Thread',self.args,'Arguments is',self.kwargs)
        return
for i in range(5):
    t=ThreadDemo(args=(i,),kwargs='hello')
    t.start()
    
