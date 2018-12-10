from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
import mpl_toolkits.mplot3d as a3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""
#Planned trayectory
"""
p = np.array([[-119.5037579,  -115.36011515, -944.52962352], #p[0]
              [-114.07800378, -122.0185057,  -956.22655749], #p[1]
              [-118.00648661, -115.04101155, -960.69477464], #p[2]

              [ -51.81599414,  -25.89100708, -943.24303368], #p[3]
              [ -43.26938473,  -31.08287261, -960.56354175], #p[4]
              [ -60.36260355,  -20.69914155, -960.56354175]]) #p[5]

ax.scatter3D(p[:, 0], p[:, 1], p[:, 2])

x = np.array([[-119.5037579], [-114.07800378], [-118.00648661], [-51.81599414],[-43.26938473], [-60.36260355]])
y = np.array([[-115.36011515], [-122.0185057], [-115.04101155], [ -25.89100708], [-31.08287261], [-20.69914155]])
z = np.array([[-944.52962352], [-956.22655749], [-960.69477464], [-943.24303368], [-960.56354175], [-960.56354175]])

labels = ['PT-EP', 'PT-EP', 'PT-EP', 'PT-TP', 'PT-TP', 'PT-TP']

x = x.flatten()
y = y.flatten()
z = z.flatten()

ax.scatter(x, y, z)
#give the labels to each point
for x, y, z, label in zip(x, y,z, labels):
    ax.text(x, y, z, label)


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

x2 = np.array([[-117.80799414], [-109.67199414], [-116.90399414], [-46.39199414], [-39.15999414], [-55.43199414]])
y2 = np.array([[ -113.57900708], [-115.38700708], [-113.57900708], [-13.23500708], [-25.89100708],[-12.33100708]])
z2 = np.array([[-943.58935547], [-953.18994141], [-959.59033203], [-940.38916016], [-957.19018555],[-959.59033203]])

labels2= ['VT-EP', 'VT-EP', 'VT-EP', 'VT-TP', 'VT-TP', 'VT-TP']

x2 = x2.flatten()
y2 = y2.flatten()
z2 = z2.flatten()

ax.scatter(x2, y2, z2)

#give the labels to each point
for x2, y2, z2, label2 in zip(x2, y2,z2, labels2):
    ax.text(x2, y2, z2, label2)

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


collection = Poly3DCollection(verts, linewidths=1, edgecolors='black', alpha=0.2)
face_color = "salmon"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

plt.show()