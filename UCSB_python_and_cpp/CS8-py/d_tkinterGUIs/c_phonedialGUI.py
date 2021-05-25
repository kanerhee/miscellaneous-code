from tkinter import *
root = Tk()


#phone dial label texts organized in a grid
labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):                                      # for every row r = 0,1,2,3
    for c in range(3):                                  # for every column c = 0,1,2

        label = Label(root,
                        relief=RAISED,
                        padx=10,
                        text=labels[r][c])
        # places label in row r and column c                
        label.grid(row=r, column=c)



root.mainloop()
