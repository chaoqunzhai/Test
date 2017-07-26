from  tkinter import *
root=Tk()
def buffonClick():
    print('buttion')

button=Button(text='hellow',command=buffonClick)
button.pack()
root.mainloop()