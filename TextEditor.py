from Console import *
import thread
import Tkinter
import Tkinter as tk
from Tkinter import *
from code import InteractiveConsole
from tkFileDialog import *
import tkFont
import tkMessageBox
import os
from Interpreter import *

class TextEditor:
    def __init__(self):
        self.fileName = None
        self.text = None

    def start(self):
        root = Tk()
        #==========================
        #  Set Screen parameters
        #==========================
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.title("Agrafena Text Editor")
        root.minsize(width=500, height=500)
        root.overrideredirect(0)
        root.geometry("%dx%d+0+0" % (400, 400))

        #==========================
        #  TEXT INPUT&Scroll bar
        #==========================
        S = Scrollbar(root)
        self.text = Text(root, height=h, width=w, fg='purple', font=('Georgia', '11'))
        self.text.tag_config('highlight', foreground='red')
        self.text.tag_add('highlihgt', 1.0, END, )

        S.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=Y)
        S.config(command=self.text.yview)
        self.text.config(yscrollcommand=S.set)

        #===================
        #    File Menu
        #===================

        menubar = Menu(root)
        filemenu = Menu(menubar)
        filemenu.add_command(label="New", command=self.newFile)
        filemenu.add_command(label="Open", command=self.openFile)
        filemenu.add_command(label="Save", command=self.saveFile)
        filemenu.add_command(label="Save As .. ", command=self.saveAs)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        #===================
        #   Run&Help Menu
        #===================

        runmenu = Menu(menubar)
        runmenu.add_command(label="Run Module", command=self.run)
        menubar.add_cascade(label='Run', menu=runmenu)

        helpmenu = Menu(menubar)
        helpmenu.add_command(label="About Agrafena", command=self.info)
        menubar.add_cascade(label='Help', menu=helpmenu)

        root.config(menu=menubar)
        for keyword in Interpreter.Keywords:
            root.bind(keyword, self.call_back_highlight_function)

        root.mainloop()

    def newFile(self):
        self.fileName = "Untitled"
        self.text.delete(0.0, END)


    def openFile(self):
        f = askopenfile(mode='r')
        if f is not None:
            self.fileName = os.path.basename(f.name)
            t = f.read()
            self.text.delete(0.0, END)
            self.text.insert(0.0, t)


    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        if f is not None:
            t = self.text.get(0.0, END)
            self.fileName = os.path.basename(f.name)
            f.write(t.rstrip())

    def saveFile(self):
        if self.fileName is not None:
            t = self.text.get(0.0, END)
            f = open(self.fileName, 'w')
            self.fileName = os.path.basename(f.name)
            f.write(t)
            f.close()
        else :
            self.saveAs()


    def run(self):
        statements = self.text.get(0.0, END)
        thread.start_new_thread(Console, (str(statements),))

    def info(self):
        tkMessageBox.showinfo(title='About The Agrafena Project',
                              message="Agrafena\nProgram Version : 1.0\n\nEmail : mohammad.siav@hotmail.com")

    def call_back_highlight_function(self, *args):
        for keyword in Interpreter.Keywords:
            start = self.text.index(1.0)
            end = self.text.index('end')
            self.text.mark_set("matchStart", start)
            self.text.mark_set("matchEnd", start)
            self.text.mark_set("searchLimit", end)
            
            count = tk.IntVar()

            while True:
                index = self.text.search(keyword, "matchEnd", "searchLimit", count=count)
                if index == "": break
                self.text.mark_set("matchStart", index)
                self.text.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
                self.text.tag_add('highlight', "matchStart", "matchEnd")
