# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Test3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 331)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(170, 230, 160, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton_15 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton_15)
        self.pushButton_17 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_17)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 20, 246, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(360, 20, 135, 69))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 90, 320, 121))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 4, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 4, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "用户名"))
        self.label_4.setText(_translate("Form", "密码"))
        self.pushButton_15.setText(_translate("Form", "确定"))
        self.pushButton_17.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "姓名"))
        self.pushButton.setText(_translate("Form", "提交"))
        self.label_2.setText(_translate("Form", "姓名"))
        self.pushButton_2.setText(_translate("Form", "提交"))
        self.pushButton_18.setText(_translate("Form", "/"))
        self.pushButton_5.setText(_translate("Form", "3"))
        self.pushButton_9.setText(_translate("Form", "5"))
        self.pushButton_7.setText(_translate("Form", "6"))
        self.pushButton_8.setText(_translate("Form", "4"))
        self.pushButton_4.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "1"))
        self.pushButton_10.setText(_translate("Form", "-"))
        self.pushButton_6.setText(_translate("Form", "*"))
        self.pushButton_13.setText(_translate("Form", "8"))
        self.pushButton_12.setText(_translate("Form", "7"))
        self.pushButton_11.setText(_translate("Form", "9"))
        self.pushButton_14.setText(_translate("Form", "+"))
        self.pushButton_16.setText(_translate("Form", "计算"))