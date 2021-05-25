try:
    # for Python2
    from Tkinter import Tk, Label, PhotoImage  ## widgets also encapsulated by * 
except ImportError:
    # for Python3
    from tkinter import *   ## * uses all ^^; notice lowercase 't' in tkinter here
    
root = Tk()                 # defines name of program as "tk"

# Label  vvv  is a widget imported from tkinter
hello = Label(master = root, text = "Hellooo GUI world!")

hello.pack()                # places hello(text) against top boundary of master
root.mainloop()
