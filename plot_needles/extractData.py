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

#df['col_3'] = df[['col_1','col_2']].apply(lambda x: f(*x), axis=1)

#new_df = f.PlannedEntryPoint.apply(lambda x: [x.split(' ') for x in f.PlannedEntryPoint])

new_df_PlannedEntryPoint = f.PlannedEntryPoint.str.split(" ", n=2, expand=True)
new_df_PlannedTargetPoint = f.PlannedTargetPoint.str.split(" ", n=2, expand=True)
new_df_ValidationEntryPoint = f.ValidationEntryPoint.str.split(" ", n=2, expand=True)
new_df_ValidationTargetPoint = f.ValidationTargetPoint.str.split(" ", n=2, expand=True)

print(new_df_PlannedTargetPoint)
# f['EP_x'] = new_df[0]
# f[['EP_x', 'EP_y', 'EP_z']] = new_df
# print()
"""
plannedEntryPointSeries1 = pd.Series(plannedEntryPointReplace1)
plannedEntryPointSeries2 = pd.Series(plannedEntryPointReplace2)
plannedEntryPointSeries3 = pd.Series(plannedEntryPointReplace3)

plannedEntryPointDataFrame1= pd.DataFrame([x.split(' ') for x in plannedEntryPointSeries1.tolist()])
plannedEntryPointDataFrame2= pd.DataFrame([x.split(' ') for x in plannedEntryPointSeries2.tolist()])
plannedEntryPointDataFrame3= pd.DataFrame([x.split(' ') for x in plannedEntryPointSeries3.tolist()])

#Preparing Planned Target Point

plannedTargetPointSeries1 = pd.Series(plannedTargetPointReplace1)
plannedTargetPointSeries2 = pd.Series(plannedTargetPointReplace2)
plannedTargetPointSeries3 = pd.Series(plannedTargetPointReplace3)

plannedTargetPointDataFrame1= pd.DataFrame([x.split(' ') for x in plannedTargetPointSeries1.tolist()])
plannedTargetPointDataFrame2= pd.DataFrame([x.split(' ') for x in plannedTargetPointSeries2.tolist()])
plannedTargetPointDataFrame3= pd.DataFrame([x.split(' ') for x in plannedTargetPointSeries3.tolist()])

#Preparing Validation Entry Point

validationEntryPointSeries1 = pd.Series(validationEntryPointReplace1)
validationEntryPointSeries2 = pd.Series(validationEntryPointReplace2)
validationEntryPointSeries3 = pd.Series(validtaionEntryPointReplace3)

validationEntryPointDataFrame1= pd.DataFrame([x.split(' ') for x in validationEntryPointSeries1.tolist()])
validationEntryPointDataFrame2= pd.DataFrame([x.split(' ') for x in validationEntryPointSeries2.tolist()])
validationEntryPointDataFrame3= pd.DataFrame([x.split(' ') for x in validationEntryPointSeries3.tolist()])

#Preparing Validation Target Point

validationTargetPointSeries1 = pd.Series(validationTargetPointReplace1)
validationTargetPointSeries2 = pd.Series(validationTargetPointReplace2)
validationTargetPointSeries3 = pd.Series(validtaionTargetPointReplace3)

validationTargetPointDataFrame1= pd.DataFrame([x.split(' ') for x in validationTargetPointSeries1.tolist()])
validationTargetPointDataFrame2= pd.DataFrame([x.split(' ') for x in validationTargetPointSeries2.tolist()])
validationTargetPointDataFrame3= pd.DataFrame([x.split(' ') for x in validationTargetPointSeries3.tolist()])

new_df = [validationTargetPointDataFrame1, validationEntryPointDataFrame2, validationTargetPointDataFrame2]
print("concatenate dataframes", new_df)

p = np.concatenate([plannedEntryPointNPArray1, plannedEntryPointNPArray2, plannedEntryPointNPArray3, plannedTargetPointNPArray1, plannedTargetPointNPArray2, plannedTargetPointNPArray3 ])
v = np.concatenate([validationEntryPointDataFrame1, validationEntryPointDataFrame2,validationEntryPointDataFrame3, validationTargetPointDataFrame1,validationTargetPointDataFrame2, validationTargetPointDataFrame3])

"""
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# ax.scatter3D(p[:,0], p[:,1], p[:,2])
# ax.scatter3D(v[:,0], v[:,1], v[:,2])
#
# verts = [[p[0],p[1],p[2]],
#           [p[0],p[2],p[5], p[3]],
#           [p[1],p[4],p[5], p[2]],
#           [p[3],p[4],p[5]],
#           [p[0],p[1],p[4], p[3]],
#
#           [v[0],v[1],v[2]],
#           [v[0],v[2],v[5], v[3]],
#           [v[1],v[4],v[5], v[2]],
#           [v[3],v[4],v[5]],
#           [v[0],v[1],v[4], v[3]]
#          ]
#
# collection = Poly3DCollection(verts, linewidths=1, edgecolors='black', alpha=0.2)
# face_color = "salmon"
# collection.set_facecolor(face_color)
# ax.add_collection3d(collection)
#
# plt.show()
