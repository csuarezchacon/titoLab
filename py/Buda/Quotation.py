import json
import requests
import time

from Logger import *

class Quotation():
	amount = float(0)
	base_balance_change = float(0)
	base_exchanged = float(0)
	fee = float(0)
	order_amount = float(0)
	quote_balance_change = float(0)
	quote_exchanged = float(0)

	def setQuotation(self, inAmount, inBaseBalanceChange, inBaseExchanged, inFee, inOrderAmount, inQuoteBalanceChange, inQuoteExchanged):
		self.amount = float(inAmount)
		self.base_balance_change = float(inBaseBalanceChange)
		self.base_exchanged = float(inBaseExchanged)
		self.fee = float(inFee)
		self.order_amount = float(inOrderAmount)
		self.quote_balance_change = float(inQuoteBalanceChange)
		self.quote_exchanged = float(inQuoteExchanged)

	def getQuotation(self, inMkt, inType, inAmount):
		try:
			if inType =="BUY":
				valType = "bid_given_earned_base"
			else:
				valType = "ask_given_spent_base"
				
			url = 'https://www.buda.com/api/v2/markets/' + inMkt + '/quotations.json'
			paramData = {"type": valType, "limit": None, "amount": inAmount, "market_id": None}
			req = requests.post(url, data=paramData)

			qttJson = json.loads(req.text)
			self.setQuotation(qttJson['quotation']['amount'][0], 
				qttJson['quotation']['base_balance_change'][0], 
				qttJson['quotation']['base_exchanged'][0], 
				qttJson['quotation']['fee'][0], 
				qttJson['quotation']['order_amount'][0], 
				qttJson['quotation']['quote_balance_change'][0], 
				qttJson['quotation']['quote_exchanged'][0])
			
		except requests.exceptions.ConnectionError:
			pass