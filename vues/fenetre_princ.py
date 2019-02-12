import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from math import log10, pi
 
import vues.menu as mn


class Fenetre_princ(tk.Tk):

	def __init__(self, appli):
		self.appli = appli
		
		#Construction de la fenetre princiaple
		super().__init__()
		self.geometry("1280x800")
		self.title("Bode expérimental")

		#--------------Construction du menu---------------#
		self['menu'] = mn.Menu(self)

		#--------------Construction du graphique----------#
		self.fig = Figure(figsize=(12, 8), dpi=112)
		self.axGain = self.fig.add_subplot(211, autoscale_on =1)
		self.axModule = self.fig.add_subplot(212, sharex=self.axGain, ylim=(-pi, pi))
		self.axGain.set_xlim(self.appli.acquisitionParametre['F_min'], self.appli.acquisitionParametre['F_max'])
		self.axGain.set_xscale('log')
		self.axGain.grid(which='major', axis='both')
		self.axGain.grid(which='minor', axis='x', linestyle='--', linewidth=0.5)
		self.axModule.grid(which='major', axis='both')
		self.axModule.grid(which='minor', axis='x', linestyle='--', linewidth=0.5)
		self.axModule.set_xlabel('Fréquence (Hz)')
		self.axGain.set_ylabel('Gain (dB)')
		self.axModule.set_ylabel('Phase (rad)')
		self.axModule.set_yticks([-pi, -3*pi/4, -pi/2, -pi/4, 0, pi/4, pi/2, 3*pi/4, pi])
		self.axModule.set_yticklabels([r'-$\pi$', r'$-\dfrac{3\pi}{4}$', r'$-\dfrac{\pi}{2}$', 
			r'$-\dfrac{\pi}{4}$', 0, r'$\dfrac{\pi}{4}$', r'$\dfrac{\pi}{2}$', r'$\dfrac{3\pi}{4}$', r'$\pi$'])

		self.graph = FigureCanvasTkAgg(self.fig, master=self)
		self.canvas = self.graph.get_tk_widget()
		self.canvas.pack(side=tk.TOP)

		self.fig.tight_layout()


	def majEchelle(self):
		self.axGain.set_xlim(self.appli.acquisitionParametre['F_min'], self.appli.acquisitionParametre['F_max'])
		self.graph.draw()


		