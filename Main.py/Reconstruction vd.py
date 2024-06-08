import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

# Generate some random points
np.random.seed(0)
points = np.random.rand(8, 2)

# Create a Voronoi diagram
vor = Voronoi(points)

# Plot the Voronoi diagram
fig, ax = plt.subplots(figsize=(8, 6))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='r', line_width=2)

# Plot the points
ax.plot(points[:, 0], points[:, 1], 'ko')

# Set plot limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Reconstructed Image')

plt.show()