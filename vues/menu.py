import tkinter as tk

import controllers.menu_controller as controller


class Menu(tk.Menu):

	def __init__(self, parent):
		self.controller = controller.Menu_controller(parent.appli)

		#----Création du menu principal----------------#
		super().__init__(parent)
		
		#----Création du menu fichier----------------#
		self.menu_fichier = tk.Menu(self, tearoff=0)

		self.menu_fichier.add_command(label="Quitter", command=parent.quit)

		#----Création menu acquisition-------------------#
		self.menu_acquisition = tk.Menu(self, tearoff=0)

		self.menu_acquisition.add_command(label="Paramètres", command=self.controller.afficher_menuParametre)
		self.menu_acquisition.add_command(label="Lancement", command=self.controller.lancer_acquisition, accelerator='F10')

		self.menu_acquisition.bind_all('<Key-F10>', lambda event : self.controller.lancer_acquisition())


		self.add_cascade(label="Fichier", menu=self.menu_fichier)
		self.add_cascade(label="Acquisition", menu=self.menu_acquisition)