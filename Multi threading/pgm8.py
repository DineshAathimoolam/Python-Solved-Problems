import threading
class ThreadDemo(threading.Thread):
    def run(self):
        print('Hello')
        self.new()
        return
    def new(self):
        print('Welcome')
for i in range(5):
    t=ThreadDemo()
    t.start()
