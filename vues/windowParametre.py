import tkinter as tk


class Window_parametre(tk.Toplevel):

	def __init__(self, appli):

		#On commence par créer la nouvelle fenêtre
		super().__init__(appli.fenetre_princ)
		self.geometry("600x400+300+0")
		self.title("Paramètres d'acquisition")