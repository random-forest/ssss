#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication
from dialog import Dialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Dialog()
    
    sys.exit(app.exec_())
