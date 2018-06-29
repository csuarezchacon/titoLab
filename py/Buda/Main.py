import time

from Balances import Balances
from History import History
from Logger import *
from MACD import MACD
from Order import Order
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'
cur = 'ETH'

limit = float(0.001)

minTrade = float(0.002000000)

#macd = MACD()
flgBid = False

hstOld = History()
hstOld.getHistory(False, mkt)

tkrOld = Ticker()
tkrOld.getTicker(mkt)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | MAXBID | MINASK |" )

try:
	logging.info("| RESUMEN | " + str(hstOld.o) + " | " + str(hstOld.h) + " | " + str(hstOld.l) + " | " + str(hstOld.c) + " | " +
		str(tkrOld.last_price) + " | " + str(tkrOld.max_bid) + " | " + str(tkrOld.min_ask) + " |" )
except:
	 logging.info("Error inesperado al iniciar valores")

while True:
	try:
		flgNew = False
		indBuy = ""
		indSell = ""

		bidId = 0
		bidLimitAmount = float(0)
		askId = 0
		askLimitAmount = float(0)

		#blncs = Balances()
		#blncs.getBalances(cur)

		order = Order()
		order.myOrders(mkt, 'pending')

		if len(order.orderList.orders) > 0:
			for it in order.orderList.orders:
				if it.type == 'Ask':
					askId = it.id
					askLimitAmount = it.limit.amount
					break
				elif it.type == 'Bid':
					bidId = it.id
					bidLimitAmount = it.limit.amount
					break

		hstNew = History()
		hstNew.getHistory(False, mkt)

		tkrNew = Ticker()
		tkrNew.getTicker(mkt)

		#macd.setEMAs(hstNew.c)
		#macd.getMACD(hstNew.c)

		#if hstNew.o < hstNew.c:
		#	print("tendencia bullish")
		#if hstNew.o > hstNew.c:
		#	print("tendencia bearish") #Comprar solo cuando existe 

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price) or (tkrNew.max_bid != tkrOld.max_bid) or (tkrNew.min_ask != tkrOld.min_ask)):
				flgNew = True

		if flgNew:
			msgAsk = ''
			msgBid = ''
			
			if ((tkrNew.min_ask != tkrOld.min_ask) and flgBid):
				if askId != 0:
					order.cancel(askId)
					msgAsk = msgAsk + 'orden ask ' + str(askId) + ' cancelada, '
				order.new(mkt, 'ask', limit, tkrNew.min_ask)
				print(msgAsk + 'se creó nueva orden ask')

			if tkrNew.max_bid != tkrOld.max_bid:
				if bidId != 0:
					order.cancel(bidId)
					msgBid = msgBid + 'orden bid ' + str(bidId) + ' cancelada, '
				order.new(mkt, 'bid', limit, tkrNew.max_bid)
				print(msgBid + 'se creó nueva orden bid')
				flgBid = True

			logging.info("| RESUMEN | " + str(hstNew.o) + " | " + str(hstNew.h) + " | " + str(hstNew.l) + " | " + str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " + str(tkrNew.max_bid) + " | " + str(tkrNew.min_ask) + " | ")

			hstOld = hstNew
			tkrOld = tkrNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	#time.sleep(5)