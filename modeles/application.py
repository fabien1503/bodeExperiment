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

	
	def run(self):
		self.fenetre_princ.mainloop()


	def acquisition(self):

		#On calcule toutes les fréquences à utiliser :
		listeFrequences = [int(10**i) for i in drange(log10(self.acquisitionParametre['F_min']),
			log10(self.acquisitionParametre['F_max']), 
			(log10(self.acquisitionParametre['F_max'])-log10(self.acquisitionParametre['F_min']))/self.acquisitionParametre['nb_points'])]

		#Puis on fait varier la fréquence et on prend les mesures
		for frequence in listeFrequences:
			self.GBF.setFrequence(frequence)
			time.sleep(1)




def drange(start, stop, step):#Generateur pour des doubles
	x = start
	while x <= stop:
		yield x
		x += step