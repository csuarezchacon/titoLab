import time

from Balances import Balances
from Core import Core
from History import History
from Logger import *
from Order import Order
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'
cur = 'ETH'

amntBuyDif = float(3000)
amntSellDif = float(1000)

minTrade = float(0.002000000)

cr = Core()

hstOld = History()
hstOld.getHistory(False, mkt)

tkrOld = Ticker()
tkrOld.getTicker(mkt)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | BUY | SELL |" )

try:
	difHLOld = hstOld.h - hstOld.l #Tamano de trade
	difOLOld = hstOld.o - hstOld.l #Ubicacion del Open
	difCLOld = hstOld.c - hstOld.l #Ubicacion del Close

	difBuyOld = difHLOld - difCLOld #Si sube validar compra

	logging.info("| RESUMEN | " +
		str(hstOld.o) + " | " +
		str(hstOld.h) + " | " +
		str(hstOld.l) + " | " +
		str(hstOld.c) + " | " +
		str(tkrOld.last_price) + " | " +
		" | " + 
		" |" )
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

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price)):
				flgNew = True

		if flgNew:

			difHLNew = hstNew.h - hstNew.l #Tamano de trade
			difOLNew = hstNew.o - hstNew.l #Ubicacion del Open
			difCLNew = hstNew.c - hstNew.l #Ubicacion del Close

			difBuyNew = difHLNew - difCLNew #Si sube validar compra
			
			#if hstNew.c != hstOld.c:
			#	if blncs.available_amount > 0.002000000:
			#		if ((hstNew.c + amntSellDif) > hstOld.c):
			#			indBuy = "SELL"
			#	elif ((hstNew.c + amntBuyDif) < hstOld.c):
			#		indSell = "BUY"

			if ((hstNew.c > (hstOld.c + amntSellDif)) or (hstNew.h > hstOld.h)):
				if blncs.available_amount > minTrade:
					indSell = "SELL" #ask
					ordNew = Order()
					ordNew.doOrder(mkt, cr, "ask", 0.001, hstNew.c)
					print(ordNew.order)


			if ((hstNew.c < (hstOld.c - amntBuyDif)) or (hstNew.l < hstOld.l)):
				#if tkrNew.last_price > hstNew.c:
				indBuy = "BUY" #bid
				ordNew = Order()
				ordNew.doOrder(mkt, cr, "bid", 0.001, hstNew.c)
				print(ordNew.order)

			logging.info("| RESUMEN | " +
				str(hstNew.o) + " | " +
				str(hstNew.h) + " | " +
				str(hstNew.l) + " | " +
				str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " +
				indBuy + " | " +
				indSell + " | ")

			hstOld = hstNew
			tkrOld = tkrNew
			difBuyOld = difBuyNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	#time.sleep(5)