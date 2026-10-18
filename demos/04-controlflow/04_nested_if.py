battery = 80
photos_left = 3
if battery >= 20:
    if photos_left > 0:
        print("Camera ready")
    else:
        print("Storage full")
else:
    print("Charge the battery")
