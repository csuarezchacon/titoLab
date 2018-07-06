from Constant import *
from Logger import *

from Balances import Balances
from History import History
from Order import Order
from Ticker import Ticker

initialize_logger('log')

hstOld = History()
tkrOld = Ticker()

def prntLog(inHst, inTkr):
	cnd = inHst.ohlc[-1] # Candle
	tnd = 'V' if cnd['o'] <= cnd['c'] else 'R' # Tending Verde o Rojo

	logging.info("| " + tnd + " | " + str(cnd['o']) + " | " + str(cnd['h']) + " | " + str(cnd['l']) + " | " + str(cnd['c']) + " | " + 
		str(inTkr.last_price) + " | " + str(inTkr.max_bid) + " | " + str(inTkr.min_ask) + " |" )
#	logging.info(str(inHst.ohlc) + "\n\n" + str(inHst.ohlcAvrg))

def pendiengOrders(inOrderList):
	bidOrder = {'oId':0, 'oType':'', 'oLimit':float(0)}
	askOrder = {'oId':0, 'oType':'', 'oLimit':float(0)}

	if len(inOrderList) > 0:

		for i in inOrderList:
			if ((i.type == 'Bid') and (bidOrder['oId'] == 0)):
				bidOrder = {'oId':i.id, 'oType':i.type, 'oLimit':i.limit[0]}

			if ((i.type == 'Ask') and (askOrder['oId'] == 0)):
				askOrder = {'oId':i.id, 'oType':i.type, 'oLimit':i.limit[0]}

			if ((bidOrder['oId'] != 0) and (askOrder['oId'] != 0)):
				break

	return bidOrder, askOrder

try:
	#hstOld.getHistory(dtRng60, mS60, mkt)
	#tkrOld.getTicker(mkt)
	
	logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | MAXBID | MINASK |" )

	prntLog(hstOld, tkrOld)
except:
	logging.info("Error inesperado al iniciar valores")

try:
	while True:
		flgNew = False
		
		blc = Balances()
		order = Order()

		hstNew = History()
		tkrNew = Ticker()

		hstNew.getHistory(dtRng60, mS60, mkt)
		tkrNew.getTicker(mkt)

		order.myOrders(mkt, 'pending')

		blc.getBalances(curClp)
		flgBid = blc.available_amount > minBid

		blc.getBalances(curBtc)
		flgAsk = blc.available_amount > minAsk

		cndlOld = hstOld.ohlc[-1]
		cndlNew = hstNew.ohlc[-1]
		
		if ((cndlNew['o'] != 0) and (cndlNew['h'] != 0) and (cndlNew['l'] != 0) and (cndlNew['c'] != 0) and (tkrNew.last_price != 0) and (tkrNew.max_bid != 0) and (tkrNew.min_ask != 0)):
			if ((cndlOld['o'] != cndlNew['o']) or (cndlOld['h'] != cndlNew['h']) or (cndlOld['l'] != cndlNew['l']) or (cndlOld['c'] != cndlNew['c']) or (tkrOld.last_price != tkrNew.last_price) or (tkrOld.max_bid != tkrNew.max_bid) or (tkrOld.min_ask != tkrNew.min_ask)):
				flgNew = True

		if flgNew:
			prntLog(hstNew, tkrNew)

			pendingBid, pendingAsk = pendiengOrders(order.orderList.orders)

			print('bid: ' + str(pendingBid))
			print('ask: ' + str(pendingAsk))

			hstOld = hstNew
			tkrOld = tkrNew

except Exception as e:
	logging.info("Error inesperado: " + str(e))