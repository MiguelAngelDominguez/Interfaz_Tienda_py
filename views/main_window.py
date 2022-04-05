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


class Tienda_Main(object):
    def setupUi(self, Tienda_Main):
        if not Tienda_Main.objectName():
            Tienda_Main.setObjectName(u"Tienda_Main")
        Tienda_Main.resize(589, 537)
        Tienda_Main.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame = QFrame(Tienda_Main)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 281, 411))
        self.frame.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Ver_Productos = QPushButton(self.frame)
        self.Ver_Productos.setObjectName(u"Ver_Productos")
        self.Ver_Productos.setGeometry(QRect(10, 60, 261, 61))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Ver_Productos.setFont(font)
        self.Ver_Productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ver_Productos.setFocusPolicy(Qt.NoFocus)
        self.Ver_Productos.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/new/art_pint/descripcion-del-producto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ver_Productos.setIcon(icon)
        self.Ver_Productos.setIconSize(QSize(50, 50))
        self.Ver_Productos.setFlat(True)
        self.Anadir_Productos = QPushButton(self.frame)
        self.Anadir_Productos.setObjectName(u"Anadir_Productos")
        self.Anadir_Productos.setGeometry(QRect(10, 200, 261, 61))
        self.Anadir_Productos.setFont(font)
        self.Anadir_Productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Anadir_Productos.setFocusPolicy(Qt.NoFocus)
        self.Anadir_Productos.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/new/art_pint/abrir-caja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Anadir_Productos.setIcon(icon1)
        self.Anadir_Productos.setIconSize(QSize(50, 50))
        self.Anadir_Productos.setFlat(True)
        self.Editar_Productos = QPushButton(self.frame)
        self.Editar_Productos.setObjectName(u"Editar_Productos")
        self.Editar_Productos.setGeometry(QRect(10, 130, 261, 61))
        self.Editar_Productos.setFont(font)
        self.Editar_Productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Editar_Productos.setFocusPolicy(Qt.NoFocus)
        self.Editar_Productos.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/new/art_pint/caracteristicas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Editar_Productos.setIcon(icon2)
        self.Editar_Productos.setIconSize(QSize(50, 50))
        self.Editar_Productos.setFlat(True)
        self.Eliminar_Productos = QPushButton(self.frame)
        self.Eliminar_Productos.setObjectName(u"Eliminar_Productos")
        self.Eliminar_Productos.setGeometry(QRect(10, 270, 261, 61))
        self.Eliminar_Productos.setFont(font)
        self.Eliminar_Productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Eliminar_Productos.setFocusPolicy(Qt.NoFocus)
        self.Eliminar_Productos.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/new/art_pint/bloqueador.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Eliminar_Productos.setIcon(icon3)
        self.Eliminar_Productos.setIconSize(QSize(50, 50))
        self.Eliminar_Productos.setFlat(True)
        self.Ajustes_Productos = QPushButton(self.frame)
        self.Ajustes_Productos.setObjectName(u"Ajustes_Productos")
        self.Ajustes_Productos.setGeometry(QRect(10, 340, 261, 61))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.Ajustes_Productos.setFont(font1)
        self.Ajustes_Productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ajustes_Productos.setFocusPolicy(Qt.NoFocus)
        self.Ajustes_Productos.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/new/art_pint/gestion-de-producto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ajustes_Productos.setIcon(icon4)
        self.Ajustes_Productos.setIconSize(QSize(50, 50))
        self.Ajustes_Productos.setFlat(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 281, 31))
        self.frame_2 = QFrame(Tienda_Main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 430, 571, 101))
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
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/new/art_pint/usuario (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Your_users.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u"../assets/icons/new/art_pint/grupo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.More_users.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u"../assets/icons/new/art_pint/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_Main.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u"../assets/icons/new/art_pint/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.New_Users.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u"../assets/icons/new/art_pint/ajustes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Confg.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u"../assets/icons/new/art_pint/abra-bloqueo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_Users.setIcon(icon10)
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
        self.frame_3 = QFrame(Tienda_Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(300, 10, 281, 411))
        self.frame_3.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Open_Recibos = QPushButton(self.frame_3)
        self.Open_Recibos.setObjectName(u"Open_Recibos")
        self.Open_Recibos.setGeometry(QRect(10, 60, 261, 61))
        self.Open_Recibos.setFont(font)
        self.Open_Recibos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Open_Recibos.setFocusPolicy(Qt.NoFocus)
        self.Open_Recibos.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../assets/icons/new/art_pint/reserva.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Open_Recibos.setIcon(icon11)
        self.Open_Recibos.setIconSize(QSize(50, 50))
        self.Open_Recibos.setFlat(True)
        self.New_Recibo = QPushButton(self.frame_3)
        self.New_Recibo.setObjectName(u"New_Recibo")
        self.New_Recibo.setGeometry(QRect(10, 200, 261, 61))
        self.New_Recibo.setFont(font)
        self.New_Recibo.setCursor(QCursor(Qt.PointingHandCursor))
        self.New_Recibo.setFocusPolicy(Qt.NoFocus)
        self.New_Recibo.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../assets/icons/new/art_pint/presupuesto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.New_Recibo.setIcon(icon12)
        self.New_Recibo.setIconSize(QSize(50, 50))
        self.New_Recibo.setFlat(True)
        self.Edit_Recibo = QPushButton(self.frame_3)
        self.Edit_Recibo.setObjectName(u"Edit_Recibo")
        self.Edit_Recibo.setGeometry(QRect(10, 130, 261, 61))
        self.Edit_Recibo.setFont(font)
        self.Edit_Recibo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Edit_Recibo.setFocusPolicy(Qt.NoFocus)
        self.Edit_Recibo.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"../assets/icons/new/art_pint/documento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Edit_Recibo.setIcon(icon13)
        self.Edit_Recibo.setIconSize(QSize(50, 50))
        self.Edit_Recibo.setFlat(True)
        self.Delate_Recibo = QPushButton(self.frame_3)
        self.Delate_Recibo.setObjectName(u"Delate_Recibo")
        self.Delate_Recibo.setGeometry(QRect(10, 270, 261, 61))
        self.Delate_Recibo.setFont(font)
        self.Delate_Recibo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Delate_Recibo.setFocusPolicy(Qt.NoFocus)
        self.Delate_Recibo.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"../assets/icons/new/art_pint/archivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Delate_Recibo.setIcon(icon14)
        self.Delate_Recibo.setIconSize(QSize(50, 50))
        self.Delate_Recibo.setFlat(True)
        self.Ajustes_Recibo = QPushButton(self.frame_3)
        self.Ajustes_Recibo.setObjectName(u"Ajustes_Recibo")
        self.Ajustes_Recibo.setGeometry(QRect(10, 340, 261, 61))
        self.Ajustes_Recibo.setFont(font)
        self.Ajustes_Recibo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ajustes_Recibo.setFocusPolicy(Qt.NoFocus)
        self.Ajustes_Recibo.setStyleSheet(u"*{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#3a3a3a;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#1e1e1e;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"../assets/icons/new/art_pint/documento (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ajustes_Recibo.setIcon(icon15)
        self.Ajustes_Recibo.setIconSize(QSize(50, 50))
        self.Ajustes_Recibo.setFlat(True)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 20, 281, 31))

        self.retranslateUi(Tienda_Main)

        QMetaObject.connectSlotsByName(Tienda_Main)
    # setupUi

    def retranslateUi(self, Tienda_Main):
        Tienda_Main.setWindowTitle(QCoreApplication.translate("Tienda_Main", u"Tienda Main", None))
        self.Ver_Productos.setText(QCoreApplication.translate("Tienda_Main", u"Ver Productos       ", None))
        self.Anadir_Productos.setText(QCoreApplication.translate("Tienda_Main", u"A\u00f1adir Producto   ", None))
        self.Editar_Productos.setText(QCoreApplication.translate("Tienda_Main", u"Editar Producto    ", None))
        self.Eliminar_Productos.setText(QCoreApplication.translate("Tienda_Main", u"Eliminar Producto", None))
        self.Ajustes_Productos.setText(QCoreApplication.translate("Tienda_Main", u"Ajustes de Productos", None))
        self.label.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Productos</span></p></body></html>", None))
        self.Your_users.setText("")
        self.More_users.setText("")
        self.Close_Main.setText("")
        self.New_Users.setText("")
        self.Confg.setText("")
        self.Close_Users.setText("")
        self.label_3.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cerrar</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Sesion</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">A\u00f1adir</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Usuario</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Ver todos</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#2d2d2d;\">los Usrs.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Confg.</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Tu</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#2d2d2d;\">Cuenta</span></p></body></html>", None))
        self.Open_Recibos.setText(QCoreApplication.translate("Tienda_Main", u" Abrir Recibos     ", None))
        self.New_Recibo.setText(QCoreApplication.translate("Tienda_Main", u"A\u00f1adir Recibo   ", None))
        self.Edit_Recibo.setText(QCoreApplication.translate("Tienda_Main", u" Editar Recibo   ", None))
        self.Delate_Recibo.setText(QCoreApplication.translate("Tienda_Main", u"Eliminar Recibo", None))
        self.Ajustes_Recibo.setText(QCoreApplication.translate("Tienda_Main", u"Ajustes de Recibo", None))
        self.label_2.setText(QCoreApplication.translate("Tienda_Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Recibo</span></p></body></html>", None))
    # retranslateUi

