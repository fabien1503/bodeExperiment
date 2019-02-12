
class BaseInstrument:

	def __del__(self):
		self.destroy()