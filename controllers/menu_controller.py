import vues.windowParametre as v_parametreWindow


class Menu_controller():

	def __init__(self, appli):
		self.appli = appli

	def afficher_menuParametre(self):
		v_parametreWindow.Window_parametre(self.appli)

	def lancer_acquisition(self):
		self.appli.acquisition()
