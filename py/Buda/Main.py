import time

from History import History
from Logger import *
from Ticker import Ticker


import base64
import hashlib
import hmac
import json
import requests
from Core import Core
from trading_api_wrappers import Buda

initialize_logger('log')

mkt = 'eth-clp'

cr = Core()

#-------------------
def gen_nonce():
	# Get a str from the current time in microseconds.
	return str(int(time.time() * 1E6))

def build_route(inPath, inParams):
	retorno = inPath + inParams
	return retorno

def _sign_payload(method, path, params, payload):
	try:
		route = build_route(path, params)
		nonce = gen_nonce()
		if payload:
			j = json.dumps(payload).encode('utf-8')
			encoded_body = base64.standard_b64encode(j).decode('utf-8')
			string = method + ' ' + route + ' ' + encoded_body + ' ' + nonce
		else:
			string = method + ' ' + route + ' ' + nonce

		h = hmac.new(key=cr.s.encode('utf-8'), msg=string.encode('utf-8'), digestmod=hashlib.sha384)

		signature = h.hexdigest()

		return {
			'X-SBTC-APIKEY': cr.k,
			'X-SBTC-NONCE': nonce,
			'X-SBTC-SIGNATURE': signature,
			'Content-Type': 'application/json'
		}
	except Exception as e:
		print(e)

def getBalance():
	signature = _sign_payload('GET', '/api/v2/balances', '', False)
	
	signature['X-SBTC-APIKEY']
	signature['X-SBTC-SIGNATURE']

	buda = Buda.Auth(cr.k, cr.s)
	print(buda.balance('BTC'))
	
	#url = 'https://www.buda.com/api/v2/balances'
	
	#url = 'https://www.buda.com/api/v2/markets/' + mkt + '/orders'
	#res = requests.get(url, auth=(signature['X-SBTC-APIKEY'], signature['X-SBTC-SIGNATURE']))

	#print(res.text)
	#_sign_payload('GET', '/api/v2/balances', "", True)

#-------------------

hstOld = History()
hstOld.getHistory(False, mkt)

tkrOld = Ticker()
tkrOld.getTicker(mkt)

logging.info("| | OPEN | HIGH | LOW | CLOSE | LAST PRICE | BUY | SELL |" )

try:
	difHLOld = hstOld.h - hstOld.l #Tamaño de trade
	difOLOld = hstOld.o - hstOld.l #Ubicación del Open
	difCLOld = hstOld.c - hstOld.l #Ubicación del Close

	difBuyOld = difHLOld - difCLOld #Si sube validar compra

	logging.info("| RESUMEN | " +
		str(hstOld.o) + " | " +
		str(hstOld.h) + " | " +
		str(hstOld.l) + " | " +
		str(hstOld.c) + " | " +
		str(tkrOld.last_price) + " | " +
		" | " + 
		" |" )
	getBalance()
except:
	 logging.info("Error inesperado al iniciar valores")
	
while True:
	try:
		flgNew = False
		indBuy = ""

		hstNew = History()
		hstNew.getHistory(False, mkt)

		tkrNew = Ticker()
		tkrNew.getTicker(mkt)

		if ((hstNew.o != 0) and (hstNew.h != 0) and (hstNew.l != 0) and (hstNew.c != 0) and (tkrNew.last_price != 0)):
			if ((hstNew.o != hstOld.o) or (hstNew.h != hstOld.h) or (hstNew.l != hstOld.l) or (hstNew.c != hstOld.c) or (tkrNew.last_price != tkrOld.last_price)):
				flgNew = True

		if flgNew:

			difHLNew = hstNew.h - hstNew.l #Tamaño de trade
			difOLNew = hstNew.o - hstNew.l #Ubicación del Open
			difCLNew = hstNew.c - hstNew.l #Ubicación del Close

			difBuyNew = difHLNew - difCLNew #Si sube validar compra

			if difBuyNew > difBuyOld:
				indBuy = "TRUE"

			logging.info("| RESUMEN | " +
				str(hstNew.o) + " | " +
				str(hstNew.h) + " | " +
				str(hstNew.l) + " | " +
				str(hstNew.c) + " | " +
				str(tkrNew.last_price) + " | " +
				indBuy + " | " +
				" | ")

			hstOld = hstNew
			tkrOld = tkrNew
			difBuyOld = difBuyNew

	except Exception as e:
		logging.info("Error inesperado: " + str(e))
	#time.sleep(5)