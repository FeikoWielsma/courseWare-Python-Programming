import _thread


def counter(my_id, count):
    for i in range(count):
        print("[%s] => %s" % (my_id, i))


for i in range(10):
    print(_thread.start_new(counter, (i, 100)))

import time

time.sleep(3)
print("Main thread exiting.")
