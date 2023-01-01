from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
root.title("clock digital")
root.geometry("500x700")
root.resizable(1,1)
menubar=Menu(root)
root.config(menu=menubar)
#adding file menue add
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label='New file',command="")
file.add_command(label='open',command="")
file.add_command(label='Save as',command="")
file.add_command(label='Exit',command=root.destroy)
#
Edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=Edit)
Edit.add_command(label='cut',command="")
Edit.add_command(label='copy',command="")
Edit.add_command(label='Delete',command="")
Edit.add_command(label='Exit',command=root.destroy)
root.mainloop()