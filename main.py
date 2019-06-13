from tkinter import *

from modules.startpage import startpage
from modules.snippetsnew import snippetsnew
from modules.aboutus import aboutus

# main content class
class maincontent(Tk):

	# init class
    def __init__(self):
    	# class is a frame
        Tk.__init__(self)
        # title
        self.title("Snippets app")
        # init frame
        self._frame = None
        # uid of database item
        self.uid = IntVar()
        # switch frame on init
        self.switch_frame(startpage)

    # switch frame method
    def switch_frame(self, frame_class):

        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        # destroy frames if not empty
        if self._frame is not None:
            self.uid = False
            self._frame.destroy()
        # create new frame
        self._frame = new_frame
        # create conteainer
        self._frame.pack(side="top", fill="both", expand = True)
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        # create menu
        self.create_menu()

    # create menu
    def create_menu(self):
        menubar = Menu(self)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New snippet", command=lambda: self.switch_frame(snippetsnew))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        # help menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About Us", command=lambda: self.switch_frame(aboutus))
        menubar.add_cascade(label="Help", menu=helpmenu)
        # display the menu
        self.config(menu=menubar)


if __name__ == "__main__":

    app = maincontent()
    app.resizable(False,False)
    app.mainloop()

