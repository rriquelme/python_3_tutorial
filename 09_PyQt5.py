from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class MainWindow(QtWidgets.QTabWidget):
    def __init__(self,):
        super(MainWindow,self).__init__()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(500, 500)
    mw.setWindowTitle('Sample window')
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
