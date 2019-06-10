# tksnippets

Simple snippets app made with Python and Tkinter


### Requirements

Tkinter
Pyinstaller for package


### Package with Pyinstaller

You can create a build.bat or build.sh with this content.

    pyinstaller main.py ^
        --onefile ^
        --clean ^
        --windowed --noconsole ^

Now copy storage folder inside dist folder and voila!

