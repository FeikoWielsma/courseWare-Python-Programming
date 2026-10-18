filename = "cover.png"
if filename.endswith(".jpg"):
    print("JPEG photo")
elif filename.endswith(".png"):
    print("PNG image")
else:
    print("Unsupported image format")
