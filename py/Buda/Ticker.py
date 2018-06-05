import json
import requests
import time

from Logger import *

class Ticker():
	last_price=['0.0', 'CLP']
	max_bid=['0.0', 'CLP']
	min_ask=['0.0', 'CLP']
	price_variation_24h=float(0)
	price_variation_7d=float(0)
	market_id=""

	def setTicker(self, inLastPrice, inMaxBid, inMinAsk, inPrice24h, inPrice7d, inMarketId):
		self.last_price = inLastPrice
		self.max_bid = inMaxBid
		self.min_ask = inMinAsk
		self.price_variation_24h = inPrice24h
		self.price_variation_7d = inPrice7d
		self.market_id = inMarketId

	def getTicker(self, mkt):
		try:
			url = 'https://www.buda.com/api/v2/markets/' + mkt + '/ticker.json'
			req = requests.get(url)

			tkrJson = json.loads(req.text)
			self.setTicker(tkrJson['ticker']['last_price'], 
				tkrJson['ticker']['max_bid'], 
				tkrJson['ticker']['min_ask'], 
				tkrJson['ticker']['price_variation_24h'], 
				tkrJson['ticker']['price_variation_7d'], 
				tkrJson['ticker']['market_id'])
			
		except requests.exceptions.ConnectionError:
			pass