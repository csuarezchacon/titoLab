from Constant import *
from Logger import *

from Balances import Balances
from History import History
from Order import Order
from Ticker import Ticker

initialize_logger('log')

hstOld = History()
tkrOld = Ticker()

order = Order()

def prntLog(inHst, inTkr):
	cnd = inHst.ohlcList[-1] # Candle
	tnd = 'V' if cnd.o <= cnd.c else 'R' # Tending Verde o Rojo

	logging.info("| " + tnd + " | " + str(cnd.o) + " | " + str(cnd.h) + " | " + str(cnd.l) + " | " + str(cnd.c) + " | " + 
		str(inTkr.last_price) + " | " + str(inTkr.max_bid) + " | " + str(inTkr.min_ask) + " |" )
#	logging.info(str(inHst.ohlcList) + "\n\n" + str(inHst.ohlcAvrg))

def bidAskOrders(inStatus):
	order.myOrders(mkt, inStatus)
	
	bidOrder = {'oId':0, 'oType':'', 'oLimit':float(0)}
	askOrder = {'oId':0, 'oType':'', 'oLimit':float(0)}

	if len(order.orderList.orders) > 0:

		for i in order.orderList.orders:
			if ((i.type == 'Bid') and (bidOrder['oId'] == 0)):
				bidOrder = {'oId':i.id, 'oType':i.type, 'oLimit':i.limit[0]}

			if ((i.type == 'Ask') and (askOrder['oId'] == 0)):
				askOrder = {'oId':i.id, 'oType':i.type, 'oLimit':i.limit[0]}

			if ((bidOrder['oId'] != 0) and (askOrder['oId'] != 0)):
				break

	return bidOrder, askOrder

def newOrder(inId, inType, inAmount):
	msg = '' 

	if inId != 0:
		order.cancel(inId)
		msg = msg + 'orden ' + inType + ' ' + str(inId) + ' cancelada, '

	order.new(mkt, inType, limit, inAmount)
	print(msg + 'se creo nueva orden ' + inType)

try:
	hstOld.getHistory(dtRng60, mS60, mkt)
	tkrOld.getTicker(mkt)
	
	logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | MAXBID | MINASK |" )

	prntLog(hstOld, tkrOld)
except:
	logging.info("Error inesperado al iniciar valores")

try:
	while True:
		flgNew = False
		
		blc = Balances()

		hstNew = History()
		tkrNew = Ticker()

		hstNew.getHistory(dtRng60, mS60, mkt)
		tkrNew.getTicker(mkt)

		blc.getBalances(curClp)
		flgBid = blc.available_amount > minBid

		blc.getBalances(curBtc)
		flgAsk = blc.available_amount > minAsk

		cndlOld = hstOld.ohlcList[-1]
		cndlNew = hstNew.ohlcList[-1]

		pendingBid, pendingAsk = bidAskOrders('pending')
		tradedBid, tradedAsk = bidAskOrders('traded')
		
		if cndlNew.o <= cndlNew.c:
			if ((flgBid == True) and (pendingBid['oId'] == 0)):
				#newOrder(pendingBid['oId'], 'bid', tkrNew.max_bid)
				pass
			if ((flgAsk == True) and (pendingAsk['oId'] == 0)):
				#newOrder(pendingAsk['oId'], 'ask', tkrNew.min_ask)
				pass

		if ((cndlNew.o != 0) and (cndlNew.h != 0) and (cndlNew.l != 0) and (cndlNew.c != 0) and (tkrNew.last_price != 0) and (tkrNew.max_bid != 0) and (tkrNew.min_ask != 0)):
			if ((cndlOld.o != cndlNew.o) or (cndlOld.h != cndlNew.h) or (cndlOld.l != cndlNew.l) or (cndlOld.c != cndlNew.c) or (tkrOld.last_price != tkrNew.last_price) or (tkrOld.max_bid != tkrNew.max_bid) or (tkrOld.min_ask != tkrNew.min_ask)):
				flgNew = True

		if flgNew:
			#prntLog(hstNew, tkrNew)

			if cndlNew.o <= cndlNew.c:
				if flgBid:
					if ((tkrOld.max_bid != 0) and (tkrOld.max_bid != tkrNew.max_bid)):
						#newOrder(pendingBid['oId'], 'bid', tkrNew.max_bid)
						pass
				if flgAsk:
					if ((tkrOld.min_ask != 0) and (tkrOld.min_ask != tkrNew.min_ask)):
						#newOrder(pendingAsk['oId'], 'ask', tkrNew.min_ask)
						pass

			hstOld = hstNew
			tkrOld = tkrNew

except Exception as e:
	logging.info("Error inesperado: " + str(e))