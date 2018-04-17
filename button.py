from tkinter import *
from random import *

    
class App():
    def do_event(self, event):
        print("{},{}".format(event.x,event.y))
            
    def jump(self, event):
        print("{},{}".format(event.x_root,event.y_root))      
        self.chase_b.place(x=event.x_root-100, y=event.y_root-55) 
        self.move_b.place(relx=random(), rely=random())
        
    def __init__(self, master):
        frame = Frame(master)
        master.geometry("600x600")
        master.title("awful button")
        master.bind("<Button-1>",self.do_event)
        frame.pack()

        self.move_b = Button(master, text="Quit", command=sys.exit)
        self.chase_b = Button(master, text="Continue") 
        self.move_b.bind("<Enter>", self.jump)
        self.move_b.pack()
        self.chase_b.pack()    
        
root = Tk()
app = App(root)
root.mainloop()
