import tkinter as tk
import re

from vues.choixParametres import ChoixParametre
from vues.choixInstruments import ChoixInstrument

import controllers.instrumentsController as ic


class Window_parametre(tk.Toplevel):

	def __init__(self, appli):
		self.appli = appli
		self.parametreAcquisition = appli.acquisitionParametre

		self.instruController = ic.InstrumentController()


		self.appli.GBF = None
		self.appli.oscillo = None
		

		#On commence par créer la nouvelle fenêtre
		super().__init__(appli.fenetre_princ, padx=4, pady=4)
		self.geometry("600x400+300+0")
		self.title("Paramètres d'acquisition")


		#-------------------Choix des paramètres d'acquisition
		self.cadreParametres = tk.LabelFrame(self, text="Choix des paramètres d'acquisition")
		self.cadreParametres.pack(side=tk.TOP, fill='x')

		self.cadreGrille = tk.Frame(self.cadreParametres)
		self.cadreGrille.pack(side=tk.TOP)
		#Boucle pour créer les Paramètres d'acquisitions
		self.parametre = dict()
		self.Select = dict()
		compteur = 0

		for cle, valeur in self.parametreAcquisition.items():
			self.parametre[cle] = tk.IntVar(value=valeur)
			self.Select[cle] = ChoixParametre(self.cadreGrille, cle, self.parametre[cle], self, compteur)
			compteur += 1

		#-------------------Choix des instruments d'acquisition

		self.cadreInstruments = tk.LabelFrame(self, text="Choix des instruments d'acquisition")
		self.cadreInstruments.pack(side=tk.TOP, fill='both', expand=1)

		#Gestion du GBF
		self.cadreGBF = ChoixInstrument(self.cadreInstruments, "GBF")
		self.cadreGBF.pack(side=tk.TOP, fill='y', expand=1)

		#Gestion de l'Oscillo
		self.cadreOscillo = ChoixInstrument(self.cadreInstruments, "Oscillo")
		self.cadreOscillo.pack(side=tk.TOP, fill='y', expand=1)





		#-------------------Boutons de validation

		self.cadreBouton = tk.Frame(self)
		self.cadreBouton.pack(side=tk.BOTTOM)

		self.boutonValidation = tk.Button(self.cadreBouton, text='Valider', command=self.validation)
		self.boutonValidation.pack(side=tk.RIGHT)

		self.boutonAnnuler = tk.Button(self.cadreBouton, text='Annuler', command=self.destroy)
		self.boutonAnnuler.pack(side=tk.RIGHT)



	def validation(self):

		#On met à jour les paramètres d'acquisition
		for cle, valeur in self.parametre.items():
			self.parametreAcquisition[cle] = valeur.get()

		#On instancie les appareils de mesure
		moduleGBF = "config.GBFsupporte."+re.sub(' ','_', self.cadreGBF.idnInstru)
		exec("import "+moduleGBF)
		exec("self.appli.GBF = self.instruController.getInstru(self.cadreGBF.varInstrument, resource_pyclass="+moduleGBF+".GBF)")

		moduleOscillo = "config.Oscillosupporte."+re.sub(' ','_', self.cadreOscillo.idnInstru)
		exec("import "+moduleOscillo)
		exec("self.appli.oscillo = self.instruController.getInstru(self.cadreOscillo.varInstrument, resource_pyclass="+moduleOscillo+".Oscillo)")

		#On met les appareils dans leur état de départ
		print(self.appli.GBF)
		self.appli.GBF.initialisation()
		self.appli.oscillo.initialisation()


		#On dessine le nouveau graphique
		self.appli.fenetre_princ.majEchelle()
		#On ferme la fenêtre de paramètre :
		self.destroy()





	







		
		

			

