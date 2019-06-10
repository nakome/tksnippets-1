from tkinter import *
from tkinter import ttk

# import sections snippets
from modules.snippets import snippets
# import database 
from utils.database import database
# import custom enty with placeholder
from utils.placeholder import EntryWithPlaceholder

# ----------------------
#   Class startpage
# ----------------------
class startpage(Frame):

    # init class
    def __init__(self, master):
        # frame 
        Frame.__init__(self, master)

        self.master = master

        self.e = EntryWithPlaceholder(self,"Search")
        self.e.pack(side="top", fill="x")
        self.e.bind('<KeyPress>', self.search_by_title)


        # create treeview like table
        self.tree = ttk.Treeview(self, columns=("uid", "title", "desc","date"))
        self.tree["show"] = "headings"
        self.tree.heading("uid", text="Uid")
        self.tree.column("uid",minwidth=50,width=50)
        self.tree.heading("title", text="Title")
        self.tree.column("title",minwidth=50,width=120)
        self.tree.heading("desc", text="Description")
        self.tree.column("desc",minwidth=240,width=240)
        self.tree.heading("date", text="Date")
        self.tree.column("date",minwidth=50,width=120)
        # insert database items
        for item in database().get_all(): 
            self.tree.insert("", "end", values=(item[0],item[1], item[2],item[4]))
        # add comand on items
        self.tree.bind("<Double-1>", self.itemEvent)
        self.tree.pack()




    # search title
    def search_by_title(self,event):
        if event.char == '\r':
            if len(self.e.get()) > 3:
                title = self.e.get()
                # clear tree
                for i in self.tree.get_children(): self.tree.delete(i)
                # insert data
                for item in database().find_by_title(title):
                    self.tree.insert("", "end", values=(item[0],item[1], item[2],item[4]))
            else:
                # clear tree
                for i in self.tree.get_children(): self.tree.delete(i)
                # insert data
                for item in database().get_all():
                    self.tree.insert("", "end", values=(item[0],item[1], item[2],item[4]))


    # on doumble click run method
    def itemEvent(self,event):
        # get selection
        for item in self.tree.selection():
            # get values
            data = self.tree.item(item, "values")
            # get and save on master uid
            self.master.uid = int(data[0])
            # change frame to snippets
            self.master.switch_frame(snippets)