import _thread


def hello(num):
    print("hello from thread %s\n" % num)


_thread.start_new_thread(hello, (0,))
_thread.start_new_thread(hello, (1,))
_thread.start_new_thread(hello, (2,))

import time

time.sleep(1)
