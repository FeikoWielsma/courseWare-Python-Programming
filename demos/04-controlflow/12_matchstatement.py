command = "play"
match command:
    case "play":
        print("Playing the current track")
    case "skip":
        print("Moving to the next track")
    case "quit":
        print("Player stopped")
    case _:
        print("Unknown player command")
