import matplotlib.pyplot as plt
import numpy as np


national = np.array([-0.23, 0.26, -0.73, -0.41, -0.17, -
                    0.57, 0.74, -0.2, -0.52, -0.42, 0.08, 0, 0.05, 0.1])
own = np.array([-0.39, -0.42, -0.25, 0.36, 2.61, 0.19, -
               0.01, -0.67, 0.7, -0.84, -1.26, -1.08, -1.07, -0.89])
point_label = np.array(["M1", "M2", "M3", "M4", "M5",
                       "M6", "M7", "D1", "D2", "D3", "D4", "D5", "D6", "D7"])

# Generate random data within the range -4 to 4
x = national
y = own

# Determine the quadrant for each data point
quadrants = []
for x_val, y_val in zip(x, y):
    if x_val >= 0 and y_val >= 0:
        quadrants.append(1)  # First quadrant
    elif x_val < 0 and y_val >= 0:
        quadrants.append(2)  # Second quadrant
    elif x_val < 0 and y_val < 0:
        quadrants.append(3)  # Third quadrant
    else:
        quadrants.append(4)  # Fourth quadrant

# Assign colors based on the quadrant
colors = ['red', 'blue', 'green', 'purple']
scatter_colors = [colors[q - 1] for q in quadrants]

# Create the scatter plot
plt.scatter(x, y, c=scatter_colors)

# Add vertical and horizontal lines
plt.axvline(x=0, color='#08807c', linestyle='--')  # Vertical line at x=0
plt.axhline(y=0, color='#08807c', linestyle='--')  # Horizontal line at y=0


plt.xlim(-4, 4)
plt.ylim(-4, 4)


for (xi, yi, pl) in zip(x, y, point_label):
    plt.text(xi, yi, "  "+pl, va='top', ha='left')


# Add labels and title
plt.xlabel('National')
plt.ylabel('Own')
plt.title('Comparison against National and Own averages')

plt.figure(figsize=(16, 8))

# Display the plot
plt.show()
