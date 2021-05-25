from tkinter import *

root = Tk()

#label for a body of text
text = Label(root,
             font = ('Helvetica', 18, 'bold italic'),
             foreground='white',                        # text color
             background='black',                        # background color
             padx=200,                                   # widen label 25 pixels horizontally
             pady=50,                                   # widen label 20 pixels vertically
             text='Here is the left side body of text:')
#push label to top
text.pack(side=LEFT)                                    # comes from import *                                  


#label for a body of text
text = Label(root,
             font = ('Helvetica', 18, 'bold italic'),
             foreground='black',                        # text color
             background='white',                        # background color
             padx=200,                                   # widen label 25 pixels horizontally
             pady=50,                                   # widen label 20 pixels vertically
             text='Here is the right side different body of text:')
#push label to top
text.pack(side=RIGHT)                                    # comes from import * 




root.mainloop()
