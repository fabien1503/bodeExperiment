from modeles.baseInstru import BaseInstrument

class BaseGBF(BaseInstrument):

	def initialisation(self, F_min):
		self.setForme('sin')
		self.setFrequence(F_min)
		self.setOffset(0)
		self.setAmplitude('2.00e+01')
		

	def setForme(self, forme):
		raise NotImplementedError

	def setFrequence(self, F):
		raise NotImplementedError

	def setAmplitude(self, ampl):
		raise NotImplementedError

	def setOffset(self, offset):
		raise NotImplementedError