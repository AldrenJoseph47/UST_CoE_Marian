#create class ust with init and to marian
#create class to marian with init and to ust


#STEP 1 :create the base window with button and image on it
#base Window in main()
import tkinter as tk
#frame is the wiget to bring the package together
#button is used to import button function into the program
from tkinter.ttk import Frame,Button
#
from tkinter import (PhotoImage,Toplevel)
#inside the Ust class there are 2 methods __init__(self,master) and to_marian(self)
class Ust(Frame):
    def __init__(self,master):
        super().__init__(master,relief='flat',borderwidth=140)# borderwidth sets the width of the border around the widget.
        #master is a reference to the parent and relief specifies the relief style for the widget
        self.master.title("UST to Marian")#renaming the windows name
        self.pack(fill=None,expand=False)#the Tkinter widget object is being instructed not to fill any extra
        # space in any direction (fill=None) and not to expand beyond its natural size (expand=False).
        self.photo=PhotoImage(file="UST.png")#to import the image from the same file
        btn=Button(self, text="Test", image=self.photo,command=self.to_marian)#creating the button with the ust
        btn.pack()
    def to_marian(self):
        Marian(self.master,self)
class Marian(Frame):
    def __init__(self,parent,main_page):
        super().__init__(parent)
        self.top=Toplevel(parent,relief='flat',borderwidth=20)
        self.main_page=main_page
        self.pack(fill=None,expand=False)
        self.photo=PhotoImage(file='Marian.png')
        button=Button(self.top,image=self.photo,command=self.to_ust)
        button.grid()
    def to_ust(self):
        self.top.destroy()
        self.destroy()
def main():
    root=tk.Tk()
    root.geometry("600x400")#size of the windows
    root.resizable(False,False)#resizing the window is not allowed
    Ust(root)
    root.mainloop()
main()