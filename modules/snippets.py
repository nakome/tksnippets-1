from tkinter import *
from tkinter import scrolledtext

# import startpage if cancel
from modules import startpage as s
# import database
from utils.database import database

# --------------------
# -Snippets class
# --------------------
class snippets(Frame):

    # init class
    def __init__(self, master):
        
        # init frame
        Frame.__init__(self, master)

        # get database items by uid
        self.uid = master.uid
        if self.uid : data = database().get_by_uid(self.uid)

        title = Label(self, text = "Title")
        title.grid(row = 0, column = 0,padx=10, sticky="nw")

        self.e = Entry(self, width = 30)
        self.e.insert(END, data[1])
        self.e.grid(row = 1, column = 0,padx=10,ipady=5, sticky="nw")

        desc = Label(self, text = "Description")
        desc.grid(row = 2, column = 0,padx=10,sticky="nw")

        self.edesc = Entry(self, width = 30)
        self.edesc.insert(END, data[2])
        self.edesc.grid(row = 3, column = 0,padx=10,ipady=5, sticky="nw")

        content = Label(self, text = "Snippet")
        content.grid(row = 4, column = 0,padx=10, sticky="nw")

        self.txt = scrolledtext.ScrolledText(self, width = 60, height = 10,insertbackground="white",bg="black",fg="cyan")
        self.txt.grid( row = 5, column=0,padx=10, sticky="nw")
        # set scrolledtext content
        self.txt.insert(INSERT, data[3])

        btn = Button(self, text = "Save", width=8,  command=lambda: self.update_snippet() )
        btn.grid(row=6, column=0, padx=10,  pady=10, sticky="nw")

        btnCancel = Button(self, text = "Cancel", width=8,  command=lambda: master.switch_frame(s.startpage))
        btnCancel.grid(row=6, column=0,  padx=80,  pady=10, sticky="nw")

        btnDel = Button(self, text = "Delete", width=8,   command=lambda: self.remove_snippet())
        btnDel.grid(row=6, column=0, padx=10, pady=10, sticky="se")

    # update snippet
    def update_snippet(self):
        t = self.e.get()
        if not t: messagebox.showwarning(message="The title is empty", title="Error")
        d = self.edesc.get()
        if not d: messagebox.showwarning(message="The description is empty", title="Error")
        c = self.txt.get('1.0', END)
        if len(c) < 2: 
            messagebox.showwarning(message="The content is empty", title="Error")
        else:
            if t and d:
                database().update(self.uid,t,d,c)
                self.master.switch_frame(s.startpage)

    # remove snippet
    def remove_snippet(self):
        print("Delete snippet {}".format(self.uid))
        if self.uid:
            database().delele_uid(self.uid)
            self.master.switch_frame(s.startpage)