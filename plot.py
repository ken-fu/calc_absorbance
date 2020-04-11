# -*- coding: utf-8 -*-
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QSizePolicy


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.subplots_adjust(left=0.1, right=0.95, bottom=0.16, top=0.95)
        self.fig_init()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def fig_init(self):
        '''initialize fig axes'''
        self.axes = self.fig.add_subplot(111)
        self.axes.tick_params(labelleft=False)
        self.axes.tick_params(direction="in")
        self.axes.set_xlabel('Wavelength [nm]')
        self.axes.set_ylabel('Absorption [arb.units]')

    def plot(self, data_xy):
        '''plot data'''
        self.axes.clear()
        self.fig_init()
        self.axes.plot(data_xy[:, 0], data_xy[:, 1], 'b-')
        self.draw()
