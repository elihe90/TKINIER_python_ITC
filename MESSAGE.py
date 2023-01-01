from tkinter import *
main = Tk()
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
T = Text(main, height=2, width=30)
T.pack()
T.insert(END, 'fgfgfgfgfg\nBEST WEBSITE\n')
main.mainloop( )