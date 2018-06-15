from Logger import *
from trading_api_wrappers import Buda

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

	def getBalances(self, inCur, inK, inS):
		try:
			buda = Buda.Auth(inK, inS)
			res = buda.balance(inCur)
			#print(res)
			self.setBalances(res.id,
				res.amount.amount,
				res.available_amount.amount,
				res.frozen_amount.amount,
				res.pending_withdraw_amount.amount)
			
		except Exception:
			pass