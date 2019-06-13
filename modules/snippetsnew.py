from tkinter import *
from tkinter import font
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

from utils.tktext import Tktext

# import startpage if cancel
from modules import startpage as s
# import database
from utils.database import database
# --------------------
# -Snippets New class
# --------------------
class snippetsnew(Frame):

    # init class
    def __init__(self, master):
        
        # init frame
        Frame.__init__(self, master)

        title = Label(self, text = "Title")
        title.grid(row = 0, column = 0,padx=10, sticky="nw")

        self.e = Entry(self, width = 30)
        self.e.grid(row = 1, column = 0, padx=10,ipady=3,sticky="nw")

        self.desc = Label(self, text = "Description")
        self.desc.grid(row = 2, column = 0, padx=10,sticky="nw")

        self.edesc = Entry(self, width = 30)
        self.edesc.grid(row = 3, column = 0,padx=10,ipady=3, sticky="nw")

        self.content = Label(self, text = "Snippet")
        self.content.grid(row = 4, column = 0,padx=10, sticky="nw")

        self.txt = scrolledtext.ScrolledText(self, width = 60, height = 10)
        self.txt.grid( row = 5, column=0, padx=10,ipady=3, sticky="nw")
        text = Tktext(master,self.txt)

        btn = Button(self, text = "Save", width=8,command=lambda: self.save_snippet() )
        btn.grid(row=6, column=0, padx=10,  pady=10, sticky="nw")

        btnCancel = Button(self, text = "Cancel", width=8, command=lambda: master.switch_frame(s.startpage))
        btnCancel.grid(row=6, column=0,  padx=80,  pady=10, sticky="nw")

    def save_snippet(self):
        t = self.e.get()
        if not t: messagebox.showwarning(message="The title is empty", title="Error")
        d = self.edesc.get()
        if not d: messagebox.showwarning(message="The description is empty", title="Error")
        c = self.txt.get('1.0', END)
        if len(c) < 2: 
            messagebox.showwarning(message="The content is empty", title="Error")
        else:
            if t and d:
                database().set(t,d,c)
                self.master.switch_frame(s.startpage)