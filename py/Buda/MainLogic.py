import time

lastO = lastH = lastL = lastC = lastT = float(0)
dAmntSafe = float(0) #monto de desicion Safe
dAmntRisk = float(50000) #monto de desicion Risk

fFrst = True
fHigh = False
fSfTr = False #Safe Trade

cntHg = 0
trdSt = 0	#0: off
			#1: buy
			#2: wait
			#3: sell
			#4: cancel

def tradeInfo(newO, newH, newL, newC, newT):
	global cntHg, fFrst, fHigh, fSfTr, lastO, lastH, lastL, lastC, lastT, trdSt

	if not(fFrst):
		
		#Safe tradding
		if ((newH > (lastH + dAmntSafe)) and (newH > newT)):
				cntHg += 1
				fHigh = True
		else:
			trdSt = 0
			fHigh = False

		if fHigh:
			fSfTr = True
			if trdSt < 1 or trdSt > 2:
				trdSt = 1
			else:
				if cntHg < 2:
					trdSt = 1
				else:
					trdSt = 2
		else:
			if cntHg > 0:
				cntHg = 0
				trdSt = 3
			else:
				#Risk tradding
				#REVISAR
				fSfTr = False
				if ((newC > (newT + dAmntRisk)) and (newT == lastC)):
					trdSt = 1
				elif((trdSt == 1) and not(newT == lastC)):
					trdSt = 2
				elif((trdSt == 2) and not(newT == lastC)):
					trdSt = 4
				elif(trdSt == 1 or trdSt == 2):
					trdSt = 3

	statChoices = {'0': '--', '1': 'buy', '2': 'wait', '3': 'sell'}
	if fSfTr:
		print("SAFE TRADE: " + statChoices.get(str(trdSt), "no valido"))
	else:
		print("RISK TRADE: " + statChoices.get(str(trdSt), "no valido"))


	fFrst = False

	lastO = newO
	lastH = newH
	lastL = newL
	lastC = newC
	lastT = newT

