import datetime
import json
import requests
import time

from OHLC import OHLC

class History():
	ohlc = OHLC()

	ohlcList = [ohlc]
	ohlcAvrg = ohlc

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
			self.ohlcList = []

			while i < cnt:

				ohlc.setOHLC(hstJson['o'][arrLen], hstJson['h'][arrLen], hstJson['l'][arrLen], hstJson['c'][arrLen])
				self.ohlcList.append(ohlc)

				ohlc.setOHLC((self.ohlcAvrg.o + hstJson['o'][arrLen]), (self.ohlcAvrg.h + hstJson['h'][arrLen]), (self.ohlcAvrg.l + hstJson['l'][arrLen]), (self.ohlcAvrg.c + hstJson['c'][arrLen]))
				self.ohlcAvrg = ohlc

				arrLen += 1
				i += 1

			ohlc.setOHLC((self.ohlcAvrg['o'] / cnt), (self.ohlcAvrg['o'] / cnt), (self.ohlcAvrg['o'] / cnt), (self.ohlcAvrg['o'] / cnt))
			self.ohlcAvrg = ohlc

		except requests.exceptions.ConnectionError:
			pass