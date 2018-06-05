import datetime
import json
import requests
import time

from Logger import *

class History():
	o = [] #Open
	h = [] #Hight
	l = [] #Low
	c = [] #Close
	s = ""
	t = []
	v = []

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
			
			self.o = histJson['o']
			self.h = histJson['h']
			self.l = histJson['l']
			self.c = histJson['c']
			self.s = histJson['s']
			self.t = histJson['t']
			self.v = histJson['v']
		except requests.exceptions.ConnectionError:
			pass