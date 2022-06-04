# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confg_product.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Confg_Productos(object):
    def setupUi(self, Confg_Productos):
        if not Confg_Productos.objectName():
            Confg_Productos.setObjectName(u"Confg_Productos")
        Confg_Productos.resize(586, 441)
        Confg_Productos.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame = QFrame(Confg_Productos)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 571, 321))
        self.frame.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 571, 31))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 111, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 140, 111, 21))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 200, 241, 21))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Nombre = QLineEdit(self.frame)
        self.Nombre.setObjectName(u"Nombre")
        self.Nombre.setGeometry(QRect(100, 90, 311, 20))
        self.Nombre.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Marca = QLineEdit(self.frame)
        self.Marca.setObjectName(u"Marca")
        self.Marca.setGeometry(QRect(120, 140, 311, 20))
        self.Marca.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.img_producto = QLineEdit(self.frame)
        self.img_producto.setObjectName(u"img_producto")
        self.img_producto.setGeometry(QRect(260, 200, 181, 20))
        self.img_producto.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.b = QPushButton(self.frame)
        self.b.setObjectName(u"b")
        self.b.setGeometry(QRect(450, 200, 41, 31))
        self.b.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"../assets/icons/new/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b.setIcon(icon)
        self.agregar = QPushButton(self.frame)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(150, 260, 131, 41))
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
        self.Cancelar.setGeometry(QRect(300, 260, 131, 41))
        self.Cancelar.setFont(font1)
        self.Cancelar.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/new/art_pint/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Cancelar.setIcon(icon2)
        self.Cancelar.setIconSize(QSize(35, 35))
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(500, 180, 61, 61))
        self.label_19.setPixmap(QPixmap(u"../assets/img_ui/producto_default.png"))
        self.label_19.setScaledContents(True)
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(420, 80, 131, 41))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(440, 130, 131, 41))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(Confg_Productos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 330, 571, 101))
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
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/new/art_pint/usuario (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Your_users.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/new/art_pint/grupo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.More_users.setIcon(icon4)
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
        self.Close_Main.setIcon(icon2)
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

        self.retranslateUi(Confg_Productos)

        QMetaObject.connectSlotsByName(Confg_Productos)
    # setupUi

    def retranslateUi(self, Confg_Productos):
        Confg_Productos.setWindowTitle(QCoreApplication.translate("Confg_Productos", u"Editar Producto", None))
        self.label.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Configuraci\u00f3n de Productos</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Confg_Productos", u"Ganacia  :", None))
        self.label_13.setText(QCoreApplication.translate("Confg_Productos", u"Descuento :", None))
        self.label_17.setText(QCoreApplication.translate("Confg_Productos", u"Imagen por defecto de producto:", None))
        self.b.setText("")
        self.agregar.setText(QCoreApplication.translate("Confg_Productos", u"GUARDAR", None))
        self.Cancelar.setText(QCoreApplication.translate("Confg_Productos", u"CANCELAR", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">GANANCIA MAX </span></p><p><span style=\" font-size:7pt; font-weight:600;\">DE *1.3%</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">DESCUENTO MAX </span></p><p><span style=\" font-size:7pt; font-weight:600;\">DE *0.1%</span></p></body></html>", None))
        self.Your_users.setText("")
        self.More_users.setText("")
        self.Close_Main.setText("")
        self.New_Users.setText("")
        self.Confg.setText("")
        self.Close_Users.setText("")
        self.label_3.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Sesion</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">A\u00f1adir</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Usuario</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Ver todos</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">los Usrs.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Confg.</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Tu</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Confg_Productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cuenta</span></p></body></html>", None))
    # retranslateUi

