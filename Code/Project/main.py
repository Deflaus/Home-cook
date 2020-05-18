
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from view import Ui_Form


def main_button():
    Window.FindRec.show()
    Window.Ingridients.show()
    Window.Callories_3.hide()
    Window.TopRec_3.hide()
    Window.Instructions.hide()

def toprec_button():
    Window.TopRec_3.show()
    Window.Callories_3.hide()
    Window.FindRec.hide()
    Window.Ingridients.hide()
    Window.Instructions.hide()

def instr_button():
    Window.Instructions.show()
    Window.Callories_3.hide()
    Window.FindRec.hide()
    Window.Ingridients.hide()
    Window.TopRec_3.hide()

def callories_button():
    Window.Callories_3.show()
    Window.TopRec_3.hide()
    Window.FindRec.hide()
    Window.Ingridients.hide()
    Window.Instructions.hide()


app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()

Window = Ui_Form()

Window.setupUi(Form)
Window.Main.clicked.connect(main_button)
Window.TopRec.clicked.connect(toprec_button)
Window.Callories.clicked.connect(callories_button)
Window.Instruction.clicked.connect(instr_button)

Form.show()


Window.Callories_3.hide()
Window.TopRec_3.hide()
Window.Instructions.hide()

sys.exit(app.exec_())

