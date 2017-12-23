import Tkinter
from ScrolledText import *
import sys


#opens file and returns the text within
def setup(filename):
  f = open(filename,'r')
  lines = f.readlines()
  toReturn = ""
  for line in lines:
    toReturn = toReturn + line
  return toReturn

text = setup('tempData.txt')
root = Tkinter.Tk(className=" Another way to create a scrollable text area")
textPad = ScrolledText(root, width=50, height =50)
textPad.insert('1.0', text)
textPad.pack()
root.mainloop()
