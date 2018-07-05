import datetime
import json
import requests
import time

from Logger import *

class History():
	ohlc = [{"o": float(0), "h": float(0), "l": float(0), "c": float(0)}]
	ohlcAvrg = {"o": float(0), "h": float(0), "l": float(0), "c": float(0)}

	def getHistory(self, inDtRng, inMlSc, inMkt):
		try:
			cnt = 24
			dateNow = datetime.datetime.now()
			dateTo = str(int(dateNow.timestamp()))
			dateFrom = str(int(dateTo) - inMlSc)

			url = 'https://www.buda.com/api/v2/tv/history?symbol=' + inMkt + '&resolution=' + inDtRng + '&from=' + dateFrom + '&to=' + dateTo
			res = requests.get(url)

			hstJson = json.loads(res.text)

			arrLen = len(hstJson['o']) - cnt # Largo de lista para obtener últimos movimientos
			i = 0
			self.ohlc = []

			while i < cnt:

				registro = {
					"o": float(hstJson['o'][arrLen]),
					"h": float(hstJson['h'][arrLen]),
					"l": float(hstJson['l'][arrLen]),
					"c": float(hstJson['c'][arrLen])}
				self.ohlc.append(registro)

				registro = {
					"o": (self.ohlcAvrg['o'] + hstJson['o'][arrLen]),
					"h": (self.ohlcAvrg['h'] + hstJson['h'][arrLen]),
					"l": (self.ohlcAvrg['l'] + hstJson['l'][arrLen]),
					"c": (self.ohlcAvrg['c'] + hstJson['c'][arrLen])}
				self.ohlcAvrg = registro

				arrLen += 1
				i += 1

			registro = {
				"o": (self.ohlcAvrg['o'] / cnt),
				"h": (self.ohlcAvrg['h'] / cnt),
				"l": (self.ohlcAvrg['l'] / cnt),
				"c": (self.ohlcAvrg['c'] / cnt)}
			self.ohlcAvrg = registro

			print(res.text)

		except requests.exceptions.ConnectionError:
			pass