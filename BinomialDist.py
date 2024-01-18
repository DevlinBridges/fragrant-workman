import matplotlib.pyplot as plt
import numpy as np

n = 10
p = 0.5

dist = np.random.binomial(n, p, 100000)
bins = np.arange(12)

plt.hist(dist, bins, color="skyblue", edgecolor="white") 
plt.title("Histogram of Binomial Dist.")
plt.xlabel("Frequency")
plt.ylabel("Number of Heads")
plt.grid(axis='x', alpha=0.75)
plt.show()
