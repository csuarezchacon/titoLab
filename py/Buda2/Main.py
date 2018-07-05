from Constant import *
from Logger import *

from History import History
from Ticker import Ticker

initialize_logger('log')

hstOld = History()
tkrOld = Ticker()

def prntLog(inHst, inTkr):
#	logging.info("| RES | " + 
#		str(inHst.ohlc[0]['o']) + " | " + str(inHst.ohlc[0]['h']) + " | " + str(inHst.ohlc[0]['l']) + " | " + str(inHst.ohlc[0]['c']) + " | " + 
#		str(inTkr.last_price) + " | " + str(inTkr.max_bid) + " | " + str(inTkr.min_ask) + " |" )
	logging.info(str(inHst.ohlc) + "\n\n" + str(inHst.ohlcAvrg))

try:
	hstOld.getHistory(dtRng60, mS60, mkt)
	tkrOld.getTicker(mkt)
	
	logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | MAXBID | MINASK |" )

	prntLog(hstOld, tkrOld)
except:
	logging.info("Error inesperado al iniciar valores")

try:
	while True:
		hstNew = History()
		tkrNew = Ticker()

		hstNew.getHistory(dtRng60, mS60, mkt)
		tkrNew.getTicker(mkt)

		if ((hstOld.ohlc[0]['c'] != hstNew.ohlc[0]['c']) or (tkrOld.max_bid != tkrNew.max_bid) or (tkrOld.min_ask != tkrNew.min_ask)):
			prntLog(hstNew, tkrNew)

		hstOld = hstNew
		tkrOld = tkrNew

except Exception as e:
	logging.info("Error inesperado: " + str(e))