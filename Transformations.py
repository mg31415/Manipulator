#packages
import numpy as np
from numpy.linalg import multi_dot
#angle values
q1,q2,q3,q4=0,0,0,0
a1,a2,a3,a4=7,8,9,10

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


T0_1=TRZ(q1,[0,0,a1])@TRX(90,t0)
T0_2=TRZ(q1,[0,0,a1])@TRX(90,t0)@TRZ(q2,[a2,0,0])
T0_3=TRZ(q1,[0,0,a1])@TRX(90,t0)@TRZ(q2,[a2,0,0])@TRZ(q3,t0)@TRX(90,t0)
T0_4=TRZ(q1,[0,0,a1])@TRX(90,t0)@TRZ(q2,[a2,0,0])@TRZ(q3,t0)@TRX(90,t0)@TRZ(q4,[a3+a4,0,0])


print (np.around(T0_4)) 
