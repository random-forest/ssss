# -*- coding: utf-8 -*-

import socket
import json

from PySide2 import QtCore   
from PySide2 import QtGui
from PySide2 import QtWidgets
from style import style

HOST = ''
SOCK_PORT = 30001

class Dialog(QtWidgets.QDialog):
    def __init__(self, action, options):
        super(Dialog, self).__init__()
        self.action = action
        self.options = options
        self.claculate_step();
        self.setWindowTitle('zalupa')
        self.setFixedSize(320, 240)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignCenter)

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((HOST, SOCK_PORT))

        self.finished.connect(self.soc.close)

        self.knob_build()
        self.setStyleSheet(style)
        self.show()

    def claculate_step(self):
        step = str(self.options["step"]).split(".")

        if len(step) < 2:
            self.step = int(step[0])
        else:
            numbers = [i for i in step[1]]
            self.step = int("1" + ("0" * len(numbers)))

    def knob_build(self):
        self.knob = QtWidgets.QDial()
        self.knob.setMinimum(self.options["min"])
        self.knob.setMaximum(self.options["max"])
        
        self.knob.setNotchesVisible(True)
        self.knob.valueChanged.connect(self.value_changed)

        self.label = QtWidgets.QLabel(self.options["title"])
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout().addWidget(self.knob)
        self.layout().addWidget(self.label)

    # # # # # # # # # # # # # EVENTS # # # # # # # # # # # # # # 
    # vco:freq:set     # lfo1:freq:set     # lfo2:freq:set     #
    # vco:function:set # lfo1:function:set # lfo2:function:set #
    # # # # # # # # # # # # # Events # # # # # # # # # # # # # #
    def value_changed(self):
        print(float(self.knob.value()) / self.step)

        data = json.dumps({'type': self.action, 'value': self.knob.value()})

        self.soc.send(data)
