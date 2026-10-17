import threading
import time

thread_break = False


def TimeProcess():
    while not thread_break:
        print(time.time() - start_time)


start_time = time.time()

threading.Thread(target=TimeProcess).start()

input()
thread_break = True
quit()
