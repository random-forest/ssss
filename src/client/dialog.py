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

    def __init__(self):
        super(Dialog, self).__init__()
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

    def knob_build(self):
        self.knob = QtWidgets.QDial()
        self.knob.setMinimum(0)
        self.knob.setMaximum(440)
        self.knob.setNotchesVisible(True)
        self.knob.valueChanged.connect(self.value_changed)

        self.label = QtWidgets.QLabel("VCO")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout().addWidget(self.knob)
        self.layout().addWidget(self.label)

    # # # # # # # # # # # # # EVENTS # # # # # # # # # # # # # # 
    # vco:freq:set     # lfo1:freq:set     # lfo2:freq:set     #
    # vco:function:set # lfo1:function:set # lfo2:function:set #
    # # # # # # # # # # # # # Events # # # # # # # # # # # # # #
    def value_changed(self):
        data = json.dumps({'type': "vco:freq:set", 'value': self.knob.value()})

        self.soc.send(data)
