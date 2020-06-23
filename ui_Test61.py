# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Test61.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildrenForm2(object):
    def setupUi(self, ChildrenForm2):
        ChildrenForm2.setObjectName("ChildrenForm2")
        ChildrenForm2.resize(372, 186)
        self.label_2 = QtWidgets.QLabel(ChildrenForm2)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 231, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/img/2.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ChildrenForm2)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm2)

    def retranslateUi(self, ChildrenForm2):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm2.setWindowTitle(_translate("ChildrenForm2", "Form"))


import app_rc