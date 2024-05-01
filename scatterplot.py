import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV
df = pd.read_csv('functions_data.csv')

# Mapping colors and markers
colors = {'enc': 'red', 'ser': 'green', 'com': 'blue'}
markers = {'mongod': 'o', 'nginx': 's', 'other': '^'}  # Circle for mongod, square for nginx, triangle for others

# Plotting
plt.figure(figsize=(10, 6))
type_objects = {}  # To store plot objects for type legend
service_objects = {}  # To store plot objects for micro-service-type legend

for (mstype, mtype), group in df.groupby(['micro-service-type', 'type']):
    label_type = f"{mtype}" if mtype not in type_objects else "_nolegend_"  # Avoid duplicate legend entries
    label_mstype = f"{mstype}" if mstype not in service_objects else "_nolegend_"
    
    plot_object = plt.scatter(group['cc/cluster'], group['bytes/cluster'], color=colors[mtype], marker=markers[mstype], label=label_type)
    if label_type != "_nolegend_":
        type_objects[mtype] = plot_object
    if label_mstype != "_nolegend_":
        service_objects[mstype] = plot_object

# Create legends
type_legend = plt.legend(type_objects.values(), type_objects.keys(), title='Type', loc='upper right')
plt.gca().add_artist(type_legend)  # Add the first legend manually
service_legend = plt.legend(service_objects.values(), service_objects.keys(), title='Micro-Service-Type', loc='lower right')
# Set the legend marker face color to black for micro-service-type
for legend_handle in service_legend.legendHandles:
    legend_handle.set_color('black')

# Adding labels and title
plt.xlabel('Clock Cycles per Cluster (cc/cluster)')
plt.ylabel('Bytes per Cluster (bytes/cluster)')
plt.title('Scatter Plot of Functions by Type and Micro-Service')
plt.grid(True)

# Save the plot to a file
plt.savefig('function_type_microservice_plot.png')

# Display the plot
plt.show()
