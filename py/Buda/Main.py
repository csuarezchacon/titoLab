import time
import requests

from History import History
from Logger import *
from Ticker import Ticker

initialize_logger('log')

mkt = 'eth-clp'

hstOld = History()
hstOld.getHistory(False, mkt)

tkrOld = Ticker()
tkrOld.getTicker(mkt)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | VAL BUY | VAL SELL | BUY | SELL |" )

try:
	logging.info("| RESUMEN | " +
		str(hstOld.o) + " | " +
		str(hstOld.h) + " | " +
		str(hstOld.l) + " | " +
		str(hstOld.c) + " | " +
		str(tkrOld.last_price) + " | " +
		str(tkrOld.max_bid) + " | " +
		str(tkrOld.min_ask) + " | | |" )
except:
	 logging.info("Error inesperado al iniciar valores")
	
while True:
	try:
		flgNew = False
		hstNew = History()
		hstNew.getHistory(False, mkt)

		tkrNew = Ticker()
		tkrNew.getTicker(mkt)

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0) and (tkrNew.max_bid != 0) and (tkrNew.min_ask != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price) or (tkrNew.max_bid != tkrOld.max_bid) or (tkrNew.min_ask != tkrOld.min_ask)):
				flgNew = True

		if flgNew:
			buyDscAmnt = float(100)
			buyStat = ""
			finalMaxBid = float(tkrNew.max_bid) + float(buyDscAmnt)
			if ((tkrNew.last_price < tkrNew.max_bid) and (finalMaxBid < tkrOld.max_bid)):
				buyStat = "BUY"

			sellDscAmnt = 100
			sellStat = ""
			finalMinAsk = float(tkrOld.min_ask) - float(sellDscAmnt)
			if ((tkrNew.last_price >= tkrNew.min_ask) and (tkrNew.min_ask > finalMinAsk)):
				sellStat = "SELL"

			logging.info("| RESUMEN | " +
				str(hstNew.o) + " | " +
				str(hstNew.h) + " | " +
				str(hstNew.l) + " | " +
				str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " +
				str(tkrNew.max_bid) + " | " +
				str(tkrNew.min_ask) + " | " +
				buyStat + " | " +
				sellStat + " | ")

			hstOld = hstNew
			tkrOld = tkrNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	time.sleep(5)

#def tradeInfo(newO, newH, newL, newC, newT):
#	global cntHg, fFrst, fHigh, fSfTr, lastO, lastH, lastL, lastC, lastT, trdSt
#
#	if not(fFrst):
#		
#		#Safe tradding
#		if ((newH > (lastH + dAmntSafe)) and (newH > newT)):
#				cntHg += 1
#				fHigh = True
#		else:
#			trdSt = 0
#			fHigh = False
#
#		if fHigh:
#			fSfTr = True
#			if trdSt < 1 or trdSt > 2:
#				trdSt = 1
#			else:
#				if cntHg < 2:
#					trdSt = 1
#				else:
#					trdSt = 2
#		else:
#			if cntHg > 0:
#				cntHg = 0
#				trdSt = 3
#			else:
#				#Risk tradding
#				#REVISAR
#				fSfTr = False
#				if ((newC > (newT + dAmntRisk)) and (newT == lastC)):
#					trdSt = 1
#				elif((trdSt == 1) and not(newT == lastC)):
#					trdSt = 2
#				elif((trdSt == 2) and not(newT == lastC)):
#					trdSt = 4
#				elif(trdSt == 1 or trdSt == 2):
#					trdSt = 3
#
#	statChoices = {'0': '--', '1': 'buy', '2': 'wait', '3': 'sell'}
#	if fSfTr:
#		print("SAFE TRADE: " + statChoices.get(str(trdSt), "no valido"))
#	else:
#		print("RISK TRADE: " + statChoices.get(str(trdSt), "no valido"))
#
#
#	fFrst = False
#
#	lastO = newO
#	lastH = newH
#	lastL = newL
#	lastC = newC
#	lastT = newT