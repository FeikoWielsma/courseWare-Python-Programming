import threading
import queue
import time, random

WORKERS = 2

class Worker(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue
      

    def run(self):
        while 1:
            item = self.__queue.get()
            if item is None:
                break # reached end of queue

            # pretend we're doing something that takes 10-100 ms
            time.sleep(random.randint(10, 100) / 1000.0)

            print ("task", item, "finished")
#
# try it

queue = queue.Queue(0)

for i in range(WORKERS):
    Worker(queue).start() # start a worker

for i in range(10):
    queue.put(i)

for i in range(WORKERS):
    queue.put(None) # add end-of-queue markers