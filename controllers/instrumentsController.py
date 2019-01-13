import visa 
from pyvisa.errors import VisaIOError
import re

class InstrumentController(visa.ResourceManager):

	def listeInstruments(self):
		return self.list_resources()

	def checkConnexion(self, instrument, varInstrument):

		try:
			instru = self.getInstru(varInstrument)
		except VisaIOError as e:
			print(e)
			return False
		finally:
			try:
				instru.close()
			except UnboundLocalError as e:
				pass

		return True


	def checkCommunication(self, instrument, varInstrument):

		try:
			instru = self.getInstru(varInstrument)
			idnInstru = instru.query('*idn?').split(",")[0] #On ne garde que le nom de l'appareil
		except VisaIOError as e:
			print(e)
			return False
		finally:
			try:
				instru.close()
			except UnboundLocalError as e:
				pass

		return True

	def checkReconnaissance(self, instrument, varInstrument):
		pass

	def getInstru(self, varInstrument):
		#Si c'est un instrument port COM on précise le baud rate
		if re.match('^ASRL', varInstrument):
			return self.open_resource(varInstrument, baud_rate=19200)
		#Si c'est un intrument USB on ne précise pas le baud rate
		if re.match('^USB', varInstrument):
			return self.open_resource(varInstrument)

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