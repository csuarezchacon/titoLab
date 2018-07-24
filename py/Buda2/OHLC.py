class OHLC():
	o = float(0)
	h = float(0)
	l = float(0)
	c = float(0)

	def setOHLC(self, inO, inH, inL, inC):
		self.o = inO
		self.h = inH
		self.l = inL
		self.c = inC