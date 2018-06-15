from Logger import *
from trading_api_wrappers import Buda

class Ticker():
	last_price=float(0)
	max_bid=float(0)
	min_ask=float(0)
	price_variation_24h=float(0)
	price_variation_7d=float(0)
	volume=float(0)

	def setTicker(self, inLastPrice, inMaxBid, inMinAsk, inPrice24h, inPrice7d, inVolume):
		self.last_price = float(inLastPrice)
		self.max_bid = float(inMaxBid)
		self.min_ask = float(inMinAsk)
		self.price_variation_24h = float(inPrice24h)
		self.price_variation_7d = float(inPrice7d)
		self.volume = float(inVolume)

	def getTicker(self, inMkt):
		try:
			buda = Buda.Public()
			res = buda.ticker(inMkt)
			
			self.setTicker(res.last_price.amount,
				res.max_bid.amount,
				res.min_ask.amount,
				res.price_variation_24h,
				res.price_variation_7d,
				res.volume.amount)
			
		except Exception:
			pass