#PWM slider
import pyfirmata
from tkinter import *

import time
bg="#272729"
fbg="#369bb5"
'''
board = pyfirmata.Arduino("/dev/ttyACM1")
it = pyfirmata.util.Iterator(board)
it.start()

servo1 = board.get_pin('d:11:s')

#servo2 = board.get_pin('d:11:s')
#servo3 = board.get_pin('d:11:s')
#servo4 = board.get_pin('d:11:s')
#servo5 = board.get_pin('d:11:s') 
'''
repeat =[]

class App:
    


        
    

    def __init__(self, master):
        frame = Frame(master)
        self.up = PhotoImage(file = "imgs/up.png")
        self.down = PhotoImage(file = "imgs/down.png")
        self.right = PhotoImage(file = "imgs/right.png")
        self.left = PhotoImage(file = "imgs/left.png")
        self.home = PhotoImage(file = "imgs/home.png")
        
        scale1 = Scale(from_=0, to=180,
              orient=HORIZONTAL, command=self.joint1,label="joint1",activebackground=fbg,bg=bg,length=200)
        scale1.place(x = 200,y = 0)
                   
        scale2 = Scale(from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint2,label="joint2",activebackground=fbg,bg=bg,length=200)
        scale2.place(x = 200,y = 50)

        
                  
        scale3 = Scale(from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint3,label="joint3",activebackground=fbg,bg=bg,length=200)
        scale3.place(x = 200,y = 100)

        
                  
        scale4 = Scale(from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint4,label="joint4",activebackground=fbg,bg=bg,length=200)
        scale4.place(x = 200,y = 150)
        
        scale5 = Scale(from_=0, to=180,
              orient= VERTICAL, command=self.joint5,label="gripper",activebackground=fbg,bg=bg,length=200)
        scale5.place(x = 420,y = 0)
        
        
        yPlus = Button(text ="Y+", image = self.up,bg=bg)
        yPlus.place(x = 280,y = 250)#command=smth
        
        yMinus = Button(text ="Y-", image = self.down,bg=bg)
        yMinus.place(x = 280,y = 370)#command=smth
        
        xPlus = Button(text ="X+", image = self.right,bg=bg)
        xPlus.place(x = 340,y = 310)#command=smth
        
        xMinus = Button(text ="X-", image = self.left,bg=bg)
        xMinus.place(x = 220,y = 310)#command=smth
        
        zPlus = Button(text ="Z+",image = self.up,bg=bg)
        zPlus.place(x = 420,y = 250)#command=smth
        
        zMinus = Button(text ="Z-", image = self.down,bg=bg)
        zMinus.place(x = 420,y = 370)#command=smth
        
        
        
        Home = Button(text ="Home",bg=bg,activebackground=fbg,image = self.home)
        Home.place(x = 0,y = 370)#command=smth
        
        
        position = Entry(bg=bg)
        position.place(x = 0,y = 330)
        
        go2position = Button(text ="Go to position",command=self.gtposition(position),bg=bg,activebackground="#369bb5")
        go2position.place(x = 90,y = 325)#command=smth
        
        repeat = Button(text ="repeat",command=self.repeatit,bg=bg,activebackground="#369bb5")
        repeat.place(x = 500,y = 500 )
        
        reset = Button(text ="reset",command=self.resetit,bg=bg,activebackground="red")
        reset.place(x = 450,y = 500 )
        
        
        Lposition = Label(text="Enter position",bg=bg)
        Lposition.place(x=0,y=310)
        
        
        xy = Label(text="XY",bg=bg)
        xy.place(x=300,y=330)
        
        z = Label(text="Z",bg=bg)
        z.place(x=440,y=330)
        
        
    def gtposition(self,position):
        print (position.get())
    
    def joint1(self, angle):
        servo1.write(angle)
        q1= angle
        repeat.append([servo1,q1])
        print ("q1 is",q1)
       
         
    def joint2(self, angle):
       
        
        q2= angle
        repeat.append([servo2,q2])
        print ("q2 is",q2)
       
         
    def joint3(self, angle):
        
        q3= angle
        repeat.append([servo3,q3])
        print ("q3 is",q3)
       
         
    def joint4(self, angle):
        
        q4=angle
        repeat.append([servo4,q4])
        print ("q4 is",q4)
        
       
    def joint5(self, angle):
        
        q5=angle
        repeat.append([servo5,q5])
        print ("q5 is",q5)     
    
    def repeatit(self):
        for i in repeat:
            i[0].write(i[1])
            time.sleep(.03)
            print (i[1])
        
     
    def resetit(self):
        
        repeat.clear()
        
root = Tk()
root.wm_title('Joint Control')
app = App(root)
root.geometry("600x600+650+250")
root.configure(background=bg)

root.mainloop()
