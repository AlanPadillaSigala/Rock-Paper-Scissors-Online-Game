# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(363, 378)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 160, 321, 207))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.LMS = QLabel(self.verticalLayoutWidget)
        self.LMS.setObjectName(u"LMS")
        self.LMS.setTextFormat(Qt.AutoText)
        self.LMS.setWordWrap(False)
        self.LMS.setMargin(0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LMS)

        self.LMensajeServidor = QLabel(self.verticalLayoutWidget)
        self.LMensajeServidor.setObjectName(u"LMensajeServidor")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LMensajeServidor)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LResultado = QLabel(self.verticalLayoutWidget)
        self.LResultado.setObjectName(u"LResultado")

        self.horizontalLayout_2.addWidget(self.LResultado)

        self.LMensajeJuego = QLabel(self.verticalLayoutWidget)
        self.LMensajeJuego.setObjectName(u"LMensajeJuego")

        self.horizontalLayout_2.addWidget(self.LMensajeJuego)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LRes = QLabel(self.verticalLayoutWidget)
        self.LRes.setObjectName(u"LRes")

        self.horizontalLayout_4.addWidget(self.LRes)

        self.LRespuestaJugador = QLabel(self.verticalLayoutWidget)
        self.LRespuestaJugador.setObjectName(u"LRespuestaJugador")

        self.horizontalLayout_4.addWidget(self.LRespuestaJugador)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.formLayout)

        self.Seleccion = QComboBox(self.verticalLayoutWidget)
        self.Seleccion.addItem("")
        self.Seleccion.addItem("")
        self.Seleccion.addItem("")
        self.Seleccion.setObjectName(u"Seleccion")

        self.verticalLayout.addWidget(self.Seleccion)

        self.BJugar = QPushButton(self.verticalLayoutWidget)
        self.BJugar.setObjectName(u"BJugar")

        self.verticalLayout.addWidget(self.BJugar)

        self.BCerrar = QPushButton(self.verticalLayoutWidget)
        self.BCerrar.setObjectName(u"BCerrar")

        self.verticalLayout.addWidget(self.BCerrar)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 60, 127, 91))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RecTotal = QLabel(self.verticalLayoutWidget_2)
        self.RecTotal.setObjectName(u"RecTotal")

        self.verticalLayout_2.addWidget(self.RecTotal)

        self.marcaContadores = QHBoxLayout()
        self.marcaContadores.setObjectName(u"marcaContadores")
        self.LGT = QLabel(self.verticalLayoutWidget_2)
        self.LGT.setObjectName(u"LGT")

        self.marcaContadores.addWidget(self.LGT)

        self.LPT = QLabel(self.verticalLayoutWidget_2)
        self.LPT.setObjectName(u"LPT")

        self.marcaContadores.addWidget(self.LPT)

        self.LET = QLabel(self.verticalLayoutWidget_2)
        self.LET.setObjectName(u"LET")

        self.marcaContadores.addWidget(self.LET)


        self.verticalLayout_2.addLayout(self.marcaContadores)

        self.contadores = QHBoxLayout()
        self.contadores.setObjectName(u"contadores")
        self.ganadosT = QLCDNumber(self.verticalLayoutWidget_2)
        self.ganadosT.setObjectName(u"ganadosT")
        self.ganadosT.setFrameShape(QFrame.NoFrame)
        self.ganadosT.setFrameShadow(QFrame.Plain)
        self.ganadosT.setDigitCount(2)

        self.contadores.addWidget(self.ganadosT)

        self.perdidosT = QLCDNumber(self.verticalLayoutWidget_2)
        self.perdidosT.setObjectName(u"perdidosT")
        self.perdidosT.setFrameShape(QFrame.NoFrame)
        self.perdidosT.setFrameShadow(QFrame.Plain)
        self.perdidosT.setDigitCount(2)

        self.contadores.addWidget(self.perdidosT)

        self.empatadosT = QLCDNumber(self.verticalLayoutWidget_2)
        self.empatadosT.setObjectName(u"empatadosT")
        self.empatadosT.setFrameShape(QFrame.NoFrame)
        self.empatadosT.setFrameShadow(QFrame.Plain)
        self.empatadosT.setDigitCount(2)

        self.contadores.addWidget(self.empatadosT)


        self.verticalLayout_2.addLayout(self.contadores)

        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(210, 60, 127, 91))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.RecLocal = QLabel(self.verticalLayoutWidget_3)
        self.RecLocal.setObjectName(u"RecLocal")

        self.verticalLayout_3.addWidget(self.RecLocal)

        self.marcaContadores_2 = QHBoxLayout()
        self.marcaContadores_2.setObjectName(u"marcaContadores_2")
        self.LGL = QLabel(self.verticalLayoutWidget_3)
        self.LGL.setObjectName(u"LGL")

        self.marcaContadores_2.addWidget(self.LGL)

        self.LPL = QLabel(self.verticalLayoutWidget_3)
        self.LPL.setObjectName(u"LPL")

        self.marcaContadores_2.addWidget(self.LPL)

        self.LEL = QLabel(self.verticalLayoutWidget_3)
        self.LEL.setObjectName(u"LEL")

        self.marcaContadores_2.addWidget(self.LEL)


        self.verticalLayout_3.addLayout(self.marcaContadores_2)

        self.contadores_2 = QHBoxLayout()
        self.contadores_2.setObjectName(u"contadores_2")
        self.ganadosL = QLCDNumber(self.verticalLayoutWidget_3)
        self.ganadosL.setObjectName(u"ganadosL")
        self.ganadosL.setFrameShape(QFrame.NoFrame)
        self.ganadosL.setFrameShadow(QFrame.Plain)
        self.ganadosL.setDigitCount(2)

        self.contadores_2.addWidget(self.ganadosL)

        self.perdidosL = QLCDNumber(self.verticalLayoutWidget_3)
        self.perdidosL.setObjectName(u"perdidosL")
        self.perdidosL.setFrameShape(QFrame.NoFrame)
        self.perdidosL.setFrameShadow(QFrame.Plain)
        self.perdidosL.setDigitCount(2)

        self.contadores_2.addWidget(self.perdidosL)

        self.empatadosL = QLCDNumber(self.verticalLayoutWidget_3)
        self.empatadosL.setObjectName(u"empatadosL")
        self.empatadosL.setFrameShape(QFrame.NoFrame)
        self.empatadosL.setFrameShadow(QFrame.Plain)
        self.empatadosL.setDigitCount(2)

        self.contadores_2.addWidget(self.empatadosL)


        self.verticalLayout_3.addLayout(self.contadores_2)

        self.LJugador = QLabel(Form)
        self.LJugador.setObjectName(u"LJugador")
        self.LJugador.setGeometry(QRect(130, 10, 91, 17))
        self.opcion = QLabel(Form)
        self.opcion.setObjectName(u"opcion")
        self.opcion.setGeometry(QRect(20, 10, 67, 17))
        self.opcion.setStyleSheet(u"color: rgba(191, 64, 64, 0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Equipo 5", None))
        self.LMS.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Servidor</span></p></body></html>", None))
        self.LMensajeServidor.setText("")
        self.LResultado.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Contrincante:</span></p></body></html>", None))
        self.LMensajeJuego.setText("")
        self.LRes.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Resultado:</span></p></body></html>", None))
        self.LRespuestaJugador.setText("")
        self.Seleccion.setItemText(0, QCoreApplication.translate("Form", u"Piedra", None))
        self.Seleccion.setItemText(1, QCoreApplication.translate("Form", u"Papel", None))
        self.Seleccion.setItemText(2, QCoreApplication.translate("Form", u"Tijera", None))

        self.BJugar.setText(QCoreApplication.translate("Form", u"Jugar", None))
        self.BCerrar.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.RecTotal.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Record Total</span></p></body></html>", None))
        self.LGT.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4e9a06;\">G</span></p></body></html>", None))
        self.LPT.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#a40000;\">P</span></p></body></html>", None))
        self.LET.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#c4a000;\">E</span></p></body></html>", None))
        self.RecLocal.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Record Local</span></p></body></html>", None))
        self.LGL.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4e9a06;\">G</span></p></body></html>", None))
        self.LPL.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#a40000;\">P</span></p></body></html>", None))
        self.LEL.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#c4a000;\">E</span></p></body></html>", None))
        self.LJugador.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600; color:#a40000;\">Jugador</span></p></body></html>", None))
        self.opcion.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

