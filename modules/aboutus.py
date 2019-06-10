from tkinter import *
import webbrowser

# import startpage if cancel
from modules import startpage as s

# --------------------
# -About Us class
# --------------------
class aboutus(Frame):
    
    # init class
    def __init__(self, master):

        # init frame
        Frame.__init__(self, master)

        # label info
        v = Label(self, width=50, text = "Version: 1.0.0").pack(anchor="w")
        d = Label(self, width=50, text = "Developer: Moncho Varela").pack(expand=1, anchor="nw")
        y = Label(self, width=50, text = "Date: June 10 2019").pack(anchor="w")
        url = Label(self, width=50, text="Github source", fg="blue", cursor="hand2")
        url.bind("<Button-1>", lambda e: self.callback("https://github.com/monchovarela/tksnippets"))
        url.pack(pady=10,anchor="nw")
        btn = Button(self, text = "Back", width=8, command=lambda: master.switch_frame(s.startpage))
        btn.pack(padx=10,pady=10,anchor="w")

    def callback(self,url):
        webbrowser.open_new(url)