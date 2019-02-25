from modeles.baseInstru import BaseInstrument

class BaseOscillo(BaseInstrument):

	def initialisation(self):
		#Pour chaque voie:
		for i in [1, 2]:
			self.afficherVoie(i) #les afficher
			self.setVoieDC(i) #les mettre en DC
			self.setVoieOffset(i, 0) #centrer les voies sur l'écran
			self.attenuationVoie(i, 1) #mettre l'attenuation à 1 

		self.setTrigger(2, 'AUTO')#trigger voie 2 en mode auto

		self.setMeasure() #afficher les mesures d'amplitude et de phase

		#Puis on règle les sensibités horizontale et verticale
		self.reglagesSensibilite()

	def setVoieDC(self, voie):
		raise NotImplementedError

	def afficherVoie(self, voie):
		raise NotImplementedError

	def setVoieOffset(self, voie, offset):
		raise NotImplementedError

	def attenuationVoie(self, voie, atte):
		raise NotImplementedError 

	def setTrigger(self, voie, mode):
		raise NotImplementedError

	def setMeasure(self):
		raise NotImplementedError 

	def reglagesSensibilite(self):
		raise NotImplementedError

	def mesureAmplitude(self, voie):
		raise NotImplementedError

	def mesurePhase(self):
		raise NotImplementedError





