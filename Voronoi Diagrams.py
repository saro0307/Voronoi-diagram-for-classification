
import sys
print("python version is: ", sys.version)

import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]])

plt.scatter(points[:,0], points[:,1])

#Create voronoi object
vor = Voronoi(points)

#Get voronoi vertices
vor_vertices = vor.vertices
print(vor_vertices)

#Get voronoi regions
vor_regions = vor.regions
print(vor_regions) #Each sub-list contains the coordinates for the regions

#Use built in function to plot
fig = voronoi_plot_2d(vor)
plt.show()


# generating a few random coordinates
coords = np.random.rand(10, 2) 
vor2 = Voronoi(coords)

plt.scatter(coords[:,0], coords[:,1])

fig2 = voronoi_plot_2d(vor2)
plt.show()

# How can Voronoi help with image segmentation?
# What if we can find object centers and use them as seeds for Voronoi?
#Then threshold objects withing each voronoi region?
#This is an easy to segment objects.

from skimage import io, filters # type: ignore

img = io.imread('temp.jpg')

plt.imshow(img, cmap='gray')
plt.axis('off')

# Gaussian blur to averagelocal intensity variations
img_blurred = filters.gaussian(img, sigma=5)
plt.imshow(img_blurred, cmap='gray')
plt.axis('off')

# Find the points representing each object, to be used for Voronoi
from skimage.feature import peak_local_max
coordinates = peak_local_max(img_blurred, min_distance=20, 
                             exclude_border=False)

plt.imshow(img_blurred, cmap='gray')
plt.plot(coordinates[:, 1], coordinates[:, 0], 'r.')
plt.axis('off')

# Vronoi regions
vor3 = Voronoi(coordinates)

fig3 = voronoi_plot_2d(vor3)
plt.axis('off')
plt.show()
