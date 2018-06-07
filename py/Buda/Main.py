import time
import requests

from Quotation import Quotation
from History import History
from Logger import *
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'

amountValue = float(0.0015)
buyOldValue = float(0)
selOldlValue = float(0)

hstOld = History()
hstOld.getHistory(False, mkt)

tkrOld = Ticker()
tkrOld.getTicker(mkt)

qttBuyOld = Quotation()
qttBuyOld.getQuotation(mkt,"BUY", amountValue)

qttSellOld = Quotation()
qttSellOld.getQuotation(mkt,"SELL", amountValue)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | VAL BUY | VAL SELL | BUY | SELL |" )

try:
	buyOldValue = qttBuyOld.quote_balance_change / qttBuyOld.base_balance_change
	sellOldValue = qttSellOld.quote_balance_change / qttSellOld.base_balance_change

	logging.info("| RESUMEN | " +
		str(hstOld.o) + " | " +
		str(hstOld.h) + " | " +
		str(hstOld.l) + " | " +
		str(hstOld.c) + " | " +
		str(tkrOld.last_price) + " | " +
		str(abs(round(buyOldValue, 2))) + " | " + 
		str(abs(round(sellOldValue, 2))) + " |" )
except:
	 logging.info("Error inesperado al iniciar valores")
	
while True:
	try:
		flgNew = False

		buyNewValue = float(0)
		sellNewValue = float(0)

		qttBuyNew = Quotation()
		qttBuyNew.getQuotation(mkt,"BUY", amountValue)

		qttSellNew = Quotation()
		qttSellNew.getQuotation(mkt,"SELL", amountValue)

		buyNewValue = qttBuyNew.quote_balance_change / qttBuyNew.base_balance_change
		sellNewValue = qttSellNew.quote_balance_change / qttSellNew.base_balance_change

		hstNew = History()
		hstNew.getHistory(False, mkt)

		tkrNew = Ticker()
		tkrNew.getTicker(mkt)

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0) and (buyNewValue != 0) and (sellNewValue != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price) or (buyNewValue != buyOldValue) or (sellNewValue != sellOldValue)):
				flgNew = True

		if flgNew:

			logging.info("| RESUMEN | " +
				str(hstNew.o) + " | " +
				str(hstNew.h) + " | " +
				str(hstNew.l) + " | " +
				str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " +
				str(abs(round(buyNewValue, 2))) + " | " +
				str(abs(round(sellNewValue, 2))) + " | ")

			hstOld = hstNew
			tkrOld = tkrNew

			buyOldValue = buyNewValue
			sellOldValue = sellNewValue

			qttBuyOld = qttBuyNew
			qttSellOld = qttSellNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	#time.sleep(5)