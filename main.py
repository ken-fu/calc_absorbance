# -*- coding: utf-8 -*-
import os
import sys

import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog

from calc import calc_abs
from plot import PlotCanvas


class PathTextBox(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setReadOnly(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path):
                self.setText(path)


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(720, 250)
        self.move(100, 100)
        self.setWindowTitle('calc_absorbance')
        self.create_widgets()
        self.show()

    def create_widgets(self):
        '''create widgets on main window'''
        self.label_ts_m = QLabel("Transmission spectrum of material", self)
        self.label_ts_m.move(10, 10)
        self.textbox_ts_m = PathTextBox(self)
        self.textbox_ts_m.setFixedWidth(400)
        self.textbox_ts_m.move(10, 30)

        self.label_bg_m = QLabel("Back ground spectrum of material", self)
        self.label_bg_m.move(10, 60)
        self.textbox_bg_m = PathTextBox(self)
        self.textbox_bg_m.setFixedWidth(400)
        self.textbox_bg_m.move(10, 80)

        self.label_ts_r = QLabel("Transmission spectrum of reference", self)
        self.label_ts_r.move(10, 110)
        self.textbox_ts_r = PathTextBox(self)
        self.textbox_ts_r.setFixedWidth(400)
        self.textbox_ts_r.move(10, 130)

        self.label_bg_r = QLabel("Back ground spectrum of reference", self)
        self.label_bg_r.move(10, 160)
        self.textbox_bg_r = PathTextBox(self)
        self.textbox_bg_r.setFixedWidth(400)
        self.textbox_bg_r.move(10, 180)

        self.pbutton_calc = QPushButton("calc", self)
        self.pbutton_calc.move(10, 210)
        self.pbutton_calc.clicked.connect(self.go_calc)

        self.plot_canvas = PlotCanvas(self, 3, 2.5)
        self.plot_canvas.move(420, 0)

        self.pbutton_save = QPushButton("save", self)
        self.pbutton_save.move(130, 210)
        self.pbutton_save.clicked.connect(self.save_fig)

    def go_calc(self):
        file_path = [self.textbox_ts_m.text(), self.textbox_bg_m.text(
        ), self.textbox_ts_r.text(), self.textbox_bg_r.text()]
        for path in file_path:
            if path == '':
                self.message_box = QMessageBox.information(
                    self, "", "file open error", QMessageBox.Close)
                return
        self.result_list = calc_abs(file_path)
        self.plot_canvas.plot(self.result_list)

    def save_fig(self):
        from pathlib import Path
        file_name, _ = QFileDialog.getSaveFileName(self)
        if len(file_name) == 0:
            return
        file_name = str(Path(file_name).with_suffix(".png"))
        self.plot_canvas.fig.savefig(file_name)

        output_csv = open(str(Path(file_name).with_suffix(".csv")), 'w')
        try:
            np.savetxt(str(Path(file_name).with_suffix(".csv")), self.result_list, delimiter=",")
        except:
            self.message_box = QMessageBox.information(
                self, "", "file save error", QMessageBox.Close)


def main():
    main_app = QApplication(sys.argv)
    main_window = MainWidget()
    sys.exit(main_app.exec_())


if __name__ == '__main__':
    main()
