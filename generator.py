from setup import Ui_frmMain

from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtCore as qtc

class GeneratorWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = GeneratorWindow()
    widget.show()
    app.exec_()

# This is a test