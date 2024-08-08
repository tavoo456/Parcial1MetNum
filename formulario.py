# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Formulario PacialRglAJl.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 1260, 690))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(12)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 161, 21))
        self.label.setFont(font)
        self.txtFuncionMA = QLineEdit(self.tab)
        self.txtFuncionMA.setObjectName(u"txtFuncionMA")
        self.txtFuncionMA.setGeometry(QRect(210, 20, 150, 20))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 90, 141, 31))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 130, 49, 16))
        self.txtA = QLineEdit(self.tab)
        self.txtA.setObjectName(u"txtA")
        self.txtA.setGeometry(QRect(420, 130, 60, 20))
        self.txtB = QLineEdit(self.tab)
        self.txtB.setObjectName(u"txtB")
        self.txtB.setGeometry(QRect(540, 130, 60, 20))
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 130, 49, 16))
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 201, 21))
        self.txtTolerancia = QLineEdit(self.tab)
        self.txtTolerancia.setObjectName(u"txtTolerancia")
        self.txtTolerancia.setGeometry(QRect(210, 90, 110, 20))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 130, 191, 20))
        self.txtNIteraciones = QLineEdit(self.tab)
        self.txtNIteraciones.setObjectName(u"txtNIteraciones")
        self.txtNIteraciones.setGeometry(QRect(210, 130, 110, 20))
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 180, 1241, 445))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.twBiseccion = QTableWidget(self.tab_5)
        if (self.twBiseccion.columnCount() < 8):
            self.twBiseccion.setColumnCount(8)
        font1 = QFont()
        font1.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.twBiseccion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twBiseccion.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.twBiseccion.setObjectName(u"twBiseccion")
        self.twBiseccion.setGeometry(QRect(0, 60, 1240, 350))
        self.twBiseccion.setFont(font)
        self.twBiseccion.setColumnCount(8)
        self.twBiseccion.horizontalHeader().setCascadingSectionResizes(True)
        self.twBiseccion.horizontalHeader().setDefaultSectionSize(154)
        self.twBiseccion.horizontalHeader().setHighlightSections(False)
        self.twBiseccion.horizontalHeader().setStretchLastSection(False)
        self.btnCalcularBiseccion = QPushButton(self.tab_5)
        self.btnCalcularBiseccion.setObjectName(u"btnCalcularBiseccion")
        self.btnCalcularBiseccion.setGeometry(QRect(40, 10, 210, 45))
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.twFalsaPosicion = QTableWidget(self.tab_6)
        if (self.twFalsaPosicion.columnCount() < 8):
            self.twFalsaPosicion.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.twFalsaPosicion.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.twFalsaPosicion.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.twFalsaPosicion.setObjectName(u"twFalsaPosicion")
        self.twFalsaPosicion.setGeometry(QRect(0, 60, 1240, 350))
        self.twFalsaPosicion.setColumnCount(8)
        self.twFalsaPosicion.horizontalHeader().setCascadingSectionResizes(True)
        self.twFalsaPosicion.horizontalHeader().setDefaultSectionSize(154)
        self.twFalsaPosicion.horizontalHeader().setHighlightSections(False)
        self.twFalsaPosicion.horizontalHeader().setStretchLastSection(False)
        self.btnCalcularFalsaPosicion = QPushButton(self.tab_6)
        self.btnCalcularFalsaPosicion.setObjectName(u"btnCalcularFalsaPosicion")
        self.btnCalcularFalsaPosicion.setGeometry(QRect(40, 10, 241, 45))
        self.tabWidget_2.addTab(self.tab_6, "")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(110, 50, 221, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"M\u00e9todos Num\u00e9ricos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese la Funci\u00f3n:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingrese el Rango:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ingrese la Tolerancia (%):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo de Iteraciones:", None))
        ___qtablewidgetitem = self.twBiseccion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Iteraci\u00f3n", None));
        ___qtablewidgetitem1 = self.twBiseccion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem2 = self.twBiseccion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem3 = self.twBiseccion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"m", None));
        ___qtablewidgetitem4 = self.twBiseccion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"f(a)", None));
        ___qtablewidgetitem5 = self.twBiseccion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"f(b)", None));
        ___qtablewidgetitem6 = self.twBiseccion.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"f(m)", None));
        ___qtablewidgetitem7 = self.twBiseccion.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"E", None));
        self.btnCalcularBiseccion.setText(QCoreApplication.translate("MainWindow", u"Calcular por Bisecci\u00f3n", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"M\u00e9todo de Bisecci\u00f3n", None))
        ___qtablewidgetitem8 = self.twFalsaPosicion.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Iteraci\u00f3n", None));
        ___qtablewidgetitem9 = self.twFalsaPosicion.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem10 = self.twFalsaPosicion.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem11 = self.twFalsaPosicion.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Xr", None));
        ___qtablewidgetitem12 = self.twFalsaPosicion.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"f(a)", None));
        ___qtablewidgetitem13 = self.twFalsaPosicion.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"f(b)", None));
        ___qtablewidgetitem14 = self.twFalsaPosicion.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"f(Xr)", None));
        ___qtablewidgetitem15 = self.twFalsaPosicion.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"E", None));
        self.btnCalcularFalsaPosicion.setText(QCoreApplication.translate("MainWindow", u"Calcular por Falsa Posici\u00f3n", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"M\u00e9todo de Falsa Posici\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ejemplo: x**5 + x**2 - 3*x + 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"M\u00e9todos Abiertos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"M\u00e9todos Cerrados", None))
    # retranslateUi