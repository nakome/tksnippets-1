from tkinter import *
from tkinter import font

from pygments.lexers.python import PythonLexer
from pygments.styles import get_style_by_name


class Tktext(object):
    
    def __init__(self, master,txt):

        self.lexer = PythonLexer()
        self.txt = txt
        # any key colorize 
        master.bind('<Key>', self.event_key)
        # paste
        master.bind('<Control-v>', self.event_paste)
        # copy
        master.bind('<Control-c>', self.event_key)
        master.update()
        self.create_tags()

    # paste method
    def paste(self, text):
        if text:
            self.txt.insert(INSERT, text)
            self.txt.tag_remove(SEL, '1.0', END)
            self.txt.see(INSERT)
            self.recolorize()

    # any key colorize
    def event_key(self, event):
        if event.keycode == 17:
            return 'break'
        self.recolorize()

    def event_paste(self, event=None):
        self.recolorize()

    def create_tags(self):
        bold_font = font.Font(self.txt, self.txt.cget("font"))
        bold_font.configure(weight=font.BOLD)

        italic_font = font.Font(self.txt, self.txt.cget("font"))
        italic_font.configure(slant=font.ITALIC)

        bold_italic_font = font.Font(self.txt, self.txt.cget("font"))
        bold_italic_font.configure(weight=font.BOLD, slant=font.ITALIC)

        style = get_style_by_name('sas')

        for ttype, ndef in style:
            # print(ttype, ndef)
            tag_font = None

            if ndef['bold'] and ndef['italic']: tag_font = bold_italic_font
            elif ndef['bold']: tag_font = bold_font
            elif ndef['italic']: tag_font = italic_font

            if ndef['color']: foreground = "#%s" % ndef['color']
            else: foreground = None

            self.txt.tag_configure(str(ttype), foreground=foreground, font=tag_font)

    def recolorize(self):
        code = self.txt.get("1.0", "end-1c")
        tokensource = self.lexer.get_tokens(code)

        start_line=1
        start_index = 0
        end_line=1
        end_index = 0
        for ttype, value in tokensource:
            if "\n" in value:
                end_line += value.count("\n")
                end_index = len(value.rsplit("\n",1)[1])
            else:
                end_index += len(value)

            if value not in (" ", "\n"):
                index1 = "%s.%s" % (start_line, start_index)
                index2 = "%s.%s" % (end_line, end_index)

                for tagname in self.txt.tag_names(index1): # FIXME
                    self.txt.tag_remove(tagname, index1, index2)

                # print(ttype, repr(value), index1, index2)
                self.txt.tag_add(str(ttype), index1, index2)

            start_line = end_line
            start_index = end_index

    def removecolors(self):
        for tag in self.tagdefs:
            self.txt.tag_remove(tag, "1.0", "end")