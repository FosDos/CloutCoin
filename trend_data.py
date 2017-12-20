import sys

import pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
search = str(sys.argv[1] + " " +  sys.argv[2])
kw_list = [search]
pytrends.build_payload(kw_list, cat=0, timeframe = 'today 5-y', geo='', gprop='')

print pytrends.interest_over_time()
