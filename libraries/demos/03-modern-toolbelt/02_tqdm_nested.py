import time

from tqdm import tqdm

albums = {"Imagine": ["Imagine", "Jealous Guy"],
          "Thriller": ["Thriller", "Billie Jean"]}
for album, titles in tqdm(albums.items(), desc="Albums"):
    for _title in tqdm(titles, desc=album, leave=False):
        time.sleep(0.02)
