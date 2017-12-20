import sys

data = open(sys.argv[1])
nums = []
for line in data:
  nums.append(int(line))
flag = False
print "======================================================"
print "-------------------LITECOIN---------------------------"
print ("Trend in past 3 weeks has been: " + str(nums[0]) + ", " + str(nums[1]) + ", " + str(nums[2]) + ".")
print " "
if(nums[0]*2 < nums[1]):
  if(nums[1]*2 < nums[2]):
    print sys.argv[1] + " currently is trending with double 100% increases in the past 2 weeks"
    print " " 
    flag = True
if flag == False:
  print "nah fam you good, " + sys.argv[1] + " aint that hot rn"
  print " " 
print "------------------------------------------------------"
print "======================================================"

