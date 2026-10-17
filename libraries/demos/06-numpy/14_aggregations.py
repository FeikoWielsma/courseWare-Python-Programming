import numpy as np

latency = np.array([12.1, 9.8, 14.0, 210.5, 11.2, 13.7, 480.0, 10.9, 12.4, 195.3])

print("count :", latency.size)
print("total :", round(float(latency.sum()), 1))
print("mean  :", round(float(latency.mean()), 1))
print("min   :", latency.min(), "max :", latency.max())
print("stdev :", round(float(latency.std()), 1))

# argmax gives the position, not the value, which is usually the more useful
# answer : it says which probe, not just how bad.
print("worst :", int(np.argmax(latency)))

# A mean is a poor summary of a skewed measurement. Percentiles are not.
print("mean  :", round(float(latency.mean()), 1))
print("median:", round(float(np.median(latency)), 1))
print("p95   :", round(float(np.percentile(latency, 95)), 1))

# Every reduction is available as a method and as a function; pick one.
print(latency.sum() == np.sum(latency))
