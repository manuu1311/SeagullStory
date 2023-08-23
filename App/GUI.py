from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class controller:
    def __init__(self):
        self.app=QtWidgets.QApplication(sys.argv)
        self.currscene=None
    def changescene(self,scene):
        #app = QtWidgets.QApplication(sys.argv)
        self.curr_scene=QtWidgets.QMainWindow()
        ui=scene
        ui.setupUi(self.curr_scene)
        self.curr_scene.show()
        self.app.exec_()

    def closescene(self):
        self.currscene.close()