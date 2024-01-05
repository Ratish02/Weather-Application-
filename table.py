from tkinter import *
from tkinter.ttk import Treeview
class Labelwindow:
  def __init__(self):  
    self.root=Tk()
    self.root.title(' WEATHER APP ')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('900x600')

    self.fr = Frame(self.root, bg="white")
    self.fr.place(x=0, y=0, width="900", height="600")

    self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'D', 'E', 'F' ),selectmode="extended")

    self.tr.heading('#0',text="Id")
    self.tr.column('#0',minwidth=2,width=70,stretch=NO)
    self.tr.place(x=0,y=0,width="900",height="600")

    self.tr.heading('#1',text="Username")
    self.tr.column('#1',minwidth=3,width=80 ,stretch=NO)
    self.tr.place(x=0,y=0,width="900",height="600")
    
    self.tr.heading('#2',text="Mobile number")
    self.tr.column('#2',minwidth=2,width=90,stretch=NO)
    self.tr.place(x=0,y=0,width="900",height="600")
    
    self.tr.heading('#3',text="e-mail")
    self.tr.column('#3',minwidth=2,width=100,stretch=NO)
    self.tr.place(x=0,y=0,width="900",height="600")
    
    self.tr.heading('#4',text="Location")
    self.tr.column('#4',minwidth=2,width=110,stretch=NO)
    self.tr.place(x=0,y=0,width="900",height="600")
    
    self.tr.heading('#5',text="Password")
    self.tr.column('#5',minwidth=2,width=120,stretch=NO)
    self.tr.place(x=0,y=0,width="900",height="600")
    
    
    
    self.tr.place(x=0,y=0,width="900",height="600")

    self.root.mainloop()
        

if __name__ == '__main__':
    obj = Labelwindow()