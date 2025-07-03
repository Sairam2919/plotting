import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.normal(0, 1, 300)

# Calculate mean and median for the data
mean = np.mean(data)
median = np.median(data)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.5)

ax.axvline(mean, color='pink', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
ax.axvline(median, color='red', linestyle='--', linewidth=2, label=f'Median: {median:.2f}')

# style the plot
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)
ax.set_title('Histogram with frequency and value', fontsize=18, color='red')
ax.set_xlim(-4, 4)
ax.set_ylim(0, 35)
ax.tick_params(axis='both', labelsize=12)
ax.legend(loc='upper left', fontsize=14)

plt.show()
