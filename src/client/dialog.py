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
    def __init__(self, w=640, h=480):
        super(Dialog, self).__init__()
        self.setWindowTitle("_____")
        self.setFixedSize(w, h)

        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setContentsMargins(10,10,10,10)
        self.layout().setSpacing(10)

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((HOST, SOCK_PORT))
        self.finished.connect(self.soc.close)

        self.setStyleSheet(style)
        self.show()

    def claculate_step(self, step_option):
        step = str(step_option).split(".")
        if len(step) < 2:
            return int(step[0])
        else:
            numbers = [i for i in step[1]]
            return int("1" + ("0" * len(numbers)))

    def add_knob(self, action, options, row, col):
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignTop)

        knob = QtWidgets.QDial()
        knob.setMinimum(options["min"])
        knob.setMaximum(options["max"])
        knob.setNotchesVisible(True)

        knob.valueChanged.connect(
            lambda x: self.value_changed(
                knob = knob,
                action=action, 
                step=self.claculate_step(options["step"])
            )
        )

        label = QtWidgets.QLabel(options["title"])
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(knob)
        layout.addWidget(label)
        layout.addStretch()

        self.layout().addLayout(layout, row, col, 1, 1)

    # # # # # # # # # # # # # EVENTS # # # # # # # # # # # # # # 
    # vco:freq:set     # lfo1:freq:set     # lfo2:freq:set     #
    # vco:function:set # lfo1:function:set # lfo2:function:set #
    # # # # # # # # # # # # # Events # # # # # # # # # # # # # #
    def value_changed(self, action, knob, step):
        value = knob.value()
        data = json.dumps({'type': action, 'value': value})

        self.soc.send(data)
