import vues.windowParametre as v_parametreWindow


class Menu_controller():

	def __init__(self, appli):
		self.appli = appli

	def afficher_menuParametre(self):
		v_parametreWindow.Window_parametre(self.appli)

	def lancer_acquisition(self):
		self.appli.acquisition()

	def enregistrerCourbe(self):
		self.appli.enregistrerCourbe()

	def effacerCourbes(self):
		for line in self.appli.fenetre_princ.axGain.get_lines():
			line.set_data(list(), list())
		for line in self.appli.fenetre_princ.axPhase.get_lines():
			line.set_data(list(), list())

		self.appli.listeCourbes = list()

		self.appli.fenetre_princ.graph.draw()
		
