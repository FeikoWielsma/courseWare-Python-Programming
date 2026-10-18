for filename in ["cover.jpg", "notes.txt", "stage.jpg"]:
    if not filename.endswith(".jpg"):
        continue
    print(f"Photo: {filename}")

for track in ["Thriller", "Imagine", "Yesterday", "Respect", "Hey Jude"]:
    if track == "Respect":
        break
    print(f"Checked {track}")
print("Search complete")
