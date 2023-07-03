# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\621\SW_Test\MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(746, 512)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 960))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setTabletTracking(True)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Left.setGeometry(QtCore.QRect(150, 220, 161, 51))
        self.pushButton_Left.setObjectName("pushButton_Left")
        self.pushButton_Right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Right.setGeometry(QtCore.QRect(330, 220, 161, 51))
        self.pushButton_Right.setObjectName("pushButton_Right")
        self.label_F4 = QtWidgets.QLabel(self.centralwidget)
        self.label_F4.setGeometry(QtCore.QRect(170, 170, 92, 24))
        self.label_F4.setObjectName("label_F4")
        self.label_F5 = QtWidgets.QLabel(self.centralwidget)
        self.label_F5.setGeometry(QtCore.QRect(370, 170, 92, 24))
        self.label_F5.setObjectName("label_F5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_Left.clicked.connect(MainWindow.f4RowClick) # type: ignore
        self.pushButton_Right.clicked.connect(MainWindow.f5RowClick) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XINDA SERVO SYSTEM"))
        self.pushButton_Left.setText(_translate("MainWindow", "F4"))
        self.pushButton_Right.setText(_translate("MainWindow", "F5"))
        self.label_F4.setText(_translate("MainWindow", "TextLabel"))
        self.label_F5.setText(_translate("MainWindow", "TextLabel"))