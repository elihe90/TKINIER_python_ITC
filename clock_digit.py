from tkinter import *
import  time
app_window=Tk()
app_window.title("clock digital")
app_window.geometry("300x300")
app_window.resizable(1,1)
text_font=("Arial",40)
forground="#f2e750"
background="y"
border_width=25
lbl_digit=Label(app_window,font=("Arial",50),background="yellow",foreground="blue")
lbl_digit.grid(row=0,column=1)
def digit_time():
   time_live =time.strftime("%H:%M:%S")
   lbl_digit.config(text=time_live)
   lbl_digit.after(100,digit_time)
digit_time()
app_window.mainloop()