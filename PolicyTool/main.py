# -*- coding: utf-8 -*-
import sys
from PySide import QtCore, QtGui
from gui import Ui_MainWindow

def main(argv):
    app = QtGui.QApplication(argv)
    mainWindow = GUIMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

class GUIMainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, *args):
        QtGui.QMainWindow.__init__(self, *args)
        Ui_MainWindow.__init__(self, self)
        self.createConnects()
    
    def createConnects(self):
        self.pushButton_save.clicked.connect(self.saveConfig)
        self.pushButton_reset.clicked.connect(self.resetOptions)
    
    def getBitBoxPath(self):
        pass

    """
    Slots optimieren die Speichverwaltung von Qt und beschleunigt somit
    die Ausführung der Slots.
    """
    @QtCore.Slot()
    def saveConfig(self):
        print "Hallo Welt"

    @QtCore.Slot()
    def resetOptions(self):
        pass


if __name__ == '__main__':
    main(sys.argv)
