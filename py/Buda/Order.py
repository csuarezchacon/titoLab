from Core import Core
from trading_api_wrappers import Buda

cr = Core()

class Order():
	order = None

	def setOrder(self, inOrder):
		self.order = inOrder

	def doOrder(self, inMkt, inType, inLimit, inAmount):
		try:
			buda = Buda.Auth(cr.k, cr.s)
			res = buda.new_order(inMkt, inType, "limit", inLimit, inAmount)
			
			self.setOrder(res)
			
		except Exception:
			pass

	def doCancel(self, orderId):
		try:
			buda = Buda.Auth(cr.k, cr.s)
			buda.cancel_order(orderId)
		except Exception:
			pass