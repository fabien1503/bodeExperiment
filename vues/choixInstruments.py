import tkinter as tk

import controllers.instrumentsController as ic


class ChoixInstrument(tk.Frame):

	def __init__(self, parent, instrument):

		super().__init__(parent)
		self.instrumentsController = ic.InstrumentController()

		self.listeInstruments = self.instrumentsController.listeInstruments()

		self.text = tk.Label(self, text="Choix "+instrument)
		self.text.pack(side=tk.LEFT)

		self.varInstrument = tk.StringVar(name=instrument)
		self.optionInstrument = tk.OptionMenu(self, self.varInstrument, '', *self.listeInstruments)
		self.optionInstrument.pack(side=tk.LEFT)

		self.varInstrument.trace('w', self.instrumentVerification)







	#Alias de la fonction ic.instrumentVerification pour lui passer la variable self.varInstrument
	def instrumentVerification(self, instrument, *args):
		if self.instrumentsController.instrumentVerification(instrument, self.varInstrument):
			print('instrument Vérifié')
		else :
			print('instrument non valide')


