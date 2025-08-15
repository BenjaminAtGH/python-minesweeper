from tkinter import *

window = Tk()

#this configures the window settings
window.title("entry box")
window.geometry("500x500")
window.configure(bg="lightgreen")    
window.resizable(False, False)
icon = PhotoImage(file="logo.png",)
window.iconphoto(True,icon)

#/////////////////////////////////////////////////
label1 = Label(window, bg="black", borderwidth=2, relief="groove")
label2 = Label(window, bg="red", borderwidth=2, relief="groove")

#define a grid//////////////////////////////////////
rows = list(range(1,6))
cols = list(range(1,6))

x= rows
y= cols


yCoor = 2
window.columnconfigure(0, weight=2)
window.columnconfigure((x), weight=1)
window.rowconfigure(0, weight=2)
window.rowconfigure((y), weight=1)
label1.grid(row=0, column=0, columnspan=len(x)+1, sticky="nsew")
label2.grid(row=1, column=0, rowspan=len(y), sticky="nwes")


for i in (rows):
    for j in (cols):
        btn = Button(window, text=f"({i},{j})", width=5, height=5)
        btn.grid(row=i, column=j, sticky="news")


window.mainloop()