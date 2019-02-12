from modeles.baseGBF import BaseGBF
from pyvisa.resources.serial import SerialInstrument

class GBF(SerialInstrument, BaseGBF):

	def initialisation(self, F_min):
		self.allumer()
		super().initialisation(F_min)
		self.setOutput('ON')

	def allumer(self):
		self.write('syst:pow ON')

	def setForme(self, forme):
		self.write('source:func '+forme)

	def setFrequence(self, F):
		self.write('source:freq '+str(F))

	def setAmplitude(self, ampl):
		self.write('source:volt '+str(ampl))

	def setOffset(self, offset):
		self.write('source:volt:offset '+str(offset))

	def setOutput(self, state):
		self.write('output '+str(state))

	def eteindre(self):
		self.write('syst:pow OFF')

	def __del__(self):
		self.eteindre()
		super().__del__()