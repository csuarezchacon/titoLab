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

	def setHistory(self, inO, inH, inL, inC, inS, inT, inV):
		self.o = float(inO)
		self.h = float(inH)
		self.l = float(inL)
		self.c = float(inC)
		self.s = inS
		self.t = float(inT)
		self.v = float(inV)

	def getHistory(self, inFirst, inMkt):
		try:
			sec = 864000 # 10 dias

			if inFirst : sec = 31104061 # 360 dias

			dateNow = datetime.datetime.now()
			dateTo = str(int(dateNow.timestamp()))
			dateFrom = str(int(dateTo) - sec)

			url = 'https://www.buda.com/api/v2/tv/history?symbol=' + inMkt + '&resolution=D&from=' + dateFrom + '&to=' + dateTo
			res = requests.get(url)
			
			hstJson = json.loads(res.text)
			self.setHistory(hstJson['o'][-1],
				hstJson['h'][-1],
				hstJson['l'][-1],
				hstJson['c'][-1],
				hstJson['s'],
				hstJson['t'][-1],
				hstJson['v'][-1])

		except requests.exceptions.ConnectionError:
			pass