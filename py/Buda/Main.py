import time

from Balances import Balances
from Core import Core
from History import History
from Logger import *
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'
cur = 'ETH'
amntSellDif = float(0)

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
		blncs.getBalances(cur, cr.k, cr.s)

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
			
			#if difCLNew > difOLNew:
			#	if blncs.available_amount > 0.002000000:
					#print('monto disponible permite comprar')
			#		if ((difBuyNew + amntSellDif) > difBuyOld):
			#			indBuy = "SELL"
			#		elif ((difBuyNew - amntSellDif) < difBuyOld):
			#			indBuy = "BUY"
				#else:
				#	print('monto disponible NO permite vender')

			if hstNew.c != hstOld.c:
				if blncs.available_amount > 0.002000000:
					if hstNew.c > hstOld.c:
						indBuy = "SELL"
				elif hstNew.c < hstOld.c:
					indSell = "BUY"

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

#2018-06-16 23:42:36 [INFO] | RESUMEN | 317000,0 | 317000,0 | 317000,0 | 317000,0 | 317000,0 |  |  | 
#2018-06-16 23:58:34 [INFO] | RESUMEN | 317000,0 | 317100,0 | 317000,0 | 317100,0 | 317000,0 |  |  | 
#2018-06-16 23:58:58 [INFO] | RESUMEN | 317000,0 | 317100,0 | 317000,0 | 317100,0 | 317100,0 |  |  | 
#2018-06-17 00:07:58 [INFO] | RESUMEN | 317000,0 | 328844,78 | 317000,0 | 328844,78 | 317100,0 |  |  | 
#2018-06-17 00:08:07 [INFO] | RESUMEN | 317000,0 | 328844,78 | 317000,0 | 328844,78 | 328844,78 |  |  | 