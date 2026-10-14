try:
    fh = open("somefile", "r")
except FileNotFoundError:
    print("The file does not exist")
except OSError as error:
    print(f"Cannot open the file: {error}")
else:
    fh.close()
