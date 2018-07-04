import datetime
import json
import requests
import time

from Logger import *

class History():
	ohlc = [{"o": float(0), "h": float(0), "l": float(0), "c": float(0)}]

	def getHistory(self, inDtRng, inMlSc, inMkt):
		try:
			dateNow = datetime.datetime.now()
			dateTo = str(int(dateNow.timestamp()))
			dateFrom = str(int(dateTo) - inMlSc)

			url = 'https://www.buda.com/api/v2/tv/history?symbol=' + inMkt + '&resolution=' + inDtRng + '&from=' + dateFrom + '&to=' + dateTo
			res = requests.get(url)
			
			hstJson = json.loads(res.text)

			arrLen = len(hstJson['o']) # Largo de lista para obtener últimos movimientos
			i = 0
			self.ohlc = []

			while i < 12:
				arrLen -= 1
				registro = {
					"o": float(hstJson['o'][arrLen]),
					"h": float(hstJson['h'][arrLen]),
					"l": float(hstJson['l'][arrLen]),
					"c": float(hstJson['c'][arrLen])}
				self.ohlc.append(registro)

				i += 1
		except requests.exceptions.ConnectionError:
			pass