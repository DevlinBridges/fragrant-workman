from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(0, 100, 0.5)

y_axis = poisson.pmf(x_axis, mu=40, loc=10)

plt.plot(x_axis, y_axis)
plt.title("Histogram of Poisson Dist.")

plt.show()
