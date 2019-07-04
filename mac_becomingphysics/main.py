import tkinter as tk
import FirstScreen as fs
import variables as v
#from tkinter.ttk import *


top = tk.Tk()


lf1 = tk.LabelFrame(top) ##height, width will be ignored unless you also call .grid_propagate(0) (prolly will want to do that for consistency)
app1 = fs.FirstScreen(lf1)

#lf2 = tk.LabelFrame(top, text="My Image")
#app2 = SimpleImageApp(lf2)


##must place the labelframe!!
lf1.grid()
#lf2.grid()
top.mainloop()