filename = "IMG_0421.jpg"
print(filename[0])  # I
print(filename[-1])  # g
print(filename[4:8])  # 0421
print(filename[-4:])  # .jpg
print(".jpg" in filename)  # True

edited = filename[:-4] + "_edit.jpg"
print(edited)  # IMG_0421_edit.jpg
print(filename)  # IMG_0421.jpg

print("-" * 12)  # ------------
print(filename[::-1])  # gpj.1240_GMI
