import datetime
import json
import requests
import time

from Logger import *

class History():
	o = float(0) #Open
	h = float(0) #Hight
	l = float(0) #Low
	c = float(0) #Close
	s = ""
	t = float(0)
	v = float(0)

	def getHistory(self, first, mkt):
		try:
			sec = 864000 # 10 dias

			if first : sec = 31104061 # 360 dias

			dateNow = datetime.datetime.now()
			dateTo = str(int(dateNow.timestamp()))
			dateFrom = str(int(dateTo) - sec)

			url = 'https://www.buda.com/api/v2/tv/history?symbol=' + mkt + '&resolution=D&from=' + dateFrom + '&to=' + dateTo
			req = requests.get(url)
			histJson = json.loads(req.text)
			
			self.o = histJson['o'][-1]
			self.h = histJson['h'][-1]
			self.l = histJson['l'][-1]
			self.c = histJson['c'][-1]
			self.s = histJson['s']
			self.t = histJson['t'][-1]
			self.v = histJson['v'][-1]
		except requests.exceptions.ConnectionError:
			pass