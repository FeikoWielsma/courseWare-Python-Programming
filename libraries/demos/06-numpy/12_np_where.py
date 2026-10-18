import numpy as np

tone = np.array([-0.9, -0.2, 0.0, 0.4, 0.9])
clipped = np.where(tone > 0.5, 0.5, np.where(tone < -0.5, -0.5, tone))
print(clipped)
print(np.where(np.abs(tone) < 0.05, "silence", "sound"))
print(np.where(tone > 0.5)[0])
