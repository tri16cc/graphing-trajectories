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



#5 needles



"""
#Planned trayectory
"""
p = np.array([[-144.70863101, -33.32654023, -1098.88832816], #p[0]
              [-149.969178, -18.24246092, -1086.48015701], #p[1]
              [-155.89005285, -21.67872293, -1078.74752773], #p[2]
              [-156.24165565, -44.28886924, -1060.75708391], #p[3]
              [-152.65669137, -53.07220511, -1092.28357803], #p[4]


              [-46.79794737, -30.4821252, -1019.8614917], #p[5]
              [-55.92692704, -11.40747771, -1009.58501575], #p[6]
              [-69.76160181, -18.56203255, -991.97250531], #p[7]
              [-69.18292136, -42.0584381, -991.36385119], #p[8]
              [-54.99060242, -49.4254605, -1008.60019269]]) #p[9]

ax.scatter3D(p[:, 0], p[:, 1], p[:, 2])

"""
# Validation 
"""

v = np.array([[-134.85925293, -31.75648499, -1087.99938965], #v[0]
                [-136.88926697, -14.46294022, -1072.25891113], #v[1]
                [-138.96415222, -21.06623441, -1062.76603818], #v[2]
                [-143.31542534, -45.94221079, -1052.43246193], #v[3]
                [-134.76943994, -52.1731559, -1076.53046644], #v[4]

                [-34.10387421, -28.54125595, -1006.08172607], #v[5]
                [-40.03656793, -8.79592699, -994.78931147], #v[6]
                [-48.28832567, -17.78498912, -978.39063251], #v[7]
                [-51.56776404, -47.69198403, -977.1163654 ], #v[8]
                [-38.69532394, -49.99339294, -996.80560303]]) #v[9]

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])


# generate list of sides' polygons of our pyramid
verts = [
        [p[0],p[1],p[2],p[3],p[4]],
          [p[0],p[1],p[6], p[5]],
          [p[1],p[2],p[7], p[6]],
          [p[2],p[3],p[8], p[7]],
          [p[3],p[4],p[9], p[8]],
          [p[4],p[0],p[5], p[9]],
          [p[5],p[6],p[7], p[8], p[9]],

          [v[0], v[1], v[2], v[3], v[4]],
          [v[0], v[1], v[6], v[5]],
          [v[1], v[2], v[7], v[6]],
          [v[2], v[3], v[8], v[7]],
          [v[3], v[4], v[9], v[8]],
          [v[4], v[0], v[5], v[9]],
          [v[5], v[6], v[7], v[8], v[9]]]


collection = Poly3DCollection(verts, linewidths=1, edgecolors='black', alpha=0.2)
face_color = "salmon"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

plt.show()