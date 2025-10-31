#import necessary libraries
from tkinter import *

#setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")

#function to open New(TopLevel) Window
def topwin():
    #setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    #adding a label widget to Top Window
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
    
    top.mainloop()
    
#adding a label and button widget to rooot (main) window
l = Label(root, text = "This is rooot window")
btn = Button(root, text = "clicke her to open another window", command = topwin)

#arranging widgets
l.pack()
btn.pack()

root.mainloop()

