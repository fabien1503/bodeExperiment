import visa 
from pyvisa.errors import VisaIOError
import re

class InstrumentController():

	def __init__(self):
		self.ic = visa.ResourceManager()


	def listeInstruments(self):
		return self.ic.list_resources()

	def instrumentVerification(self, instrument, varInstrument):

		listeInstrumentsSupporte = self.listeInstrumentsSupporte(instrument)

		try:
			instru = self.ic.open_resource(varInstrument.get(), baud_rate=19200)
			idnInstru = instru.query('*idn?').split(",")[0] #On ne garde que le nom de l'appareil
		except VisaIOError as e:
			print(e)
			return False
		finally:
			try:
				instru.close()
			except UnboundLocalError as e:
				pass

		if idnInstru in listeInstrumentsSupporte :
			return True
		else : return False

	def listeInstrumentsSupporte(self, instrument):

		with open('config/'+instrument+'supporte.txt', 'r') as fichier:
			listeInstrumentsSupporte = self.nettoyageListeInstrumentsSupporte(fichier.readlines())

		return listeInstrumentsSupporte

	#Fonction permettant de supprimer le \n en fin de ligne
	def nettoyageListeInstrumentsSupporte(self, listeInstruments):
		listeInstrumentsNettoye = list()
		for instrumentString in listeInstruments:
			listeInstrumentsNettoye.append(re.sub(r'(\n)$', '', instrumentString))

		return listeInstrumentsNettoye