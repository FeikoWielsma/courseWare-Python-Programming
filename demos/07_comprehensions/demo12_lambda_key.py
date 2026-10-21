plays = {"Bohemian Rhapsody": 41, "Yesterday": 97, "Imagine": 63}
most_played = sorted(plays, key=lambda title: plays[title], reverse=True)
print(most_played)  # ['Yesterday', 'Imagine', 'Bohemian Rhapsody']
print(max(plays, key=lambda title: plays[title]))  # Yesterday
