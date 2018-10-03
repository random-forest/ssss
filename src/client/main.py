#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication
from dialog import Dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)

    vco  = Dialog("vco:freq:set", { "title": "vco", "min": 0, "max": 440, "step": 0.1 })
    lfo1 = Dialog("lfo1:freq:set", { "title": "lfo1", "min": 0, "max": 13, "step": 1 })
    lfo2 = Dialog("lfo2:freq:set", { "title": "lfo2", "min": 0, "max": 27, "step": 1 })

    sys.exit(app.exec_())
