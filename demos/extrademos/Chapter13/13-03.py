import time


class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, string):
        file = open(self.filename, "a")
        file.write("[" + time.asctime() + "] ")
        file.write(string + "\n")
        file.close()


log = Logger("logfile.txt")
