from modeles.baseOscillo import BaseOscillo
from pyvisa.resources.usb import USBInstrument

class Oscillo(USBInstrument, BaseOscillo):

	def initialisation(self):
		pass