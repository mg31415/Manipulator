#frames visualization
import plotly.graph_objects as go
import numpy as np
import pandas as pd

p0=np.array([0,0,0])
p1=np.around(T0_1[:3,3:4])
p2=np.around(T0_2[:3,3:4])
p3=np.around(T0_3[:3,3:4])
p4=np.around(T0_4[:3,3:4])

x=[int(p0[0]),int(p1[0]),int(p2[0]),int(p3[0]),int(p4[0])]
y=[int(p0[1]),int(p1[1]),int(p2[1]),int(p3[1]),int(p4[1])]
z=[int(p0[2]),int(p1[2]),int(p2[2]),int(p3[2]),int(p4[2])]

print ("End effector: ",x[4],y[4],z[4])
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z)])
fig.show() 
