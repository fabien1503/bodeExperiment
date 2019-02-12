import tkinter as tk

import controllers.instrumentsController as ic


class ChoixInstrument(tk.Frame):

	def __init__(self, parent, instrument):

		super().__init__(parent)

		self.instrumentsController = ic.InstrumentController()
		self.listeInstruments = self.instrumentsController.listeInstruments()

		self.instrument = instrument

		self.frameChoix = tk.Frame(self)
		self.frameChoix.pack(side=tk.TOP)

		self.text = tk.Label(self.frameChoix, text="Choix "+instrument)
		self.text.pack(side=tk.LEFT)

		self._varInstrument = tk.StringVar()
		self.optionInstrument = tk.OptionMenu(self.frameChoix, self._varInstrument, '', *self.listeInstruments)
		self.optionInstrument.pack(side=tk.LEFT)

		self.frameCheck = tk.Frame(self)
		self.frameCheck.pack(side=tk.TOP)
		self.frameCheck.columnconfigure(1, minsize=120)

		self.labelConnexionCheck = tk.Label(self.frameCheck, text="Test de connexion : ", justify='right')
		self.labelConnexionResult = tk.Label(self.frameCheck)
		self.labelCommunicationCheck = tk.Label(self.frameCheck, text="Test de communication : ", justify='right')
		self.labelCommunicationResult = tk.Label(self.frameCheck)
		self.labelReconnaissanceCheck = tk.Label(self.frameCheck, text="Appareil reconnu : ", justify='right')
		self.labelReconnaissanceResult = tk.Label(self.frameCheck)

		self.labelConnexionCheck.grid(column=0, row=0, sticky='e')
		self.labelConnexionResult.grid(column=1, row=0)
		self.labelCommunicationCheck.grid(column=0, row=1, sticky='e')
		self.labelCommunicationResult.grid(column=1, row=1)
		self.labelReconnaissanceCheck.grid(column=0, row=2, sticky='e')
		self.labelReconnaissanceResult.grid(column=1, row=2)


		self._varInstrument.trace('w', self.instrumentVerification)



	@property
	def varInstrument(self):
		return self._varInstrument.get()


	#Lance tous les tests (connexion, comm et Reconnaissance) de l'instrument
	def instrumentVerification(self, *args):
		listeVerifs = ['Connexion', 'Communication', 'Reconnaissance']

		verifications = self.instrumentsController.checkInstrument(self.instrument, self.varInstrument)

		for index, verif in enumerate(listeVerifs):
			verifLabel = getattr(self, 'label'+verif+'Result')
			verifLabel.grid_forget()
			verifLabel.destroy()
			
			if verifications[index]:
				setattr(self, 'label'+verif+'Result', self.ConstructionLabelResult('OK', self.frameCheck))
				exec('self.label'+verif+'Result.grid(column=1, row=index)')
			else:
				setattr(self, 'label'+verif+'Result', self.ConstructionLabelResult('ECHEC', self.frameCheck))
				exec('self.label'+verif+'Result.grid(column=1, row=index)')

		#Si la dernière vérification est passée, on garde le nom de l'appareil en mémoire	
		if verifications[2]:
			self.idnInstru = verifications[3]


	def ConstructionLabelResult(self, resultat, parent):
		labelResultat = tk.Label(parent)
		labelI = tk.Label(labelResultat, text='[')
		labelI.pack(side=tk.LEFT)
		labelII = tk.Label(labelResultat, text=resultat)
		labelII.pack(side=tk.LEFT)
		labelIII = tk.Label(labelResultat, text=']')
		labelIII.pack(side=tk.LEFT)

		if resultat=='OK':
			labelII.config(fg='green')
		if resultat=='ECHEC':
			labelII.config(fg='red')

		return labelResultat
			

			
			
		


