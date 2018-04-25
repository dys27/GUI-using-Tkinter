import Tkinter as tk
import webbrowser

def doorbell(event):
    print "You rang a doorbell"

def click_google(event):
    webbrowser.open_new_tab('https://www.google.com') #open a new tab on button click

window=tk.Tk()
window.geometry("300x200")

alabel=tk.Label(text="Banana")
alabel.grid(column=0,row=0)

blabel=tk.Label(text="Apple")
blabel.grid(column=1,row=0)

button1=tk.Button(window,text="Doorbell")
button1.grid(column=0,row=1)

button2=tk.Button(window,text="google")
button2.grid(column=1,row=1 )

button1.bind("<Button-1>",doorbell)
button2.bind("<Button-1>",click_google)
window.mainloop()
        
