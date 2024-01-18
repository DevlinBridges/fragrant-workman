import matplotlib.pyplot as plt
import numpy as np

dist = np.random.uniform(1,2,10000)

count, bins, ignored = plt.hist(dist, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=1, color='skyblue')
plt.title("Histogram of Uniform Dist.")
plt.show()
