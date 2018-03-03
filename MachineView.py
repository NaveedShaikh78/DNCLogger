from Tkinter import *
import ttk

root = Tk()
root.attributes('-fullscreen',True)
root.grid_columnconfigure(0, weight=1)

class Machine :
  def __init__(self) :
       self.macCycleCounter= StringVar()
       self.macCycleCount = StringVar()
       self.macOperator = StringVar()

  def setCycleCounter(self,counter) :
       self.macCycleCounter.set(counter)
          
  def setCount(self,count) :
       self.macCycleCount.set(count)
       
  def setCycleOff(self) :
       self.lblstate1.configure(bg="#ff1a1aff1a1a")

  def setCycleOn(self) :
       self.lblstate1.configure(bg="#94FD7C")
       
  def setOperator(self,value) :
       self.macOperator.set(value)

class MachineMainView:
  def __init__(self) :
       countColors=["#ffffcc","#ffdab3","#ccffcc","#ffccff","#ccffff","#ffcccc","#ccccff","#cce4ff"];
       machColors=["#ffffb3","#ffcc99","#b3ffb3","#ffb3ff","#99ffff","#ffb3b3","#b3b3ff","#b3d7ff"];
       self.machines={26:Machine(),13:Machine(),6:Machine(),5:Machine(),22:Machine(),27:Machine(),17:Machine()}
       #machines = [Machine() for i in range(8)]
       pos = [26,13,6,5,22,27,17]
       self.frame=Frame(root)
       for i  in range(0 , 28) :
             self.frame.columnconfigure(i, weight=1)

       self.frame.pack(expand=True,fill=BOTH)
       rowpos=0
       i=0
       Label(self.frame,height=2, anchor=W ) .grid(row=3,column=0,sticky=W+E+N+S,columnspan=24) 
       for j  in range(0 , 7) :
              
              if j == 4 :
                  i=0
                  rowpos=4
              Label(self.frame,height=2, font=("Courier bold", 60), anchor=W, bg=machColors[j] ,   text="%d:" %(j+1) ) .grid(row=rowpos,column=i*6,sticky=W+E+N+S) 
              Label(self.frame, anchor=W, background=countColors[i],font=("Courier bold", 60) , padx = 10 , textvariable=self.machines[pos[j]].macCycleCount).grid(row=rowpos,column=(i*6+1),columnspan=5,sticky=W+E+N+S)
              
              self.machines[pos[j]].lblstate1= Label(self.frame, height=1,anchor=W ,bg="#ff1a1a" ,font=("Courier bold", 40),  padx = 5 ,textvariable=self.machines[pos[j]].macCycleCounter )
              self.machines[pos[j]].lblstate1.grid(row=rowpos+1,column=i*6,sticky=W+E+N+S,columnspan=6)      
              
              self.machines[pos[j]].lblOperator= Label(self.frame, height=1,anchor=W ,bg=machColors[j] ,font=("Courier bold", 40),  padx = 5 ,textvariable=self.machines[pos[j]].macOperator )
              self.machines[pos[j]].lblOperator.grid(row=rowpos+2,column=i*6,sticky=W+E+N+S,columnspan=6)      
              
              i=i+1
