filename = input("Photo filename: ")
if filename.lower().endswith(".jpg"):
    print(f"Photo selected: {filename}")
else:
    print("Choose a JPG photo")
