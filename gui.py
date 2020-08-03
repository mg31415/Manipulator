#PWM slider

from tkinter import *
#import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT)
#pwm = GPIO.PWM(18, 100)
#pwm.start(5)

class App:
    

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        scale1 = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.joint1)
        scale1.grid(row=0)
                   
        scale2 = Scale(frame, from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint2)
        scale2.grid(row=1)

        
                  
        scale3 = Scale(frame, from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint3)
        scale3.grid(row=2)

        
                  
        scale4 = Scale(frame, from_=-90, to=90,
              orient=HORIZONTAL, command=self.joint4)
        scale4.grid(row=3)
        
        
      
          
     
    def joint1(self, angle):
        duty = float(angle) / 10.0 + 2.5
        #pwm.ChangeDutyCycle(duty)
        q1= angle
        print ("q1 is",q1)
       
         
    def joint2(self, angle):
        duty = float(angle) / 10.0 + 2.5
        #pwm.ChangeDutyCycle(duty)
        q2= angle
        print ("q2 is",q2)
       
         
    def joint3(self, angle):
        duty = float(angle) / 10.0 + 2.5
        #pwm.ChangeDutyCycle(duty)
        q3= angle
        print ("q3 is",q3)
       
         
    def joint4(self, angle):
        duty = float(angle) / 10.0 + 2.5
        #pwm.ChangeDutyCycle(duty)
        q4=angle
        print ("q4 is",q4)
        
       
        
        
        

root = Tk()
root.wm_title('Joint Control')
app = App(root)
root.geometry("500x500+0+0")
root.mainloop()
