import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.rcsetup import cycler

from math import log10, pi
 
import vues.menu as mn


class Fenetre_princ(tk.Tk):

	def __init__(self, appli):
		self.appli = appli
		
		#Construction de la fenetre princiaple
		super().__init__()
		self.geometry("1280x700+0+0")
		self.title("Bode expérimental")

		#--------------Construction du menu---------------#
		self['menu'] = mn.Menu(self)

		#--------------Construction du graphique----------#
		self.fig = Figure(figsize=(12, 8), dpi=112)
		self.axGain = self.fig.add_subplot(211)
		self.axPhase = self.fig.add_subplot(212, sharex=self.axGain, ylim=(-180, 180))
		self.axGain.set_xlim(self.appli.acquisitionParametre['F_min'], self.appli.acquisitionParametre['F_max'])
		self.axGain.set_xscale('log')
		self.axGain.grid(which='major', axis='both')
		self.axGain.grid(which='minor', axis='x', linestyle='--', linewidth=0.5)
		self.axPhase.grid(which='major', axis='both')
		self.axPhase.grid(which='minor', axis='x', linestyle='--', linewidth=0.5)
		self.axPhase.set_xlabel('Fréquence (Hz)')
		self.axGain.set_ylabel('Gain (dB)')
		self.axPhase.set_ylabel('Phase (°)')
		self.axPhase.set_yticks([-180, -135, -90, -45, 0, 45, 90, 135, 180])

		self.lineGain, = self.axGain.plot([], [], 'r+')
		self.linePhase, = self.axPhase.plot([], [], 'r+')

		self.graph = FigureCanvasTkAgg(self.fig, master=self)
		self.canvas = self.graph.get_tk_widget()
		self.canvas.pack(side=tk.TOP)

		self.fig.tight_layout()


	def majEchelle(self):
		self.axGain.set_xlim(self.appli.acquisitionParametre['F_min'], self.appli.acquisitionParametre['F_max'])
		self.graph.draw()


		