import pandas as pd
import matplotlib.pyplot as plt

# Load the parquet file
url = 'https://star.herts.ac.uk/~kuhn/DHV/exercises_problem2.parquet'
data = pd.read_parquet(url)
x = data['var1']
y = data['var3']

# Plot 1: Histogram of a numeric column
column = 'var1'
fig, ax = plt.subplots(figsize=(10,6))
ax.hist(data[column], bins=30, color='blue', edgecolor='black', alpha=0.5)

ax.set_xlabel(column, fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)
ax.set_title(f'Histogram of {column}', fontsize=16)
ax.tick_params(axis='both', labelsize=12)

plt.show()


# Plot 2: Line Plot
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(x, y, color='red', linewidth=2, label='line')

ax.set_xlabel('Var1', fontsize=14)
ax.set_ylabel('Var2', fontsize=14)
ax.set_title('Line plot for data', fontsize=16)
ax.tick_params(axis='both', labelsize=12)
ax.legend(loc='upper left',fontsize=12)

plt.show()
