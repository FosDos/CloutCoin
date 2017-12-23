import sys
import pytrends
from pytrends.request import TrendReq
import arrow
"""
getPayload accesses google trends and pulls down data into a string

searchterm - string, term to return data for
startdate - string, date to start data collection on YYYY-MM-DD format
enddate - string, date to end data collection on YYYY-MM-DD format

returns string with data for that time period
"""
def getPayload(searchterm, startdate, enddate):
  print "Finding data for " + searchterm + " between " + startdate + ", and " + enddate + "..."
  #setting up connection to google 
  pytrends = TrendReq(hl='en-US', tz=360)
  kw_list = [searchterm]
  timeFrame = '' + startdate + ' ' + enddate
  #building payload, cat always 0, geo and gprop empty for now
  pytrends.build_payload(kw_list, cat=0, timeframe = timeFrame, geo='', gprop='')
  
  return pytrends.interest_over_time().to_string()
'''
parsePayload takes the string that getPayload created and returns a []

payload - string generated by getPayload

returns [] with the oldest data at the start of the list
'''
def parsePayload(payload):
  toReturn = []
  #first two lines are irrelevant so we cut them
  dataList = payload.splitlines()[2:] 
  #In order to get them out of unicode, I found I had to make them utf-8
  for item in dataList:
    #Break up each line into a list by spaces
    lineBreakup = item.split() 
    #Iterate through list encoding each to be utf-8
    for x in range(len(lineBreakup)):
      lineBreakup[x] = lineBreakup[x].encode("utf-8")
    #The second item in each list is the number we want so we append that
    #If the input on getting the payload included hours, we want to ignore that
    if len(lineBreakup[1])>3:
      toReturn.append(int(lineBreakup[2]))
    else:
      toReturn.append(int(lineBreakup[1]))
  return toReturn
 
"""
anaylze12MonthData takes in a [] full of numbers generated by parsePayload, returns its analysis

data - [] full of ints representing weekly google trend numbers

returns anaylsis of the data depending on its values


"""
def analyze12MonthData(data):
  #slim down data to past 3 weeks
  realData = data[-3:]
  #first we iterate through the data, if everything is below 5, we ignore the data
  badDataFlag = True
  for item in realData:
    if item > 5:
      badDataFlag = False
  if (badDataFlag):
    return "No good data"
  holder = realData[0]
  for item in realData:
    if item >= holder:
      holder = item
    else:
      return "No Growth"
  toReturn = "The data has been steadily increasing with values of: " + realData + "\n"
  lastWeekIncrease = realData[2] - realData[1]
  lastWeekPercentIncrease = (lastWeekIncrease/realData[1])*100
  twoWeekIncrease = (realData[1] - realData[0])
  twoWeeksPercentIncrease = (twoWeekIncrease/realData[0])*100
  toReturn = toReturn + "In the past week, trend data has a " + str(lastWeekPercentIncrease) + "% increase\n"
  toReturn = toReturn + "From 2 weeks ago to last week, trend data has a " + str(twoWeeksPercentIncrease) + "% increase\n"
  return toReturn
