# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Test1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 100, 54, 12))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 23))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action13 = QtWidgets.QAction(MainWindow)
        self.action13.setObjectName("action13")
        self.action14 = QtWidgets.QAction(MainWindow)
        self.action14.setObjectName("action14")
        self.menu_1.addAction(self.action1)
        self.menu_1.addAction(self.action2)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.action3)
        self.menu_1.addAction(self.action4)
        self.menu_2.addAction(self.action11)
        self.menu_2.addAction(self.action12)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action13)
        self.menu_2.addAction(self.action14)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt测试项目"))
        self.pushButton.setText(_translate("MainWindow", "按钮"))
        self.label.setText(_translate("MainWindow", "显示标签"))
        self.menu_1.setTitle(_translate("MainWindow", "测试1"))
        self.menu_2.setTitle(_translate("MainWindow", "测试2"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
        self.action4.setText(_translate("MainWindow", "4"))
        self.action11.setText(_translate("MainWindow", "11"))
        self.action12.setText(_translate("MainWindow", "12"))
        self.action13.setText(_translate("MainWindow", "13"))
        self.action14.setText(_translate("MainWindow", "14"))
