import visa 
from pyvisa.errors import VisaIOError
import re
import os

class InstrumentController(visa.ResourceManager):

	def listeInstruments(self):
		return self.list_resources()

	def checkInstrument(self, instrument, varInstrument):

		try:
			instru = self.getInstru(varInstrument)
		except VisaIOError as e: #Erreur lors de la connexion
			print(e)
			return (False, False, False)
		else:
			try:
				idnInstru = instru.query('*idn?').split(",")[0] #On ne garde que le nom de l'appareil
			except VisaIOError as e: #Erreur lors de la communication
				print(e)
				return (True, False, False)
		finally:
			try:
				instru.close()
			except UnboundLocalError as e:
				pass

		try:
			if idnInstru in self.listeInstrumentsSupporte(instrument):
				return (True, True, True)
			else : return (True, True, False)# Instrument non reconnu
		except AttributeError as e:
			return (True, True, False)# Instrument non reconnu
		

	def getInstru(self, varInstrument, baud=19200, **kargs):
		#Si c'est un instrument port COM on précise le baud rate
		if re.match('^ASRL', varInstrument):
			return self.open_resource(varInstrument, baud_rate=baud, **kargs)
		#Si c'est un intrument USB on ne précise pas le baud rate
		if re.match('^USB', varInstrument):
			return self.open_resource(varInstrument, **kargs)

	def listeInstrumentsSupporte(self, instrument):

		listeFichiersSupportInstru = os.listdir('config/'+instrument+'supporte/')
		listeInstrumentsSupporte = list()

		for fichier in listeFichiersSupportInstru :
			listeInstrumentsSupporte.append(re.sub('(.py)$', '', re.sub('_', ' ', fichier)))

		return listeInstrumentsSupporte
