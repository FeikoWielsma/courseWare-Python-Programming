class NetworkError(RuntimeError):
    def __init__(self, hostname: str) -> None:
        super().__init__(f"Bad hostname: {hostname}")
        self.hostname = hostname


try:
    raise NetworkError("example.invalid")
except NetworkError as e:
    print(e)  # Bad hostname: example.invalid
    print(e.hostname)  # example.invalid

# Uncaught, it ends the program with a traceback naming the class and message.
raise NetworkError("oops.invalid")
