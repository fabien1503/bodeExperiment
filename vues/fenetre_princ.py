import tkinter as tk

import vues.menu as mn


class Fenetre_princ(tk.Tk):

	def __init__(self, appli):
		self.appli = appli
		
		#Construction de la fenetre princiaple
		super().__init__()
		self.geometry("1280x800")
		self.title("Bode théorique")

		#--------------Construction du menu---------------#
		self['menu'] = mn.Menu(self)

		