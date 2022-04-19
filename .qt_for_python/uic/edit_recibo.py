# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_recibo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AgregarProducto(object):
    def setupUi(self, AgregarProducto):
        if not AgregarProducto.objectName():
            AgregarProducto.setObjectName(u"AgregarProducto")
        AgregarProducto.resize(587, 670)
        AgregarProducto.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame = QFrame(AgregarProducto)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 571, 541))
        self.frame.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 571, 31))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 151, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 100, 111, 21))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 140, 161, 21))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(70, 180, 221, 21))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Nombre_cliente = QLineEdit(self.frame)
        self.Nombre_cliente.setObjectName(u"Nombre_cliente")
        self.Nombre_cliente.setGeometry(QRect(220, 60, 291, 20))
        self.Nombre_cliente.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dni = QLineEdit(self.frame)
        self.dni.setObjectName(u"dni")
        self.dni.setGeometry(QRect(120, 100, 391, 20))
        self.dni.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 210, 131, 31))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"../assets/icons/new/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(440, 430, 91, 61))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.agregar = QPushButton(self.frame)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(140, 490, 131, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.agregar.setFont(font1)
        self.agregar.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/new/art_pint/anadir-al-carrito.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar.setIcon(icon1)
        self.agregar.setIconSize(QSize(35, 35))
        self.Cancelar = QPushButton(self.frame)
        self.Cancelar.setObjectName(u"Cancelar")
        self.Cancelar.setGeometry(QRect(290, 490, 131, 41))
        self.Cancelar.setFont(font1)
        self.Cancelar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(530, 430, 141, 61))
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.table_compra = QTableView(self.frame)
        self.table_compra.setObjectName(u"table_compra")
        self.table_compra.setGeometry(QRect(20, 250, 541, 192))
        self.fecha_compra = QLabel(self.frame)
        self.fecha_compra.setObjectName(u"fecha_compra")
        self.fecha_compra.setGeometry(QRect(130, 140, 171, 21))
        font2 = QFont()
        font2.setPointSize(16)
        self.fecha_compra.setFont(font2)
        self.fecha_compra.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.id_compra = QLabel(self.frame)
        self.id_compra.setObjectName(u"id_compra")
        self.id_compra.setGeometry(QRect(190, 180, 171, 21))
        self.id_compra.setFont(font2)
        self.id_compra.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(AgregarProducto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 560, 571, 101))
        self.frame_2.setStyleSheet(u"background-color: rgb(115, 115, 115);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Your_users = QPushButton(self.frame_2)
        self.Your_users.setObjectName(u"Your_users")
        self.Your_users.setGeometry(QRect(460, 10, 51, 51))
        self.Your_users.setCursor(QCursor(Qt.PointingHandCursor))
        self.Your_users.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/new/art_pint/usuario (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Your_users.setIcon(icon2)
        self.Your_users.setIconSize(QSize(40, 40))
        self.Your_users.setFlat(True)
        self.More_users = QPushButton(self.frame_2)
        self.More_users.setObjectName(u"More_users")
        self.More_users.setGeometry(QRect(300, 10, 51, 51))
        self.More_users.setCursor(QCursor(Qt.PointingHandCursor))
        self.More_users.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/new/art_pint/grupo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.More_users.setIcon(icon3)
        self.More_users.setIconSize(QSize(40, 40))
        self.More_users.setFlat(True)
        self.Close_Main = QPushButton(self.frame_2)
        self.Close_Main.setObjectName(u"Close_Main")
        self.Close_Main.setGeometry(QRect(50, 10, 51, 51))
        self.Close_Main.setCursor(QCursor(Qt.PointingHandCursor))
        self.Close_Main.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/new/art_pint/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_Main.setIcon(icon4)
        self.Close_Main.setIconSize(QSize(40, 40))
        self.Close_Main.setFlat(True)
        self.New_Users = QPushButton(self.frame_2)
        self.New_Users.setObjectName(u"New_Users")
        self.New_Users.setGeometry(QRect(220, 10, 51, 51))
        self.New_Users.setCursor(QCursor(Qt.PointingHandCursor))
        self.New_Users.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/new/art_pint/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.New_Users.setIcon(icon5)
        self.New_Users.setIconSize(QSize(40, 40))
        self.New_Users.setFlat(True)
        self.Confg = QPushButton(self.frame_2)
        self.Confg.setObjectName(u"Confg")
        self.Confg.setGeometry(QRect(380, 10, 51, 51))
        self.Confg.setCursor(QCursor(Qt.PointingHandCursor))
        self.Confg.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../assets/icons/new/art_pint/ajustes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Confg.setIcon(icon6)
        self.Confg.setIconSize(QSize(40, 40))
        self.Confg.setFlat(True)
        self.Close_Users = QPushButton(self.frame_2)
        self.Close_Users.setObjectName(u"Close_Users")
        self.Close_Users.setGeometry(QRect(130, 10, 51, 51))
        self.Close_Users.setCursor(QCursor(Qt.PointingHandCursor))
        self.Close_Users.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../assets/icons/new/art_pint/abra-bloqueo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_Users.setIcon(icon7)
        self.Close_Users.setIconSize(QSize(40, 40))
        self.Close_Users.setFlat(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 60, 61, 16))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 60, 61, 16))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 80, 61, 16))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 60, 61, 16))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 80, 61, 16))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 60, 71, 16))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 80, 61, 16))
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(380, 70, 51, 16))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(450, 60, 31, 21))
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(460, 80, 51, 21))
        self.label_5.raise_()
        self.Your_users.raise_()
        self.More_users.raise_()
        self.Close_Main.raise_()
        self.New_Users.raise_()
        self.Confg.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.Close_Users.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()

        self.retranslateUi(AgregarProducto)

        QMetaObject.connectSlotsByName(AgregarProducto)
    # setupUi

    def retranslateUi(self, AgregarProducto):
        AgregarProducto.setWindowTitle(QCoreApplication.translate("AgregarProducto", u"Agregar Producto", None))
        self.label.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Nuevo Recibo</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("AgregarProducto", u"Nombre del Cliente :", None))
        self.label_13.setText(QCoreApplication.translate("AgregarProducto", u"DNI :", None))
        self.label_14.setText(QCoreApplication.translate("AgregarProducto", u"Fecha :", None))
        self.label_15.setText(QCoreApplication.translate("AgregarProducto", u"N\u00b0 de compra :", None))
        self.pushButton.setText(QCoreApplication.translate("AgregarProducto", u"Buscar productos", None))
        self.label_18.setText(QCoreApplication.translate("AgregarProducto", u"Canselado :", None))
        self.agregar.setText(QCoreApplication.translate("AgregarProducto", u"AGREGAR", None))
        self.Cancelar.setText(QCoreApplication.translate("AgregarProducto", u"CANCELAR", None))
        self.checkBox.setText(QCoreApplication.translate("AgregarProducto", u"SI", None))
        self.fecha_compra.setText(QCoreApplication.translate("AgregarProducto", u"../../....", None))
        self.id_compra.setText(QCoreApplication.translate("AgregarProducto", u"1234567", None))
        self.Your_users.setText("")
        self.More_users.setText("")
        self.Close_Main.setText("")
        self.New_Users.setText("")
        self.Confg.setText("")
        self.Close_Users.setText("")
        self.label_3.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Sesion</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">A\u00f1adir</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Usuario</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Ver todos</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">los Usrs.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Confg.</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Tu</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("AgregarProducto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cuenta</span></p></body></html>", None))
    # retranslateUi

