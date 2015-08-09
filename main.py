import sys
from Interpreter import Interpreter
from TextEditor import *
from Tkinter import *
import ttk

arg = ''
if len(sys.argv) > 1:
    arg = sys.argv[1]
if arg == '-i':
    Interpreter().interact()
else:
    textEditor = TextEditor()
    textEditor.start()
