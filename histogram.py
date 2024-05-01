import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV
df = pd.read_csv('functions_data.csv')

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(df['bytes/cluster'], bins=20, color='blue', edgecolor='black')  # 20 bins for demonstration, adjust as needed

# Adding titles and labels
plt.title('Frequency Plot of Bytes per Cluster')
plt.xlabel('Bytes per Cluster')
plt.ylabel('Frequency')

# Show grid
plt.grid(True)

# Save the plot to a file
plt.savefig('bytes_per_cluster_frequency.png')

# Display the plot
plt.show()
