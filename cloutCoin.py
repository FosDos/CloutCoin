from os import system
from time import sleep

zzz = open('currency.txt','r')
currencies = []
currency = 0;
for line in zzz:
  currencies.append(line)

for x in range(len(currencies)):
  currency = currencies[x]
  currency.lstrip()
  command = 'python trend_data.py purchase ' + currency + ' > ' 
  print command
