import vues.fenetre_princ as main_fene


class Appli():

	def __init__(self):

		#Dictionnaire des paramètres d'acquisition
		self.acquisitionParametre = {"F_min": 100,
									"F_max": 10**5,
									"nb_points": 30}

		#---------On définit la fenêtre principale------------------#
		self.fenetre_princ = main_fene.Fenetre_princ(self)

	
	def run(self):
		self.fenetre_princ.mainloop()