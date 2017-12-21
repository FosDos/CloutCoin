from os import system
from time import sleep
from string import printable
import sys
import string
import re

zzz = open(sys.argv[1],'r')
currencies = []
currency = 0;
for line in zzz:
  currencies.append(line)
system('rm finished')
for x in range(len(currencies)):
  currency = currencies[x]
  currency = currency.strip('\n')
  currency = currency.rstrip()
  re.sub(r'\W+', '',currency)
  file1 = currency + '_data1.txt'
  file2 = currency + '_data2.txt'
  file3 = currency + '_data3.txt'
  file4 = currency + '_data4.txt'
  command1 = 'python trend_data.py buy ' + currency + ' > ' + file1
  command2 = 'tail ' + file1 + ' > ' + file2
  command3 = 'rm ' + file1
  command4 = 'head -8 ' + file2 + ' > '  + file3
  command5 = 'rm ' + file2
  command6 = 'tail -3 ' + file3+  ' > ' + file4
  command7 = 'rm ' + file3
  command8 = 'python data_clean.py ' + file4 + ' > ' + currency
  command9 = 'python analyze.py ' + currency + ' >> finished'
  command10 = 'rm ' + file4
  command11 = 'rm ' + currency
  system(command1)
  system(command2)
  system(command3)
  system(command4)
  system(command5)
  system(command6)
  system(command7)
  system(command8)
  system(command9)
  system(command10)
  system(command11)


