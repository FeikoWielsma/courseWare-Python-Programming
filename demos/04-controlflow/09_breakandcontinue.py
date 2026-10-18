for filename in ["cover.jpg", "notes.txt", "stage.jpg"]:
    if not filename.endswith(".jpg"):
        continue
    print(f"Photo: {filename}")

for track in ["Intro", "Orbit", "Echo", "Pulse", "Outro"]:
    if track == "Pulse":
        break
    print(f"Checked {track}")
print("Search complete")
