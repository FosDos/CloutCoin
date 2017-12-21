import sys
cashout = open('money.txt','a')
cashString = ""
data = open(sys.argv[1])
nums = []
for line in data:
  nums.append(int(line))
flag = False
print "======================================================"
print "-------------------" + sys.argv[1] + "---------------------------"
try:
  print ("Trend in past 3 weeks has been: " + str(nums[0]) + ", " + str(nums[1]) + ", " + str(nums[2]) + ".")
  print " "
  oldPrice = float(nums[0])
  midPrice = float(nums[1])
  newPrice = float(nums[2])
  
  if (oldPrice < midPrice and midPrice < newPrice and midPrice > 9):
    print "Steady Growth" 
    cashString = cashString + "===================================\n"
    cashString = cashString + "------------" + sys.argv[1] + "--------------\n" 
    if (oldPrice*2 <= midPrice and midPrice*2 <= newPrice):
      print "Has increased by 100% twice in 2 weeks"
      cashString = cashString + "Has increased by 100% twice in 2 weeks\n"
    if (midPrice*2.25 <= newPrice):
      print "Has jumped 225% in the past week"
      cashString = cashString + "Has increased by 100% twice in 2 weeks\n"
    cashString = cashString + "\n"
    cashString = cashString + "---------------------------------------\n"
    cashString = cashString + "========================================\n"
    cashString = cashString + "\n"
    cashout.write(cashString)
    
except:
  print "Not enough relevant data for " + sys.argv[1] 
  print " " 
print "------------------------------------------------------"
print "======================================================"
print "..."
print "..."
print "..."
print "..."
