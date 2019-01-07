import visa 

class InstrumentController():

	def __init__(self):
		self.ic = visa.ResourceManager()



	def listeInstruments(self):
		return self.ic.list_resoureces()