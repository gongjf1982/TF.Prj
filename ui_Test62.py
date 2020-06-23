# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Test62.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm2(object):
    def setupUi(self, MainForm2):
        MainForm2.setObjectName("MainForm2")
        MainForm2.resize(523, 285)
        self.centralwidget = QtWidgets.QWidget(MainForm2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 30, 331, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        MainForm2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainForm2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm2)
        self.statusbar.setObjectName("statusbar")
        MainForm2.setStatusBar(self.statusbar)
        self.actionOpen_O = QtWidgets.QAction(MainForm2)
        self.actionOpen_O.setObjectName("actionOpen_O")
        self.actionClose_X = QtWidgets.QAction(MainForm2)
        self.actionClose_X.setObjectName("actionClose_X")
        self.actionNew_N = QtWidgets.QAction(MainForm2)
        self.actionNew_N.setObjectName("actionNew_N")
        self.menuFile.addAction(self.actionOpen_O)
        self.menuFile.addAction(self.actionClose_X)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_N)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainForm2)
        QtCore.QMetaObject.connectSlotsByName(MainForm2)

    def retranslateUi(self, MainForm2):
        _translate = QtCore.QCoreApplication.translate
        MainForm2.setWindowTitle(_translate("MainForm2", "MainWindow"))
        self.menuFile.setTitle(_translate("MainForm2", "File"))
        self.actionOpen_O.setText(_translate("MainForm2", "Open(&O)"))
        self.actionOpen_O.setShortcut(_translate("MainForm2", "Alt+O"))
        self.actionClose_X.setText(_translate("MainForm2", "Close(&X)"))
        self.actionClose_X.setShortcut(_translate("MainForm2", "Alt+X"))
        self.actionNew_N.setText(_translate("MainForm2", "New(&N)"))
        self.actionNew_N.setShortcut(_translate("MainForm2", "Alt+N"))
