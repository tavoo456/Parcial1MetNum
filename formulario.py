# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Formulario ParcialNgIuMf.ui'
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
        font.setPointSize(14)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 191, 21))
        self.label.setFont(font)
        self.txtFuncionMC = QLineEdit(self.tab)
        self.txtFuncionMC.setObjectName(u"txtFuncionMC")
        self.txtFuncionMC.setGeometry(QRect(230, 20, 150, 20))
        self.txtFuncionMC.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 90, 171, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 130, 21, 16))
        self.label_3.setFont(font)
        self.txtA = QLineEdit(self.tab)
        self.txtA.setObjectName(u"txtA")
        self.txtA.setGeometry(QRect(450, 130, 60, 20))
        self.txtA.setFont(font)
        self.txtB = QLineEdit(self.tab)
        self.txtB.setObjectName(u"txtB")
        self.txtB.setGeometry(QRect(570, 130, 60, 20))
        self.txtB.setFont(font)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 130, 21, 16))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 90, 241, 21))
        self.label_8.setFont(font)
        self.txtToleranciaMC = QLineEdit(self.tab)
        self.txtToleranciaMC.setObjectName(u"txtToleranciaMC")
        self.txtToleranciaMC.setGeometry(QRect(250, 90, 110, 20))
        self.txtToleranciaMC.setFont(font)
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 130, 231, 20))
        self.label_9.setFont(font)
        self.txtNIteracionesMC = QLineEdit(self.tab)
        self.txtNIteracionesMC.setObjectName(u"txtNIteracionesMC")
        self.txtNIteracionesMC.setGeometry(QRect(250, 130, 110, 20))
        self.txtNIteracionesMC.setFont(font)
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 180, 1241, 445))
        self.tabWidget_2.setFont(font)
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
        self.btnCalcularBiseccion.setGeometry(QRect(40, 10, 231, 45))
        self.btnCalcularBiseccion.setFont(font)
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
        self.twFalsaPosicion.setFont(font)
        self.twFalsaPosicion.setColumnCount(8)
        self.twFalsaPosicion.horizontalHeader().setCascadingSectionResizes(True)
        self.twFalsaPosicion.horizontalHeader().setDefaultSectionSize(154)
        self.twFalsaPosicion.horizontalHeader().setHighlightSections(False)
        self.twFalsaPosicion.horizontalHeader().setStretchLastSection(False)
        self.btnCalcularFalsaPosicion = QPushButton(self.tab_6)
        self.btnCalcularFalsaPosicion.setObjectName(u"btnCalcularFalsaPosicion")
        self.btnCalcularFalsaPosicion.setGeometry(QRect(40, 10, 271, 45))
        self.btnCalcularFalsaPosicion.setFont(font)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 50, 271, 31))
        self.label_10.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 180, 1241, 445))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btnCalcularPuntoFijo = QPushButton(self.tab_3)
        self.btnCalcularPuntoFijo.setObjectName(u"btnCalcularPuntoFijo")
        self.btnCalcularPuntoFijo.setGeometry(QRect(40, 10, 241, 45))
        self.btnCalcularPuntoFijo.setFont(font)
        self.twPuntoFijo = QTableWidget(self.tab_3)
        if (self.twPuntoFijo.columnCount() < 4):
            self.twPuntoFijo.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.twPuntoFijo.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.twPuntoFijo.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.twPuntoFijo.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.twPuntoFijo.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        self.twPuntoFijo.setObjectName(u"twPuntoFijo")
        self.twPuntoFijo.setGeometry(QRect(0, 60, 1240, 350))
        self.twPuntoFijo.setFont(font)
        self.twPuntoFijo.setColumnCount(4)
        self.twPuntoFijo.horizontalHeader().setCascadingSectionResizes(True)
        self.twPuntoFijo.horizontalHeader().setDefaultSectionSize(310)
        self.twPuntoFijo.horizontalHeader().setHighlightSections(False)
        self.twPuntoFijo.horizontalHeader().setStretchLastSection(False)
        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(360, 10, 361, 21))
        self.label_14.setFont(font)
        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(360, 30, 361, 21))
        self.label_15.setFont(font)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.btnCalcularNewtonRaphson = QPushButton(self.tab_4)
        self.btnCalcularNewtonRaphson.setObjectName(u"btnCalcularNewtonRaphson")
        self.btnCalcularNewtonRaphson.setGeometry(QRect(40, 10, 311, 45))
        self.btnCalcularNewtonRaphson.setFont(font)
        self.twNewtonRaphson = QTableWidget(self.tab_4)
        if (self.twNewtonRaphson.columnCount() < 4):
            self.twNewtonRaphson.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.twNewtonRaphson.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.twNewtonRaphson.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.twNewtonRaphson.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.twNewtonRaphson.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.twNewtonRaphson.setObjectName(u"twNewtonRaphson")
        self.twNewtonRaphson.setGeometry(QRect(0, 60, 1240, 350))
        self.twNewtonRaphson.setFont(font)
        self.twNewtonRaphson.setColumnCount(4)
        self.twNewtonRaphson.horizontalHeader().setCascadingSectionResizes(True)
        self.twNewtonRaphson.horizontalHeader().setDefaultSectionSize(310)
        self.twNewtonRaphson.horizontalHeader().setHighlightSections(False)
        self.twNewtonRaphson.horizontalHeader().setStretchLastSection(False)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.btnCalcularSecante = QPushButton(self.tab_7)
        self.btnCalcularSecante.setObjectName(u"btnCalcularSecante")
        self.btnCalcularSecante.setGeometry(QRect(40, 10, 311, 45))
        self.btnCalcularSecante.setFont(font)
        self.twSecante = QTableWidget(self.tab_7)
        if (self.twSecante.columnCount() < 7):
            self.twSecante.setColumnCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.twSecante.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        self.twSecante.setObjectName(u"twSecante")
        self.twSecante.setGeometry(QRect(0, 60, 1240, 350))
        self.twSecante.setFont(font)
        self.twSecante.setColumnCount(7)
        self.twSecante.horizontalHeader().setCascadingSectionResizes(True)
        self.twSecante.horizontalHeader().setDefaultSectionSize(177)
        self.twSecante.horizontalHeader().setHighlightSections(False)
        self.twSecante.horizontalHeader().setStretchLastSection(False)
        self.label_16 = QLabel(self.tab_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 20, 121, 21))
        self.txtXi_1 = QLineEdit(self.tab_7)
        self.txtXi_1.setObjectName(u"txtXi_1")
        self.txtXi_1.setGeometry(QRect(490, 20, 110, 20))
        self.txtXi_1.setFont(font)
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.btnCalcularSecanteModificada = QPushButton(self.tab_8)
        self.btnCalcularSecanteModificada.setObjectName(u"btnCalcularSecanteModificada")
        self.btnCalcularSecanteModificada.setGeometry(QRect(40, 10, 331, 45))
        self.btnCalcularSecanteModificada.setFont(font)
        self.twSecanteModificada = QTableWidget(self.tab_8)
        if (self.twSecanteModificada.columnCount() < 8):
            self.twSecanteModificada.setColumnCount(8)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.twSecanteModificada.setHorizontalHeaderItem(7, __qtablewidgetitem38)
        self.twSecanteModificada.setObjectName(u"twSecanteModificada")
        self.twSecanteModificada.setGeometry(QRect(0, 60, 1240, 350))
        self.twSecanteModificada.setFont(font)
        self.twSecanteModificada.setColumnCount(8)
        self.twSecanteModificada.horizontalHeader().setCascadingSectionResizes(True)
        self.twSecanteModificada.horizontalHeader().setDefaultSectionSize(154)
        self.twSecanteModificada.horizontalHeader().setHighlightSections(False)
        self.twSecanteModificada.horizontalHeader().setStretchLastSection(False)
        self.txtdxi = QLineEdit(self.tab_8)
        self.txtdxi.setObjectName(u"txtdxi")
        self.txtdxi.setGeometry(QRect(520, 20, 110, 20))
        self.txtdxi.setFont(font)
        self.label_17 = QLabel(self.tab_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(390, 20, 121, 21))
        self.label_18 = QLabel(self.tab_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(640, 20, 311, 16))
        self.tabWidget_3.addTab(self.tab_8, "")
        self.txtFuncionMA = QLineEdit(self.tab_2)
        self.txtFuncionMA.setObjectName(u"txtFuncionMA")
        self.txtFuncionMA.setGeometry(QRect(230, 10, 150, 20))
        self.txtFuncionMA.setFont(font)
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 120, 231, 20))
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 80, 241, 21))
        self.label_12.setFont(font)
        self.txtNIteracionesMA = QLineEdit(self.tab_2)
        self.txtNIteracionesMA.setObjectName(u"txtNIteracionesMA")
        self.txtNIteracionesMA.setGeometry(QRect(250, 120, 110, 20))
        self.txtNIteracionesMA.setFont(font)
        self.txtToleranciaMA = QLineEdit(self.tab_2)
        self.txtToleranciaMA.setObjectName(u"txtToleranciaMA")
        self.txtToleranciaMA.setGeometry(QRect(250, 80, 110, 20))
        self.txtToleranciaMA.setFont(font)
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 40, 271, 31))
        self.label_13.setFont(font)
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 10, 191, 21))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 70, 301, 31))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 120, 49, 16))
        self.txtAproximacionInicial = QLineEdit(self.tab_2)
        self.txtAproximacionInicial.setObjectName(u"txtAproximacionInicial")
        self.txtAproximacionInicial.setGeometry(QRect(490, 120, 113, 21))
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
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


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
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Error", None));
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
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.btnCalcularFalsaPosicion.setText(QCoreApplication.translate("MainWindow", u"Calcular por Falsa Posici\u00f3n", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"M\u00e9todo de Falsa Posici\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ejemplo: x**5 + x**2 - 3*x + 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"M\u00e9todos Cerrados", None))
        self.btnCalcularPuntoFijo.setText(QCoreApplication.translate("MainWindow", u"Calcular por Punto Fijo", None))
        ___qtablewidgetitem16 = self.twPuntoFijo.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de iteraci\u00f3n", None));
        ___qtablewidgetitem17 = self.twPuntoFijo.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Xo", None));
        ___qtablewidgetitem18 = self.twPuntoFijo.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"g(Xo)", None));
        ___qtablewidgetitem19 = self.twPuntoFijo.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Para obtener resultado satisfactorios", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ingrese la funci\u00f3n despejada", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"M\u00e9todo del punto fijo", None))
        self.btnCalcularNewtonRaphson.setText(QCoreApplication.translate("MainWindow", u"Calcular por Newton Raphson", None))
        ___qtablewidgetitem20 = self.twNewtonRaphson.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de iteraci\u00f3n", None));
        ___qtablewidgetitem21 = self.twNewtonRaphson.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Xo", None));
        ___qtablewidgetitem22 = self.twNewtonRaphson.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Xr", None));
        ___qtablewidgetitem23 = self.twNewtonRaphson.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"M\u00e9todo de Newton Raphson", None))
        self.btnCalcularSecante.setText(QCoreApplication.translate("MainWindow", u"Calcular por Secante", None))
        ___qtablewidgetitem24 = self.twSecante.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Iteracion", None));
        ___qtablewidgetitem25 = self.twSecante.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Xi-1", None));
        ___qtablewidgetitem26 = self.twSecante.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem27 = self.twSecante.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"f(Xi-1)", None));
        ___qtablewidgetitem28 = self.twSecante.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"f(Xi)", None));
        ___qtablewidgetitem29 = self.twSecante.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Xi+1", None));
        ___qtablewidgetitem30 = self.twSecante.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ingrese Xi-1:", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"M\u00e9todo de la Secante", None))
        self.btnCalcularSecanteModificada.setText(QCoreApplication.translate("MainWindow", u"Calcular por Secante Modificada", None))
        ___qtablewidgetitem31 = self.twSecanteModificada.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Iteraci\u00f3n", None));
        ___qtablewidgetitem32 = self.twSecanteModificada.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem33 = self.twSecanteModificada.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"dxi", None));
        ___qtablewidgetitem34 = self.twSecanteModificada.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Xi + dxi", None));
        ___qtablewidgetitem35 = self.twSecanteModificada.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"f(Xi)", None));
        ___qtablewidgetitem36 = self.twSecanteModificada.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"f(Xi + dxi)", None));
        ___qtablewidgetitem37 = self.twSecanteModificada.horizontalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Xi+1", None));
        ___qtablewidgetitem38 = self.twSecanteModificada.horizontalHeaderItem(7)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Error", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Ingrese dxi:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"dxi es eficiente si ronda por 0.01", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"M\u00e9todo de la Secante Modificada", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo de Iteraciones:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ingrese la Tolerancia (%):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ejemplo: x**5 + x**2 - 3*x + 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ingrese la Funci\u00f3n:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ingrese la aproximaci\u00f3n Inicial:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Xo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"M\u00e9todos Abiertos", None))
    # retranslateUi

