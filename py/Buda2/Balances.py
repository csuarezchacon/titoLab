from Core import Core
from trading_api_wrappers import Buda

cr = Core()

class Balances():
	id = ''
	amount = float(0)
	available_amount = float(0)
	frozen_amount = float(0)
	pending_withdrawal_amount = float(0)

	def setBalances(self, inId, inAmount, inAvailableAmount, inFrozenAmount, inPendingWithdrawalAmount):
		self.id = inId
		self.amount = float(inAmount)
		self.available_amount = float(inAvailableAmount)
		self.frozen_amount = float(inFrozenAmount)
		self.pending_withdrawal_amount = float(inPendingWithdrawalAmount)

	def getBalances(self, inCur):
		try:
			buda = Buda.Auth(cr.k, cr.s)
			res = buda.balance(inCur)
			
			self.setBalances(res.id,
				res.amount.amount,
				res.available_amount.amount,
				res.frozen_amount.amount,
				res.pending_withdraw_amount.amount)
			
		except Exception:
			pass