import matplotlib.pyplot as plt
import numpy as np

# Create list of number of samples to run in loop
num = [1, 5, 10, 100]  
# Empty list of means to append to so we can plot histogram
means = []  
 
# Generating 1, 5, 10, 100 random numbers from 0 to 100
# Mean is appended to list
for n in num:
    # Generating seed so that we can get same result 
    np.random.seed(1)
    x = [np.mean(
        np.random.randint(
            0, 100, n)) for _i in range(1000)]
    means.append(x)
k = 0
 
# Histograms are plotted
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for n in range(0, 2):
        # Histogram for each x stored in means
        ax[i, n].hist(means[k], 10, density = True)
        ax[i, n].set_title(label = num[k])
        k = k + 1
plt.show()
