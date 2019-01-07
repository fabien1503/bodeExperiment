import tkinter as tk


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
		self.window_parametre.boutonValidation.config(state = 'normal')#On réactive le bouton s'il était déactivé

		#On teste l'erreur, si il y en a une on affiche le message d'erreur
		try:
			int(self.variableParametre.get())
		except Exception as e:
			self.cadreErreur.pack(side=tk.TOP, before=self.cadreNormal)
			#et on déactive le bouton de validation :
			self.window_parametre.boutonValidation.config(state = 'disabled')
			