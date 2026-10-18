titles = ["Afterglow", "Echo", "Orbit"]
print(sorted(titles))  # ['Afterglow', 'Echo', 'Orbit']
print(sorted(titles, key=len))  # ['Echo', 'Orbit', 'Afterglow']
print(min(titles, key=len), max(titles, key=len))  # Echo Afterglow
