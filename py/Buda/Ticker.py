import json
import requests
import time

from Logger import *

class Ticker():
	last_price=float(0)
	max_bid=float(0)
	min_ask=float(0)
	price_variation_24h=float(0)
	price_variation_7d=float(0)
	market_id=""

	def setTicker(self, inLastPrice, inMaxBid, inMinAsk, inPrice24h, inPrice7d, inMarketId):
		self.last_price = float(inLastPrice)
		self.max_bid = float(inMaxBid)
		self.min_ask = float(inMinAsk)
		self.price_variation_24h = float(inPrice24h)
		self.price_variation_7d = float(inPrice7d)
		self.market_id = inMarketId

	def getTicker(self, inMkt):
		try:
			url = 'https://www.buda.com/api/v2/markets/' + inMkt + '/ticker.json'
			res = requests.get(url)

			tkrJson = json.loads(res.text)
			self.setTicker(tkrJson['ticker']['last_price'][0], 
				tkrJson['ticker']['max_bid'][0], 
				tkrJson['ticker']['min_ask'][0], 
				tkrJson['ticker']['price_variation_24h'], 
				tkrJson['ticker']['price_variation_7d'], 
				tkrJson['ticker']['market_id'])
			
		except requests.exceptions.ConnectionError:
			pass