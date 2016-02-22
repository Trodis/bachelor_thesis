import sys
from PySide import QtCore, QtGui
from gui import Ui_MainWindow

def main(argv):
    app = QtGui.QApplication(argv)
    mainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)
