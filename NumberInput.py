import thread
from Tkinter import *
import ttk

class NumberInput:
  def __init__(self, frame):
        self.frame = frame;  
  def getandreplace(self):
    self.expression = self.e.get()

  def getRetValue(self) :
    return self.retvalue

  def equals(self):
    #when the equal button is pressed#

    self.getandreplace()
    try: 
      self.value= eval(self.newtext) #evaluate the expression using the eval function
    except SyntaxError or NameErrror:
      self.e.delete(0,END)
      self.e.insert(0,'Invalid Input!')
    else:
      self.e.delete(0,END)
      self.e.insert(0,self.value)
  
  def squareroot(self):
    """squareroot method"""
    
    self.getandreplace()
    try: 
      self.value= eval(self.newtext) #evaluate the expression using the eval function
    except SyntaxError or NameErrror:
      self.e.delete(0,END)
      self.e.insert(0,'Invalid Input!')
    else:
      self.sqrtval=math.sqrt(self.value)
      self.e.delete(0,END)
      self.e.insert(0,self.sqrtval)
  
  def clearall(self): 
    """when clear button is pressed,clears the text input area"""
    self.e.delete(0,END)
  
  def clear1(self):
    self.txt=self.e.get()[:-1]
    self.e.delete(0,END)
    self.e.insert(0,self.txt)

  def action(self,argi): 
    """pressed button's value is inserted into the end of the text area"""
    self.e.insert(END,argi)
    self.retvalue =self.e.get()
  
  def __init__(self,master):
    """Constructor method"""
    self.frame = master;  
    self.e = Entry(master)
    self.e.grid(row=0,column=0,columnspan=2,pady=3,sticky=W+E+N+S)
    self.e.focus_set() 

    #Generating Buttons
    Button(master,text="7", height=self.frame.height, command=lambda:self.action(7)).grid(row=1, column=0,sticky=W+E+N+S)
    Button(master,text="8", height=self.frame.height, command=lambda:self.action(8)).grid(row=1, column=1,sticky=W+E+N+S)
    Button(master,text="9", height=self.frame.height, command=lambda:self.action(9)).grid(row=1, column=2,sticky=W+E+N+S)
    Button(master,text="4", height=self.frame.height, command=lambda:self.action(4)).grid(row=2, column=0,sticky=W+E+N+S)
    Button(master,text="5", height=self.frame.height, command=lambda:self.action(5)).grid(row=2, column=1,sticky=W+E+N+S)
    Button(master,text="6", height=self.frame.height, command=lambda:self.action(6)).grid(row=2, column=2,sticky=W+E+N+S)
    Button(master,text="1", height=self.frame.height, command=lambda:self.action(1)).grid(row=3, column=0,sticky=W+E+N+S)
    Button(master,text="2", height=self.frame.height, command=lambda:self.action(2)).grid(row=3, column=1,sticky=W+E+N+S)
    Button(master,text="3", height=self.frame.height, command=lambda:self.action(3)).grid(row=3, column=2,sticky=W+E+N+S)
    Button(master,text="0", height=self.frame.height, command=lambda:self.action(0)).grid(row=4, column=0,sticky=W+E+N+S)
    Button(master,text='<-',  height=self.frame.height, command=lambda:self.clear1()).grid(row=4, column=1,sticky=W+E+N+S)
    
  #Main