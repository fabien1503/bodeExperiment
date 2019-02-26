from modeles.baseOscillo import BaseOscillo
from pyvisa.resources.usb import USBInstrument
import re


def NR3toFloat(nr3):
	nombre, puissance = re.split('E', re.sub(r'\n', '', nr3))
	return float(nombre)*10**float(puissance)



def sensibilityGenerator(puiss_depart, puissance_arrivee):
	valeurs = [1, 2, 5]
	for i in range(puiss_depart, puissance_arrivee+1):
		for val in valeurs:
			yield round(val*10**i, 6)


class Oscillo(USBInstrument, BaseOscillo):

	SENSIBILITE_H = [i for i in sensibilityGenerator(-6,-2)]
	SENSIBILITE_V = [i for i in sensibilityGenerator(-3,1)]

	def initialisation(self):
		super().initialisation()
		self.averageMode(5)

	def averageMode(self, nombre):
		self.write('acquire:type average')
		self.write('acquire:count '+str(nombre))

	def setVoieDC(self, voie):
		self.write('channel'+str(voie)+':coupling DC')

	def afficherVoie(self, voie):
		self.write('channel'+str(voie)+':display ON')

	def setVoieOffset(self, voie, offset):
		self.write('channel'+str(voie)+':offset '+str(offset))

	def attenuationVoie(self, voie, atte):
		self.write('channel'+str(voie)+':probe '+str(atte))

	def setTrigger(self, voie, mode):
		self.write('trigger:source channel'+str(voie))
		self.write('trigger:sweep '+str(mode))

	def setMeasure(self):
		self.write('measure:clear')
		for i in [1,2]:
			self.write('measure:vamplitude channel'+str(i))

		self.write('measure:phase channel1, channel2')

	def reglagesSensibilite(self):
		self.reglageSensibiliteH()
		for i in [1,2]:
			self.reglageSensibiliteV(i)

	def reglageSensibiliteH(self):
		scaleActual = round(NR3toFloat(self.query('timebase:scale?')), 6)
		scaleIndex = self.SENSIBILITE_H.index(scaleActual)
		periode = self.mesurePeriode()

		if periode < scaleActual:
			self.setScaleH(self.SENSIBILITE_H[scaleIndex - 1])
			self.reglageSensibiliteH()
		if 2*periode > 10*scaleActual:
			self.setScaleH(self.SENSIBILITE_H[scaleIndex + 1])
			self.reglageSensibiliteH()

	def reglageSensibiliteV(self, voie):
		scaleActual = round(NR3toFloat(self.query('channel'+str(voie)+':scale?')), 6)
		scaleIndex = self.SENSIBILITE_V.index(scaleActual)
		amplitude = self.mesureAmplitude(voie)

		if amplitude < 1.5*scaleActual:
			self.setScaleV(voie, self.SENSIBILITE_V[scaleIndex - 1])
			self.reglageSensibiliteV(voie)
		if amplitude > 6*scaleActual:
			self.setScaleV(voie, self.SENSIBILITE_V[scaleIndex + 1])
			self.reglageSensibiliteV(voie)

	def setScaleH(self, scale):
		self.write('timebase:scale '+str(scale))

	def setScaleV(self, voie, scale):
		self.write('channel'+str(voie)+':scale '+str(scale))

	def mesureFrequence(self):
		return NR3toFloat(self.query('measure:frequency? channel2'))

	def mesurePeriode(self):
		return NR3toFloat(self.query('measure:period? channel2'))

	def mesureAmplitude(self, voie):
		return NR3toFloat(self.query('measure:vamplitude? channel'+str(voie)))

	def mesurePhase(self):
		phase = NR3toFloat(self.query('measure:phase? channel1, channel2'))

		if phase > 180:
			phase = phase - 360
		if phase < -180:
			phase = phase + 360

		return phase
