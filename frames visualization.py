#packages
import numpy as np
from numpy.linalg import multi_dot
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as py
from ipywidgets import interactive, HBox, VBox
py.init_notebook_mode()


#angle values
q=["some times arrays are better started at 1",0,45,0,0]

a1,a2,a3,a4=3,8,9,10

t0=[0,0,0] #zero vector


#Transformation of Rotation around x || y || z functions

def TRX(phi,t):
    phi= phi*np.pi/180
    TRX=np.array([[1,0,0,t[0]],[0,np.cos(phi),-np.sin(phi),t[1]],[0,np.sin(phi),np.cos(phi),t[2]],[0,0,0,1]])
    return TRX

def TRY(phi,t):
    phi= phi*np.pi/180
    TRY=np.array([[np.cos(phi),0,np.sin(phi),t[0]],[0,1,0,t[1]],[-np.sin(phi),0,np.cos(phi),t[2]],[0,0,0,1]])
    return TRY


def TRZ(phi,t):
    phi= phi*np.pi/180
    TRZ=np.array([[np.cos(phi),-np.sin(phi),0,t[0]],[np.sin(phi),np.cos(phi),0,t[1]],[0,0,1,t[2]],[0,0,0,1]])
    return TRZ
#_______________________________________________________________

#TRZ(q1,[0,0,a1]) . TRX(90,t0) . TRZ(q2,[a2,0,0]) . TRZ(q3,t0) . TRX(90,t0) . TRZ(q4,[a3+a4,0,0])




def zxy():
    
    T0_1=TRZ(q[1],[0,0,a1])@TRX(90,t0)
    T0_2=TRZ(q[1],[0,0,a1])@TRX(90,t0)@TRZ(q[2],[a2,0,0])
    T0_3=TRZ(q[1],[0,0,a1])@TRX(90,t0)@TRZ(q[2],[a2,0,0])@TRZ(q[3],t0)@TRX(90,t0)
    T0_4=TRZ(q[1],[0,0,a1])@TRX(90,t0)@TRZ(q[2],[a2,0,0])@TRZ(q[3],t0)@TRX(90,t0)@TRZ(q[4],[a3+a4,0,0])
    
    p0=np.array([0,0,0])
    p1=np.around(T0_1[:3,3:4])
    p2=np.around(T0_2[:3,3:4])
    p3=np.around(T0_3[:3,3:4])
    p4=np.around(T0_4[:3,3:4])

    x=[int(p0[0]),int(p1[0]),int(p2[0]),int(p3[0]),int(p4[0])]
    y=[int(p0[1]),int(p1[1]),int(p2[1]),int(p3[1]),int(p4[1])]
    z=[int(p0[2]),int(p1[2]),int(p2[2]),int(p3[2]),int(p4[2])]
    return z,x,y
    


#frames visualization

f = go.FigureWidget(
    data=[
        go.Scatter3d(z=zxy()[0], x=zxy()[1], y=zxy()[2])],
    layout=go.Layout(scene=go.layout.Scene(
        camera=go.layout.scene.Camera(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.25, y=1.25, z=1.25))
    ))
)






def update_q1(q1):
    q[1]=q1
    f.data[0].z=zxy()[0]
    f.data[0].x=zxy()[1]
    f.data[0].y=zxy()[2]
def update_q2(q2):
    q[2]=q2
    f.data[0].z=zxy()[0]
    f.data[0].x=zxy()[1]
    f.data[0].y=zxy()[2]
def update_q3(q3):
    q[3]=q3
    f.data[0].z=zxy()[0]
    f.data[0].x=zxy()[1]
    f.data[0].y=zxy()[2]
    

def update_q4(q4):
    q[4]=q4
    f.data[0].z=zxy()[0]
    f.data[0].x=zxy()[1]
    f.data[0].y=zxy()[2]

    
q1_slider = interactive(update_q1, q1=(0, 180, 0.01))
q2_slider = interactive(update_q2, q2=(0, 180, 0.01))
q3_slider = interactive(update_q3, q3=(0, 180, 0.01))
q4_slider = interactive(update_q4, q4=(0, 180, 0.01))

vb = VBox((f, q1_slider,q2_slider,q3_slider,q4_slider))
vb.layout.align_items = 'center'
vb


