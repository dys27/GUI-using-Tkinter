import Tkinter as tk

def doorbell(event):
    print("you pressed a doorbell!!!")

window=tk.Tk()
window.geometry("300x200")

alabel=tk.Label(text="banana") #adding text
alabel.grid(column=0,row=0)

button1=tk.Button(window,text="doorbell") #adding button
button1.grid(column=0,row=1)

button1.bind("<Button-1>",doorbell)

window.mainloop()
