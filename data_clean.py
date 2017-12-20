import sys


arg = str(sys.argv[1])
text = open(arg, 'r')
data = []
for line in text:
  data.append(line)
fuck_this = []
temp = ""
for rip in range(len(data)):
  p = data[rip]
  p.split()
  x = []
  for cop in range(11,len(p)):
    x.append(p[cop])
  i = 0
  while i < len(x):
    if x[i].isdigit():
      checker = i+1
      temp = x[i]
      while x[checker].isdigit():
        temp = temp + x[checker]
        checker = checker + 1
        i = i + 1
      fuck_this.append(temp)
      temp = ""
    i = i + 1


for killme in range(len(fuck_this)):
  print fuck_this[killme]

