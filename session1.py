import tkinter as tk
from tkinter import *
m=tk.Tk()
m.title('session1')
con=tk.Canvas(m,width=150,height=50)
button = tk.Button(m, text='submit', width=25)
lbl=tk.Label(m,text='fname',background='red')
var1=IntVar()
var2=IntVar()
Checkbutton(m,text='male', variable=var1).grid(row=3,column=0)
Checkbutton(m,text='fmale', variable=var2).grid(row=3,column=1)
con.grid(row=2)
lbl.grid(row=1)
button.grid(row=4)
lbl2=tk.Label(m,text='project')
lbl2.grid(row=5)

Label(m, text='First Name').grid(row=6)
Label(m, text='Last Name').grid(row=7)
e1 = Entry(m,width=100)
e2 = Entry(m,width=100)
e1.grid(row=6, column=1)
e2.grid(row=7, column=1)


m.mainloop()