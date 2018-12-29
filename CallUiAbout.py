# -*- coding: utf-8 -*-

"""
Module implementing CallUiAbout.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QStyleFactory

from Ui_about import Ui_Form


class CallUiAbout(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CallUiAbout, self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    ui = CallUiAbout()
    ui.show()
    sys.exit(app.exec_())
    
