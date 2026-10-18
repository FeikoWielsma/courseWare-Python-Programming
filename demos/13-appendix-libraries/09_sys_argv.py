import sys

print(f"Script: {sys.argv[0]}")
playlist_file = sys.argv[1] if len(sys.argv) > 1 else "night-drive.json"
print(f"Playlist file: {playlist_file}")
