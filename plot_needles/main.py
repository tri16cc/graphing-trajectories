from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
import mpl_toolkits.mplot3d as a3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""
#Planned trayectory
"""
p = np.array([[-119.5037579,  -115.36011515, -944.52962352], #v[0]
              [-114.07800378, -122.0185057,  -956.22655749], #v[1]
              [-118.00648661, -115.04101155, -960.69477464], #v[2]

              [ -51.81599414,  -25.89100708, -943.24303368], #v[3]
              [ -43.26938473,  -31.08287261, -960.56354175], #v[4]
              [ -60.36260355,  -20.69914155, -960.56354175]]) #v[5]

ax.scatter3D(p[:, 0], p[:, 1], p[:, 2])

"""
# Validation 
"""

v = np.array([[-117.80799414, -113.57900708, -943.58935547], #v[0]
              [-109.67199414, -115.38700708, -953.18994141], #v[1]
              [-116.90399414, -113.57900708, -959.59033203], #v[2]

              [-46.39199414, -13.23500708, -940.38916016], #v[3]
              [-39.15999414, -25.89100708, -957.19018555], #v[4]
              [-55.43199414, -12.33100708, -959.59033203]]) #v[5]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])


# generate list of sides' polygons of our pyramid
verts = [[p[0],p[1],p[2]],
          [p[0],p[2],p[5], p[3]],
          [p[1],p[4],p[5], p[2]],
          [p[3],p[4],p[5]],
          [p[0],p[1],p[4], p[3]],

          [v[0],v[1],v[2]],
          [v[0],v[2],v[5], v[3]],
          [v[1],v[4],v[5], v[2]],
          [v[3],v[4],v[5]],
          [v[0],v[1],v[4], v[3]]]


collection = Poly3DCollection(verts, linewidths=3, edgecolors='black', alpha=0.2)
face_color = "salmon"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

plt.show()