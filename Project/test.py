from PyQt5.QtWidgets import QWidget, QPushButton

def initUI(self):
  self.barWidget = QWidget()
  self.barWidget.show()
  self.fooWidget = QWidget()
  self.fooWidget.hide()
  self.magicButton = QPushButton("foo")
  self.magicButton.clicked.connect(lambda: self.check_state_slot(self.magicButton.text()))


def check_state_slot(self, state):
  if state == "foo":
    self.barWidget.hide()
    self.fooWidget.show()
    self.magicButton.setText("bar")
  elif state == "bar":
    self.fooWidget.hide()
    self.barWidget.show()
    self.magicButton.setText("foo")