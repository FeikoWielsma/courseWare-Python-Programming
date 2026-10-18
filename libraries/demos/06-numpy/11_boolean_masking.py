import numpy as np

tone = np.array([0.0, 0.2, 0.9, -0.8, 0.0, -0.1])
silent = np.abs(tone) < 0.05
print(tone[silent])
print(silent.sum(), silent.any(), silent.all())
print(np.nonzero(silent)[0])
print(tone[(tone > -0.5) & (tone < 0.5)])
