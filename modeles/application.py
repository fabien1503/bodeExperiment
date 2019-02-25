import vues.fenetre_princ as main_fene
import time
from singleton_decorator import singleton
from math import log10

@singleton
class Appli():

	def __init__(self):

		#Dictionnaire des paramètres d'acquisition
		self.acquisitionParametre = {"F_min": 100,
									"F_max": 10**5,
									"nb_points": 30}

		#---------On définit la fenêtre principale------------------#
		self.fenetre_princ = main_fene.Fenetre_princ(self)

		self.GBF = None
		self.oscillo = None

		self.listeCourbes = list()

	
	def run(self):
		self.fenetre_princ.mainloop()


	def acquisition(self):

		#On calcule toutes les fréquences à utiliser :
		listeFrequences = [int(10**i) for i in drange(log10(self.acquisitionParametre['F_min']),
			log10(self.acquisitionParametre['F_max']), 
			(log10(self.acquisitionParametre['F_max'])-log10(self.acquisitionParametre['F_min']))/(self.acquisitionParametre['nb_points']-1))]
		#On initialise les listes de gain et de phase
		listeGain = list()
		listePhase = list()
		listeFrequence = list() # liste qui servira a tracer

		#Puis on fait varier la fréquence et on prend les mesures
		for frequence in listeFrequences:
			self.GBF.setFrequence(frequence)
			self.oscillo.reglagesSensibilite()
			#time.sleep(0.5)


			listeGain.append(20*log10(self.oscillo.mesureAmplitude(1)/self.oscillo.mesureAmplitude(2)))
			listePhase.append(self.oscillo.mesurePhase())
			listeFrequence.append(frequence)

			self.fenetre_princ.lineGain.set_data(listeFrequence, listeGain)
			self.fenetre_princ.linePhase.set_data(listeFrequence, listePhase)
			self.fenetre_princ.axGain.set_ylim(bottom=min(listeGain)-1, top=max(listeGain)+1)
			self.fenetre_princ.graph.draw()
			self.fenetre_princ.update_idletasks()

	def enregistrerCourbe(self):
		listeCouleur = ['blue', 'green', 'gray', 'purple', 'orange', 'pink', 'cyan']
		#On copie les courbes :
		courbeGain = self.fenetre_princ.lineGain
		courbePhase = self.fenetre_princ.linePhase
		#On change les couleurs :
		courbeGain.set_marker('o')
		courbeGain.set_color(listeCouleur[len(self.listeCourbes)])
		courbePhase.set_marker('o')
		courbePhase.set_color(listeCouleur[len(self.listeCourbes)])
		#On défini de nouvelles courbes pour le tracé :
		self.fenetre_princ.lineGain, = self.fenetre_princ.axGain.plot([], [], 'r+')
		self.fenetre_princ.linePhase, = self.fenetre_princ.axPhase.plot([], [], 'r+')

		#On enregistre les courbes dans liste courbes :
		self.listeCourbes.append((courbeGain, courbePhase))

		#On trace :
		self.fenetre_princ.graph.draw()










def drange(start, stop, step):#Generateur pour des doubles
	x = start
	while x <= stop+0.000001:#evite les pb d'arrondi
		yield x
		x += step