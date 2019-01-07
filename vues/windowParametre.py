import tkinter as tk


class Window_parametre(tk.Toplevel):

	def __init__(self, appli):
		self.parametreAcquisition = appli.acquisitionParametre

		#On commence par créer la nouvelle fenêtre
		super().__init__(appli.fenetre_princ, padx=4, pady=4)
		self.geometry("600x400+300+0")
		self.title("Paramètres d'acquisition")


		#-------------------Choix des paramètres d'acquisition
		self.cadreParametres = tk.LabelFrame(self, text="Choix des paramètres d'acquisition")
		self.cadreParametres.pack(side=tk.TOP, fill='x')

		#Boucle pour créer les Paramètres d'acquisitions
		self.parametre = dict()
		self.Select = dict()

		for cle, valeur in self.parametreAcquisition.items():
			self.parametre[cle] = tk.IntVar(value=self.parametreAcquisition[cle])
			self.Select[cle] = ChoixParametre(self.cadreParametres, cle, self.parametre[cle], self)
			self.Select[cle].pack(side=tk.TOP)

		#-------------------Choix des instruments d'acquisition

		self.cadreInstruments = tk.LabelFrame(self, text="Choix des instruments d'acquisition")
		self.cadreInstruments.pack(side=tk.TOP, fill='both', expand=1)


		#-------------------Boutons de validation

		self.cadreBouton = tk.Frame(self)
		self.cadreBouton.pack(side=tk.BOTTOM)

		self.boutonValidation = tk.Button(self.cadreBouton, text='Valider')
		self.boutonValidation.pack(side=tk.RIGHT)

		self.boutonAnnuler = tk.Button(self.cadreBouton, text='Annuler', command=self.destroy)
		self.boutonAnnuler.pack(side=tk.RIGHT)


	



class ChoixParametre(tk.Frame):

	def __init__(self, parent, labelParametre, variableParametre, window_parametre, **kwargs):
		
		super().__init__(parent, **kwargs)

		self.window_parametre = window_parametre
		self.variableParametre = variableParametre
		self.labelParametre = labelParametre


		self.cadreErreur = tk.Frame(self)
		self.messageErreur = tk.Label(self.cadreErreur, text="Le paramètre doit être un entier", fg='red')
		self.messageErreur.pack(side=tk.TOP)

		self.cadreNormal = tk.Frame(self)
		self.cadreNormal.pack(side=tk.TOP)

		self.text = tk.Label(self.cadreNormal, text = 'Choix de '+labelParametre+' = ')
		self.text.pack(side=tk.LEFT)
		self.saisiParametre = tk.Entry(self.cadreNormal, textvariable=variableParametre, 
										justify='left')
		self.saisiParametre.pack(side=tk.LEFT)

		variableParametre.trace('w', self.testChiffres)


	def testChiffres(self, *args):
		#On désaffiche le message d'erreur (si il était affiché)		
		self.cadreErreur.forget()

		#On teste l'erreur, si il y en a une on affiche le message d'erreur
		try:
			int(self.variableParametre.get())
		except Exception as e:
			self.cadreErreur.pack(side=tk.TOP, before=self.cadreNormal)
			#et on déactive le bouton de validation :
			self.window_parametre.boutonValidation.config(default = 'disabled')
			

		
		

			

