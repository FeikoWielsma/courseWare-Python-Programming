import numpy as np

times = np.arange(8) / 8000
tone = np.sin(2 * np.pi * 440 * times)
quiet = tone * 0.5
print(quiet.round(3))
print(np.sqrt(tone ** 2).round(3))
print((tone - quiet).round(3))
