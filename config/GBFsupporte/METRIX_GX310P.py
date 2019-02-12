from modeles.baseGBF import BaseGBF
from pyvisa.resources.serial import SerialInstrument

class GBF(SerialInstrument, BaseGBF):

	def initialisation(self):
		self.allumer()

	def allumer(self):
		self.write('syst:pow ON')

	def eteindre(self):
		self.write('syst:pow OFF')

	def __del__(self):
		self.eteindre()
		super().__del__()