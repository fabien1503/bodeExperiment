
class BaseInstrument:

	def initialisation(self):
		raise NotImplementedError

	def __del__(self):
		self.close()
		super().__del__()