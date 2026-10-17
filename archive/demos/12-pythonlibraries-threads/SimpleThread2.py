from threading import Thread


class MyThread(Thread):
    def run(self):
        print("hello from thread %s" % self.name)


for i in range(3):
    my_thread = MyThread()
    my_thread.name = i
    my_thread.start()
