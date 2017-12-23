#Author: Foster C. Williams fosterclarksonwilliams@gmail.com
#Basic program to pull down data from google trends with a crude GUI
import coinTrends 
from os import system
from Tkinter import *
import Tkinter
import sys
import datetime
import tkMessageBox
import time

def get_data():
  term = search_term.get()
  start = start_date.get()
  end = stop_date.get()
  try:
    string=coinTrends.getPayload(term,start,end)
  except:
    tkMessageBox.showinfo("Error","Please enter dates in the YYYY-MM-DD format")
    return
  f = open('tempData.txt','w')
  f.write(string)
  time.sleep(1)
  f.close()
  system('python reveal_data.py tempData.txt')
  return
    
    

def get_5year_data():
  term = search_term.get()
  string=coinTrends.getPayload(term,'today','5-y')
  f = open('tempData.txt','w')
  f.write(string)
  time.sleep(1)
  f.close()
  system('python reveal_data.py tempData.txt')
  return

def get_big_data():
  inFile = file_to_read.get()
  outFile = file_to_output.get()
  if (outFile == ""):
    outFile = tempData.txt
  source = open(inFile,'r')
  output = open(outFile,'w')
  lines = source.readlines()
  start = ""
  end = ""
  toReturn = ""
  print "Starting loop..."
  for line in lines:
    start = start_date.get()
    end = stop_date.get()
    try:
      string = coinTrends.getPayload(line,start,end)
    except:
      tkMessageBox.showinfo("Error","Please enter dates in the YYYY-MM-DD format")
      return
    output.write(string)
    output.write("\n")
  source.close()
  output.close()
  tkMessageBox.showinfo("Message", "Successfully wrote data to " + outFile + " based on the topics in " + inFile)
  return
    
    

def get_instructions():
  tkMessageBox.showinfo("Instructions", "Enter the topic you want data about, then the dates in YYYY-MM-DD you want it from. \nYou may also designate an an input file and the data for each topic listed in it will be put into the listed output file (by default this is tempData.txt).")
root = Tk()
root.title("Cloutcoin")
label_stop_date = StringVar()
label_start_date = StringVar()
label_search_term = StringVar()
label_file_input = StringVar()
label_file_output = StringVar()
instructions = Button(root, text="Instructions", command = get_instructions)
start_date_label = Label(root, textvariable = label_start_date)
start_date = Entry(root) 
stop_date_label = Label(root, textvariable = label_stop_date)
stop_date = Entry(root)
show_data = Button(root, text="Get Data", command = get_data)
search_term_label = Label(root, textvariable = label_search_term)
search_term = Entry(root)
read_file_label = Label(root, textvariable = label_file_input)
file_to_read = Entry(root)
five_year_data = Button(root, text="5 Year Data",command = get_5year_data)
file_output_label = Label(root,textvariable = label_file_output)
file_to_output = Entry(root)
big_data = Button(root, text="Read Input File", command = get_big_data)


label_stop_date.set("Stop Date")
label_start_date.set("Start Date")
label_search_term.set("Search Term")
label_file_input.set("File Input")
label_file_output.set("File Output")



search_term_label.grid(row=0,column=0)
start_date_label.grid(row=1,column=0)
stop_date_label.grid(row=2,column=0)
stop_date.grid(row=2,column=1)
start_date.grid(row=1,column=1)
show_data.grid(row=3,column=0)
search_term.grid(row=0,column=1)
read_file_label.grid(row=4,column=0)
file_to_read.grid(row=4,column=1)
five_year_data.grid(row=3,column=1)
file_to_output.grid(row=5,column=1)
file_output_label.grid(row=5,column=0)
instructions.grid(row=6,column=0)
big_data.grid(row=6,column=1)
root.mainloop()



