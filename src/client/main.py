#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication
from dialog import Dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Dialog(600, 400)
    window.add_knob("vco:freq:set", { "title": "vco hz", "min": 0, "max": 440, "step": 0.1 }, 0, 0)
    window.add_knob("vco:function:set", { "title": "vco fn", "min": 0, "max": 4, "step": 1 }, 0, 1)
    window.add_knob("lfo1:freq:set", { "title": "lfo1 hz", "min": 0, "max": 13, "step": 1 }, 0, 2)
    window.add_knob("lfo1:function:set", { "title": "lfo1 fn", "min": 0, "max": 4, "step": 1 }, 0, 3)
    window.add_knob("lfo2:freq:set", { "title": "lfo2 hz", "min": 0, "max": 27, "step": 1 }, 1, 1)
    window.add_knob("lfo2:function:set", { "title": "lfo2 fn", "min": 0, "max": 4, "step": 1 }, 1, 2)

    sys.exit(app.exec_())
