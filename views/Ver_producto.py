# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ver_producto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ver_productos(object):
    def setupUi(self, Ver_productos):
        if not Ver_productos.objectName():
            Ver_productos.setObjectName(u"Ver_productos")
        Ver_productos.resize(1091, 670)
        Ver_productos.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame = QFrame(Ver_productos)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1071, 541))
        self.frame.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 10, 1031, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 40, 61, 21))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.filtro = QComboBox(self.frame_3)
        self.filtro.setObjectName(u"filtro")
        self.filtro.setGeometry(QRect(100, 40, 151, 22))
        self.filtro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Busqueda = QLineEdit(self.frame_3)
        self.Busqueda.setObjectName(u"Busqueda")
        self.Busqueda.setGeometry(QRect(270, 40, 441, 21))
        self.Busqueda.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.buscar_producto = QPushButton(self.frame_3)
        self.buscar_producto.setObjectName(u"buscar_producto")
        self.buscar_producto.setGeometry(QRect(720, 40, 151, 23))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buscar_producto.setFont(font)
        self.buscar_producto.setStyleSheet(u"background-color: rgb(99, 99, 99);\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"../assets/icons/new/art_pint/documento (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_producto.setIcon(icon)
        self.actualizar_producto = QPushButton(self.frame_3)
        self.actualizar_producto.setObjectName(u"actualizar_producto")
        self.actualizar_producto.setGeometry(QRect(880, 40, 151, 23))
        self.actualizar_producto.setStyleSheet(u"background-color: rgb(99, 99, 99);\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/new/art_pint/reiniciar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actualizar_producto.setIcon(icon1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 0, 261, 20))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tabla = QTableWidget(self.frame)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(30, 90, 1031, 401))
        self.tabla.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Anadir_producto = QPushButton(self.frame)
        self.Anadir_producto.setObjectName(u"Anadir_producto")
        self.Anadir_producto.setGeometry(QRect(660, 502, 131, 31))
        self.Anadir_producto.setFont(font)
        self.Anadir_producto.setStyleSheet(u"background-color: rgb(94, 144, 86);\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/new/art_pint/abrir-caja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Anadir_producto.setIcon(icon2)
        self.Anadir_producto.setIconSize(QSize(25, 25))
        self.Editar_producto = QPushButton(self.frame)
        self.Editar_producto.setObjectName(u"Editar_producto")
        self.Editar_producto.setGeometry(QRect(800, 502, 121, 31))
        self.Editar_producto.setFont(font)
        self.Editar_producto.setStyleSheet(u"background-color: rgb(130, 132, 95);\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/new/art_pint/caracteristicas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Editar_producto.setIcon(icon3)
        self.Editar_producto.setIconSize(QSize(25, 25))
        self.Eliminar_producto = QPushButton(self.frame)
        self.Eliminar_producto.setObjectName(u"Eliminar_producto")
        self.Eliminar_producto.setGeometry(QRect(930, 502, 121, 31))
        self.Eliminar_producto.setFont(font)
        self.Eliminar_producto.setStyleSheet(u"background-color: rgb(148, 112, 112);\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/new/art_pint/bloqueador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Eliminar_producto.setIcon(icon4)
        self.Eliminar_producto.setIconSize(QSize(25, 25))
        self.frame_2 = QFrame(Ver_productos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 560, 1071, 101))
        self.frame_2.setStyleSheet(u"background-color: rgb(115, 115, 115);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Your_users = QPushButton(self.frame_2)
        self.Your_users.setObjectName(u"Your_users")
        self.Your_users.setGeometry(QRect(730, 10, 51, 51))
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
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/new/art_pint/usuario (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Your_users.setIcon(icon5)
        self.Your_users.setIconSize(QSize(40, 40))
        self.Your_users.setFlat(True)
        self.More_users = QPushButton(self.frame_2)
        self.More_users.setObjectName(u"More_users")
        self.More_users.setGeometry(QRect(570, 10, 51, 51))
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
        icon6 = QIcon()
        icon6.addFile(u"../assets/icons/new/art_pint/grupo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.More_users.setIcon(icon6)
        self.More_users.setIconSize(QSize(40, 40))
        self.More_users.setFlat(True)
        self.Close_Main = QPushButton(self.frame_2)
        self.Close_Main.setObjectName(u"Close_Main")
        self.Close_Main.setGeometry(QRect(320, 10, 51, 51))
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
        icon7 = QIcon()
        icon7.addFile(u"../assets/icons/new/art_pint/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_Main.setIcon(icon7)
        self.Close_Main.setIconSize(QSize(40, 40))
        self.Close_Main.setFlat(True)
        self.New_Users = QPushButton(self.frame_2)
        self.New_Users.setObjectName(u"New_Users")
        self.New_Users.setGeometry(QRect(490, 10, 51, 51))
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
        icon8 = QIcon()
        icon8.addFile(u"../assets/icons/new/art_pint/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.New_Users.setIcon(icon8)
        self.New_Users.setIconSize(QSize(40, 40))
        self.New_Users.setFlat(True)
        self.Confg = QPushButton(self.frame_2)
        self.Confg.setObjectName(u"Confg")
        self.Confg.setGeometry(QRect(650, 10, 51, 51))
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
        icon9 = QIcon()
        icon9.addFile(u"../assets/icons/new/art_pint/ajustes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Confg.setIcon(icon9)
        self.Confg.setIconSize(QSize(40, 40))
        self.Confg.setFlat(True)
        self.Close_Users = QPushButton(self.frame_2)
        self.Close_Users.setObjectName(u"Close_Users")
        self.Close_Users.setGeometry(QRect(400, 10, 51, 51))
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
        icon10 = QIcon()
        icon10.addFile(u"../assets/icons/new/art_pint/abra-bloqueo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_Users.setIcon(icon10)
        self.Close_Users.setIconSize(QSize(40, 40))
        self.Close_Users.setFlat(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 60, 61, 16))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 60, 61, 16))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 80, 61, 16))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(480, 60, 61, 16))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(500, 80, 61, 16))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(560, 60, 71, 16))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(580, 80, 61, 16))
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(650, 70, 51, 16))
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(720, 60, 31, 21))
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(730, 80, 51, 21))
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

        self.retranslateUi(Ver_productos)

        QMetaObject.connectSlotsByName(Ver_productos)
    # setupUi

    def retranslateUi(self, Ver_productos):
        Ver_productos.setWindowTitle(QCoreApplication.translate("Ver_productos", u"Tienda Main", None))
        self.label_2.setText(QCoreApplication.translate("Ver_productos", u"Buscar por : ", None))
        self.buscar_producto.setText(QCoreApplication.translate("Ver_productos", u"Buscar", None))
        self.actualizar_producto.setText(QCoreApplication.translate("Ver_productos", u"Actualizar", None))
        self.label.setText(QCoreApplication.translate("Ver_productos", u"Ver Todos los Productos", None))
        self.Anadir_producto.setText(QCoreApplication.translate("Ver_productos", u"A\u00f1adir", None))
        self.Editar_producto.setText(QCoreApplication.translate("Ver_productos", u"Editar", None))
        self.Eliminar_producto.setText(QCoreApplication.translate("Ver_productos", u"Eliminar", None))
        self.Your_users.setText("")
        self.More_users.setText("")
        self.Close_Main.setText("")
        self.New_Users.setText("")
        self.Confg.setText("")
        self.Close_Users.setText("")
        self.label_3.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Sesion</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">A\u00f1adir</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Usuario</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Ver todos</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">los Usrs.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Confg.</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Tu</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Ver_productos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cuenta</span></p></body></html>", None))
    # retranslateUi

