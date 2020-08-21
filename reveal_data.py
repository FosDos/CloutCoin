import sys


#opens file and returns the text within
def setup(filename):
  f = open(filename,'r')
  lines = f.readlines()
  toReturn = ""
  for line in lines:
    toReturn = toReturn + line
  return toReturn
