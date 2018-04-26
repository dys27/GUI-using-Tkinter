import Tkinter as tk

parent=tk.Tk()

#tk.WidgetName(parent_frame,options)
tk.Entry(parent,width=25).pack()
tk.Button(parent,text="LOOKOUT!").pack()
tk.Checkbutton(parent,text="remember me",variable=tk.IntVar()).pack()
tk.Label(parent,text="what's your name?").pack()
tk.OptionMenu(parent,tk.IntVar(),"Select Age","15+","25+","40+","60+").pack()
tk.Scrollbar(parent,orient=tk.VERTICAL).pack()
tk.Radiobutton(parent,text="Democratic",variable=tk.IntVar(),value=3).pack()
tk.Radiobutton(parent,text="Republic",variable=tk.IntVar(),value=5).pack()

parent.mainloop()
