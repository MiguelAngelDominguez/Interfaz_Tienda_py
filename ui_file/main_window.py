# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tienda_Main(object):
    def setupUi(self, Tienda_Main):
        if not Tienda_Main.objectName():
            Tienda_Main.setObjectName(u"Tienda_Main")
        Tienda_Main.resize(961, 550)
        self.pushButton = QPushButton(Tienda_Main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 230, 251, 71))

        self.retranslateUi(Tienda_Main)

        QMetaObject.connectSlotsByName(Tienda_Main)
    # setupUi

    def retranslateUi(self, Tienda_Main):
        Tienda_Main.setWindowTitle(QCoreApplication.translate("Tienda_Main", u"Tienda Main", None))
        self.pushButton.setText(QCoreApplication.translate("Tienda_Main", u"PushButton", None))
    # retranslateUi

