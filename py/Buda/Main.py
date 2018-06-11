import time

from History import History
from Logger import *
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'

hstOld = History()
#hstOld.getHistory(False, mkt)

tkrOld = Ticker()
#tkrOld.getTicker(mkt)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | BUY | SELL |" )

try:

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

		hstNew = History()
		hstNew.getHistory(False, mkt)

		tkrNew = Ticker()
		tkrNew.getTicker(mkt)

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price)):
				flgNew = True

		if flgNew:

			difHL = hstOld.h - hstOld.l #Tamaño de trade
			difOL = hstOld.o - hstOld.l #Ubicación del Open
			difCL = hstOld.c - hstOld.l #Ubicación del Close

			difBy = difHL - difCL #Si sube validar compra

			logging.info("| RESUMEN | " +
				str(hstNew.o) + " | " +
				str(hstNew.h) + " | " +
				str(hstNew.l) + " | " +
				str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " +
				" | " +
				" | ")

			hstOld = hstNew
			tkrOld = tkrNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	#time.sleep(5)