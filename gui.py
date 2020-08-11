#PWM slider
import pyfirmata
from tkinter import *

import time
board = pyfirmata.Arduino("/dev/ttyACM0")
it = pyfirmata.util.Iterator(board)
it.start()

servo = board.get_pin('d:11:s')


class App:
    


        
    

    def __init__(self, master):
        frame = Frame(master)
        
        
        scale1 = Scale(from_=0, to=180,
              orient=HORIZONTAL, command=self.joint1,label="joint1",activebackground="green")
        scale1.place(x = 250,y = 0)
                   
        scale2 = Scale(from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint2,label="joint2",activebackground="green")
        scale2.place(x = 250,y = 50)

        
                  
        scale3 = Scale(from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint3,label="joint3",activebackground="green")
        scale3.place(x = 250,y = 100)

        
                  
        scale4 = Scale(from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint4,label="joint4",activebackground="green")
        scale4.place(x = 250,y = 150)
        
        scale5 = Scale(from_=0, to=180,
              orient= VERTICAL, command=self.joint5,label="gripper",activebackground="green",length=200)
        scale5.place(x = 370,y = 0)
        
        yPlus = Button(text ="Y+")
        yPlus.place(x = 280,y = 250)#command=smth
        
        yMinus = Button(text ="Y-")
        yMinus.place(x = 280,y = 300)#command=smth
        
        xPlus = Button(text ="X+")
        xPlus.place(x = 330,y = 275)#command=smth
        
        xMinus = Button(text ="X-")
        xMinus.place(x = 230,y = 275)#command=smth
        
        zPlus = Button(text ="Z+")
        zPlus.place(x = 330,y = 350)#command=smth
        
        zMinus = Button(text ="Z-")
        zMinus.place(x = 230,y = 350)#command=smth
        
        
        Home = Button(text ="Home")
        Home.place(x = 0,y = 350)#command=smth
        
        Lposition = Label(text="Enter position")
        Lposition.place(x=0,y=310)
        
        position = Entry()
        position.place(x = 0,y = 330)
        
        go2position = Button(text ="Go to position",command=self.gtposition(position))
        go2position.place(x = 70,y = 330)#command=smth
        
        
        
    def gtposition(self,position):
        print (position.get())
    
    def joint1(self, angle):
        servo.write(angle)
        
        q1= angle
        print ("q1 is",q1)
       
         
    def joint2(self, angle):
       
        
        q2= angle
        print ("q2 is",q2)
       
         
    def joint3(self, angle):
        
        q3= angle
        print ("q3 is",q3)
       
         
    def joint4(self, angle):
        
        q4=angle
        print ("q4 is",q4)
        
       
    def joint5(self, angle):
        
        q5=angle
        print ("q5 is",q5)     
    
        
root = Tk()
root.wm_title('Joint Control')
app = App(root)
root.geometry("600x600+650+250")
root.mainloop()
