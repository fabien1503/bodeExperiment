import vues.fenetre_princ as main_fene


class Appli():

	def __init__(self):

		#---------On définit la fenêtre principale------------------#
		self.fenetre_princ = main_fene.Fenetre_princ(self)

	
	def run(self):
		self.fenetre_princ.mainloop()