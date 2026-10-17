command = "help"
match command:
    case "help":
        print("Available commands: help, quit")
    case "quit":
        print("Goodbye")
    case _:
        print("Unknown command")
