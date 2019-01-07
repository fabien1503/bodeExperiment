import tkinter as tk

import controllers.instrumentsController as ic


class ChoixInstrument(tk.Frame):

	def __init__(self, parent, instrument):

		super().__init__(parent)
		self.instrumentsController = ic.InstrumentController()

		self.listeInstruments = self.instrumentsController.listeInstruments()

		self.text = tk.Label(self, text="Choix "+instrument)
		self.text.pack(side=tk.LEFT)

		self.varInstrument = tk.StringVar()
		self.optionInstrument = tk.OptionMenu(self, self.varInstrument, *self.listeInstruments)

