import tkinter as tk
import tkinter.messagebox as mb


class ChoixParametre(tk.Frame):

	def __init__(self, parent, labelParametre, variableParametre, window_parametre, compteur, **kwargs):
		
		super().__init__(parent, **kwargs)

		self.window_parametre = window_parametre
		self.variableParametre = variableParametre
		self.labelParametre = labelParametre


		self.text = tk.Label(parent, text = 'Choix de '+labelParametre+' = ')
		self.text.grid(column=0, row=compteur, sticky='e')
		self.saisiParametre = tk.Entry(parent, textvariable=variableParametre, 
										justify='left')
		self.saisiParametre.grid(column=1, row=compteur)

		variableParametre.trace('w', self.testChiffres)


	def testChiffres(self, *args):
		#On teste l'erreur, si il y en a une on affiche le message d'erreur
		try:
			int(self.variableParametre.get())
		except Exception as e:
			#On cree une dialogue box
			mb.showerror('Paramètre non valable', 'Le paramètre doit être un entier !', parent=self.window_parametre)
			