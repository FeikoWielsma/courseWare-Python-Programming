import time

thread_break = False


def TimeProcess():
    while not thread_break:
        print(time.time() - start_time)


start_time = time.time()

TimeProcess()

input()
thread_break = True
quit()
