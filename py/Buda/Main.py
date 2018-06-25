import time

from Balances import Balances
from Core import Core
from History import History
from Logger import *
from MACD import MACD
from Order import Order
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'
cur = 'ETH'

amntBuyDif = float(3000)
amntSellDif = float(1000)

minTrade = float(0.002000000)

macd = MACD()

cr = Core()

hstOld = History()
hstOld.getHistory(False, mkt)

tkrOld = Ticker()
tkrOld.getTicker(mkt)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | BUY | SELL |" )

try:
	logging.info("| RESUMEN | " + str(hstOld.o) + " | " + str(hstOld.h) + " | " + str(hstOld.l) + " | " + str(hstOld.c) + " | " +
		str(tkrOld.last_price) + " | " + " | " + " |" )
except:
	 logging.info("Error inesperado al iniciar valores")
	
while True:
	try:
		flgNew = False
		indBuy = ""
		indSell = ""

		blncs = Balances()
		blncs.getBalances(cur, cr)

		hstNew = History()
		hstNew.getHistory(False, mkt)

		tkrNew = Ticker()
		tkrNew.getTicker(mkt)

		#macd.setEMAs(hstNew.c)
		#macd.getMACD(hstNew.c)
		
		if hstNew.o < hstNew.c:
			print("ver menor valor")
		if hstNew.o > hstNew.c:
			print("ver mayor precio")

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price)):
				flgNew = True

		if flgNew:

			logging.info("| RESUMEN | " + str(hstNew.o) + " | " + str(hstNew.h) + " | " + str(hstNew.l) + " | " + str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " + indBuy + " | " + indSell + " | ")

			hstOld = hstNew
			tkrOld = tkrNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	#time.sleep(5)