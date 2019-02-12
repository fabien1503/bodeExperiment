from modeles.baseGBF import BaseGBF
from pyvisa.resources.serial import SerialInstrument

class GBF(SerialInstrument, BaseGBF):

	def allumer(self):
		self.write('syst:pow ON')