# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:15:32 2018

@author: Trinidad Castillo
"""
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

file = 'test_pacient_for_draw.xlsx'
f= pd.read_excel(file)

##%%
f.PlannedEntryPoint = f.PlannedEntryPoint.apply(lambda x: x.replace('  ', ' ').replace('[', '').replace(']', ''))
f.PlannedTargetPoint = f.PlannedTargetPoint.apply(
    lambda x: x.replace('[ ', '[').replace('  ', ' ').replace('[', '').replace(']', ''))
f.ValidationEntryPoint = f.ValidationEntryPoint.apply(lambda x: x.replace('  ', ' ').replace('[', '').replace(']', ''))
f.ValidationTargetPoint = f.ValidationTargetPoint.apply(
    lambda x: x.replace('[ ', '[').replace('  ', ' ').replace('[', '').replace(']', ''))

new_df_PlannedEntryPoint = f.PlannedEntryPoint.str.split(" ", n=2, expand=True)
new_df_PlannedTargetPoint = f.PlannedTargetPoint.str.split(" ", n=2, expand=True)
new_df_ValidationEntryPoint = f.ValidationEntryPoint.str.split(" ", n=2, expand=True)
new_df_ValidationTargetPoint = f.ValidationTargetPoint.str.split(" ", n=2, expand=True)

p = new_df_PlannedEntryPoint.append(new_df_PlannedTargetPoint, ignore_index=True)
p = p.astype(float)

v = new_df_ValidationEntryPoint.append(new_df_ValidationTargetPoint, ignore_index=True)
v = v.astype(float)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(p[0], p[1], p[2])
ax.scatter3D(v[0], v[1], v[2])

verts = [[p.loc[0],p.loc[1],p.loc[2]],
          [p.loc[0],p.loc[2],p.loc[5],p.loc[3]],
          [p.loc[1],p.loc[4],p.loc[5], p.loc[2]],
          [p.loc[3],p.loc[4],p.loc[5]],
          [p.loc[0],p.loc[1],p.loc[4], p.loc[3]],

          [v.loc[0],v.loc[1],v.loc[2]],
          [v.loc[0],v.loc[2],v.loc[5],v.loc[3]],
          [v.loc[1],v.loc[4],v.loc[5],v.loc[2]],
          [v.loc[3],v.loc[4],v.loc[5]],
          [v.loc[0],v.loc[1],v.loc[4],v.loc[3]]]

x = np.array(p[0])
y = np.array(p[1])
z = np.array(p[2])

labels = ['PT-EP', 'PT-EP', 'PT-EP', 'PT-TP', 'PT-TP', 'PT-TP']

x = x.flatten()
y = y.flatten()
z = z.flatten()

ax.scatter(x, y, z)
#give the labels to each point
for x, y, z, label in zip(x, y,z, labels):
    ax.text(x, y, z, label)

x2 = np.array(v[0])
y2 = np.array(v[1])
z2 = np.array(v[2])

labels2= ['VT-EP', 'VT-EP', 'VT-EP', 'VT-TP', 'VT-TP', 'VT-TP']

x2 = x2.flatten()
y2 = y2.flatten()
z2 = z2.flatten()

ax.scatter(x2, y2, z2)

#give the labels to each point
for x2, y2, z2, label2 in zip(x2, y2,z2, labels2):
    ax.text(x2, y2, z2, label2)

collection = Poly3DCollection(verts, linewidths=1, edgecolors='black', alpha=0.2)
face_color = "salmon"
collection.set_facecolor(face_color)
ax.add_collection3d(collection)

plt.show()
