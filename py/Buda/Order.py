
from Core import Core
from trading_api_wrappers import Buda

cr = Core()

class Order():
	orderList = None

	def new(self, inMkt, inType, inLimit, inAmount):
		try:
			buda = Buda.Auth(cr.k, cr.s)
			res = buda.new_order(inMkt, inType, "limit", inLimit, inAmount)
			
		except Exception:
			pass

	def cancel(self, orderId):
		try:
			buda = Buda.Auth(cr.k, cr.s)
			buda.cancel_order(orderId)
		except Exception:
			pass

	def myOrders(self, inMkt, inStatus):
		try:
			buda = Buda.Auth(cr.k, cr.s)
			self.orderList = buda.order_pages(inMkt, None, None, inStatus)

		except Exception:
			pass