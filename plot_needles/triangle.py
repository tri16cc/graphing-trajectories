from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
import mpl_toolkits.mplot3d as a3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax2 = fig.add_subplot(111, projection='3d')
"""
#PARA UNA PIRAMIDE DE BASE RECTANGULAR

# vertices of a pyramid
v = np.array([[-1, -1, -1], #v[0]
              [1, -1, -1], #v[1]
              [1, 1, -1], #v[2]
              [-1, 1, -1], #v[3]
              [0, 0, -2]]) #v[4]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[4]],
          [v[0],v[3],v[4]],
          [v[2],v[1],v[4]],
          [v[2],v[3],v[4]],
          [v[0],v[1],v[2],v[3]]]
"""
"""
#PARA UNA PIRAMIDE DE BASE TRIANGULAR
v = np.array([[1, -1, -1], #v[0]
              [1, 1, -1], #v[1]
              [-1, 1, -1], #v[2]
              [0, 0, 1]]) #v[3]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[3]],
          [v[0],v[2],v[3]],
          [v[1],v[2],v[3]],
          [v[0],v[1],v[2]]]
"""
"""
#PARA UN PRISMA TRIANGULAR CON BASE TRIANGULAR


"""
v = np.array([[-119.5037579,  -115.36011515, -944.52962352], #v[0]
              [-114.07800378, -122.0185057,  -956.22655749], #v[1]
              [-118.00648661, -115.04101155, -960.69477464], #v[2]

              [ -51.81599414,  -25.89100708, -943.24303368], #v[3]
              [ -43.26938473,  -31.08287261, -960.56354175], #v[4]
              [ -60.36260355,  -20.69914155, -960.56354175]]) #v[5]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[2]],
          [v[0],v[2],v[5], v[3]],
          [v[1],v[4],v[5], v[2]],
          [v[3], v[4], v[5]],
          [v[0],v[1],v[4], v[3]]]

collection = Poly3DCollection(verts, linewidths=1, edgecolors='black', alpha=0.2)
face_color = "aquamarine"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

# v2 = np.array([[-119.5037579,  -115.36011515, -944.52962352], #v[0]
#               [-114.07800378, -122.0185057,  -956.22655749], #v[1]
#               [-118.00648661, -115.04101155, -960.69477464], #v[2]
#
#               [ -51.81599414,  -25.89100708, -943.24303368], #v[3]
#               [ -43.26938473,  -31.08287261, -960.56354175], #v[4]
#               [ -60.36260355,  -20.69914155, -960.56354175]]) #v[5]
#
# ax2.scatter3D(v2[:, 0], v2[:, 1], v2[:, 2])
#
# # generate list of sides' polygons of our pyramid
# verts2 = [ [v[0],v[1],v[2]],
#           [v[0],v[2],v[5], v[3]],
#           [v[1],v[4],v[5], v[2]],
#           [v[3], v[4], v[5]],
#           [v[0],v[1],v[4], v[3]]]
#
# collection2 = Poly3DCollection(verts2, linewidths=1, edgecolors='black', alpha=0.2)
# face_color2 = [1, 1, 1]
# collection.set_facecolor(face_color2)
# ax2.add_collection3d(collection2)


#plt.tight_layout()
plt.show()


"""
#PARA DOS VOLUMENES EN EL MISMO GRAFICO
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#PARA UNA PIRAMIDE DE BASE RECTANGULAR

# vertices of a pyramid
v = np.array([[-1, -1, -1], #v[0]
              [1, -1, -1], #v[1]
              [1, 1, -1], #v[2]
              [-1, 1, -1], #v[3]
              [0, 0, 1]]) #v[4]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

t = np.array([[-1, -1, -1], #v[0]
              [1, -1, -1], #v[1]
              [1, 1, -1], #v[2]
              [-1, 1, -1], #v[3]
              [0, 0, 2]]) #v[4]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
ax.scatter3D(t[:, 0], t[:, 1], t[:, 2])


# generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[4]],
          [v[0],v[3],v[4]],
          [v[2],v[1],v[4]],
          [v[2],v[3],v[4]],
          [v[0],v[1],v[2],v[3]],
          [t[0],t[1],t[4]],
          [t[0],t[3],t[4]],
          [t[2],t[1],t[4]],
          [t[2],t[3],t[4]],
          [t[0],t[1],t[2],t[3]]
          ]


collection = Poly3DCollection(verts, linewidths=1, edgecolors='black', alpha=0.2)
face_color = "aquamarine"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

plt.show()


"""