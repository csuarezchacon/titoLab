
class MACD():
	arrEma12 = []
	arrEma26 = []

	mul12 = 2 / (12 + 1)
	mul26 = 2 / (26 + 1)
	
	def setEMAs(self, price):
		if len(self.arrEma12) == 12:
			self.arrEma12.pop(0)
		if len(self.arrEma12) < 12:
			self.arrEma12.append(price)

		if len(self.arrEma26) == 26:
			self.arrEma26.pop(0)
		if len(self.arrEma26) < 26:
			self.arrEma26.append(price)

	def getMACD(self, price):
		sumEma12 = float(0)
		sumEma26 = float(0)

		if ((len(self.arrEma12) == 12) and (len(self.arrEma26) == 26)):
			for i in self.arrEma12:
				sumEma12 = sumEma12 + i
			for i in self.arrEma26:
				sumEma26 = sumEma26 + i
			
			sma12 = sumEma12/len(self.arrEma12)
			ema12 = self.mul12 * price + (1 - self.mul12) #* ema anterior
			sma26 = sumEma26/len(self.arrEma26)
			ema26 = self.mul26 * price + (1 - self.mul26) #* ema anterior

			print(ema12-ema26)