import queue
import threading
import time

exit_flag = 0


class my_thread(threading.Thread):
    def __init__(self, thread_id, name, q):
        self.thread_id = thread_id
        self.name = name
        self.q = q
        threading.Thread.__init__(self)

    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)


def process_data(thread_name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            queue_lock.release()
        time.sleep(1)


thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_id = 1

# Create new threads
for t_name in thread_list:
    thread = my_thread(thread_id, t_name, work_queue)
    thread.start()
    threads.append(thread)
    thread_id += 1

# Fill the queue
queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()

# Wait for queue to empty
while not work_queue.empty():
    pass

# Notify threads it's time to exit
exit_flag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
