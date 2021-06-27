from os import pardir
import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT
import serial.tools.list_ports as ports
import serial.tools.list_ports
import serial
from time import sleep
from PIL import Image, ImageTk
from tkinter import Tk, Text, TOP, BOTH, Widget, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry



class quantanx(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("QuantanX Testing GUI")
        self.pack(fill=BOTH, expand=True)

#----------------frame 1 CONNECTION DROPDOWN----------------------------------------
        frame1 = Frame(self)
        frame1.pack(fill=X,pady=20)

        lbl1 = Label(frame1, text="Select the connection",width=23)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        ComList=[]
        ComSelected=tk.StringVar()
        ComSelected.set("connection")
        com_ports = list(ports.comports()) 
# -------------------------------frame 2 CONN STATUS-------------------------------------------
        for i in com_ports:                    
            ComList.append(i.device)

        drop_ComPort=tk.OptionMenu(frame1,ComSelected,*ComList)
        drop_ComPort.pack(fill=X, padx=5, expand=True)

        def CommOn():
            print(ComSelected.get()+" is "+button_on.cget('text'))
            
                #WRITE FUNCTION OF COMMUNICATION ON

        def CommOff():
            print(ComSelected.get()+" is "+button_off.cget('text'))
            
                #WRITE FUNCTION FOR COMMUNICATION OFF


        frame2 = Frame(self)
        frame2.pack(fill=X,pady=5)

        lbl2 = Label(frame2, text="Select Connection Status",width=23)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        button_on=tk.Button(frame2,text="ON",command=CommOn,width=20)
        button_on.pack(side=LEFT, padx=5, expand=True)

        button_off=tk.Button(frame2,text="OFF",command=CommOff,width=20)
        button_off.pack( side=RIGHT, padx=5, expand=True)  

# ---------------------------Frame 3 OPTIONS---------------------------------------------

        frame3 = Frame(self)
        frame3.pack(fill=BOTH,pady=20)

        lbl3 = Label(frame3, text="Select your feedback",width=23)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        def haptic():
            print("haptic")
            # insert code for haptic
        def tactile():
            print("tactile")
            # insert code for tactile
        def temprature():
            print("temprature")
            # insert code for temprature
        def heartbeat():
            print("heartbeat")
            # insert code for heartbeat
        def raindrop():
            print("raindrop")
            # insert code for raindrop
        def hotwater():
            print("hotwater")
            # insert code for hotwater
        def coldwater():
            print("coldwater")
            # insert code for coldwater 

        button_haptic=tk.Button(frame3,text="HAPTIC",command=haptic,width=10)
        button_haptic.pack(fill=X, padx=5,pady=5, expand=True)

        button_tactile=tk.Button(frame3,text="TACTILE",command=tactile,width=10)
        button_tactile.pack(fill=X, padx=5,pady=5, expand=True)

        button_temp=tk.Button(frame3,text="TEMPRATURE FEEDBACK",command=temprature,width=20)
        button_temp.pack(fill=X, padx=5,pady=5, expand=True)

        button_heartbeat=tk.Button(frame3,text="HEART BEAT",command=heartbeat,width=10)
        button_heartbeat.pack(fill=X, padx=5,pady=5, expand=True) 

        button_raindrop=tk.Button(frame3,text="RAIN DROP",command=raindrop,width=10)
        button_raindrop.pack(fill=X, padx=5,pady=5, expand=True) 

        button_hotwater=tk.Button(frame3,text="HOT WATER",command=hotwater,width=10)
        button_hotwater.pack(fill=X, padx=5,pady=5, expand=True)

        button_coldwater=tk.Button(frame3,text="COLD WATER",command=coldwater,width=10)
        button_coldwater.pack(fill=X, padx=5, pady=5,expand=True)

     
def main():

    root = Tk()
    root.iconbitmap('static/QX-logo-2.ico')
    root.geometry("450x450")
    app = quantanx()
    root.mainloop()


if __name__ == '__main__':
    main()
 
