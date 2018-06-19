from trading_api_wrappers import Buda

class Order():
	order = None

	def setOrder(self, inOrder):
		self.order = inOrder

	def doOrder(self, inMkt, inCr, inType, inLimit, inAmount):
		try:
			buda = Buda.Auth(inCr.k, inCr.s)
			res = buda.new_order(inMkt, inType, "limit", inLimit, inAmount)
			
			self.setOrder(res)
			
		except Exception:
			pass