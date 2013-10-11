#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *

def bmicalc ( height, weight ):
  return ( weight / pow(height/100.0,2) )

class mainWindow ( QWidget ):
  def __init__ ( self, parent = None ):
    super(mainWindow, self).__init__(parent)
    self.initLayout()
    self.connection()

  def initLayout(self):
    self.lblHeight = QLabel(u"身高(cm)")
    self.lblWeight = QLabel(u"體重(kg)")

    self.txtHeight = QLineEdit("0")
    self.txtWeight = QLineEdit("0")

    self.btnCalc = QPushButton(u"計算")
    self.btnExit = QPushButton(u"離開")
    
    self.lblLayout = QVBoxLayout()
    self.lblLayout.addWidget(self.lblHeight)
    self.lblLayout.addWidget(self.lblWeight)

    self.txtLayout = QVBoxLayout()
    self.txtLayout.addWidget(self.txtHeight)
    self.txtLayout.addWidget(self.txtWeight)

    self.contentLayout = QHBoxLayout()
    self.contentLayout.addLayout(self.lblLayout)
    self.contentLayout.addLayout(self.txtLayout)

    self.btnLayout = QHBoxLayout()
    self.btnLayout.addWidget(self.btnCalc)
    self.btnLayout.addWidget(self.btnExit)

    self.outerWrapper = QVBoxLayout()
    self.outerWrapper.addLayout(self.contentLayout)
    self.outerWrapper.addLayout(self.btnLayout)

    self.setLayout(self.outerWrapper)


  def connection(self):
    self.btnExit.clicked.connect(self.close)
    self.btnCalc.clicked.connect(self.calc)

  def calc(self):
    height = float(self.txtHeight.text())
    weight = float(self.txtWeight.text())

    QMessageBox.about( self , u"你的 BMI", str( bmicalc( height, weight ) ) ) 

if __name__ == "__main__":
  app = QApplication(sys.argv)
  widget = mainWindow()
  widget.show()
  app.exec_()
