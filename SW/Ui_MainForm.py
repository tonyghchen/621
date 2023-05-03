# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 960)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 960))
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 1241, 901))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Home = QtWidgets.QWidget()
        self.tab_Home.setObjectName("tab_Home")
        self.horizontalSlider_gauge = QtWidgets.QSlider(self.tab_Home)
        self.horizontalSlider_gauge.setGeometry(QtCore.QRect(80, 230, 251, 22))
        self.horizontalSlider_gauge.setMaximum(100)
        self.horizontalSlider_gauge.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_gauge.setInvertedAppearance(False)
        self.horizontalSlider_gauge.setInvertedControls(False)
        self.horizontalSlider_gauge.setObjectName("horizontalSlider_gauge")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_Home)
        self.horizontalSlider.setGeometry(QtCore.QRect(420, 540, 691, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_Silder = QtWidgets.QLabel(self.tab_Home)
        self.label_Silder.setGeometry(QtCore.QRect(710, 580, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Silder.setFont(font)
        self.label_Silder.setObjectName("label_Silder")
        self.widget = AnalogGaugeWidget(self.tab_Home)
        self.widget.setGeometry(QtCore.QRect(50, 10, 311, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(200, 200))
        self.widget.setMaximumSize(QtCore.QSize(600, 600))
        self.widget.setBaseSize(QtCore.QSize(300, 300))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Reset = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_Reset.setGeometry(QtCore.QRect(50, 720, 161, 121))
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.pushButton_Test = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_Test.setGeometry(QtCore.QRect(210, 620, 161, 91))
        self.pushButton_Test.setObjectName("pushButton_Test")
        self.pushButton_SPHome = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_SPHome.setGeometry(QtCore.QRect(50, 630, 161, 81))
        self.pushButton_SPHome.setObjectName("pushButton_SPHome")
        self.pushButton_StopCycle = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_StopCycle.setGeometry(QtCore.QRect(210, 720, 161, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.pushButton_StopCycle.setFont(font)
        self.pushButton_StopCycle.setObjectName("pushButton_StopCycle")
        self.pushButton_MPG = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_MPG.setGeometry(QtCore.QRect(210, 520, 161, 91))
        self.pushButton_MPG.setObjectName("pushButton_MPG")
        self.pushButton_Home = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_Home.setGeometry(QtCore.QRect(50, 560, 161, 71))
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.pushButton_Auto = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_Auto.setGeometry(QtCore.QRect(130, 520, 81, 41))
        self.pushButton_Auto.setObjectName("pushButton_Auto")
        self.pushButton_VR = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_VR.setGeometry(QtCore.QRect(50, 520, 81, 41))
        self.pushButton_VR.setObjectName("pushButton_VR")
        self.tabWidget.addTab(self.tab_Home, "")
        self.tab_File = QtWidgets.QWidget()
        self.tab_File.setObjectName("tab_File")
        self.tabWidget.addTab(self.tab_File, "")
        self.tab_Paramter = QtWidgets.QWidget()
        self.tab_Paramter.setObjectName("tab_Paramter")
        self.tabWidget.addTab(self.tab_Paramter, "")
        self.pushButton_EDIT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EDIT.setGeometry(QtCore.QRect(60, 0, 251, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_EDIT.setFont(font)
        self.pushButton_EDIT.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.pushButton_EDIT.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_EDIT.setObjectName("pushButton_EDIT")
        self.pushButton_EDIT_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EDIT_2.setGeometry(QtCore.QRect(310, 0, 251, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_EDIT_2.setFont(font)
        self.pushButton_EDIT_2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.pushButton_EDIT_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_EDIT_2.setObjectName("pushButton_EDIT_2")
        self.pushButton_EDIT_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EDIT_3.setGeometry(QtCore.QRect(560, 0, 251, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_EDIT_3.setFont(font)
        self.pushButton_EDIT_3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.pushButton_EDIT_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_EDIT_3.setObjectName("pushButton_EDIT_3")
        self.pushButton_EDIT_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EDIT_4.setGeometry(QtCore.QRect(810, 0, 251, 45))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_EDIT_4.setFont(font)
        self.pushButton_EDIT_4.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.pushButton_EDIT_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_EDIT_4.setObjectName("pushButton_EDIT_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XINDA SERVO SYSTEM"))
        self.label_Silder.setText(_translate("MainWindow", "0"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_Test.setText(_translate("MainWindow", "TEST"))
        self.pushButton_SPHome.setText(_translate("MainWindow", "SP-Home"))
        self.pushButton_StopCycle.setText(_translate("MainWindow", "Stop \n"
" Cycle"))
        self.pushButton_MPG.setText(_translate("MainWindow", "MPG"))
        self.pushButton_Home.setText(_translate("MainWindow", "Home"))
        self.pushButton_Auto.setText(_translate("MainWindow", "Auto"))
        self.pushButton_VR.setText(_translate("MainWindow", "VR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Home), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_File), _translate("MainWindow", "File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Paramter), _translate("MainWindow", "Paramter"))
        self.pushButton_EDIT.setText(_translate("MainWindow", "Home Page"))
        self.pushButton_EDIT_2.setText(_translate("MainWindow", "File Manage"))
        self.pushButton_EDIT_3.setText(_translate("MainWindow", "Edit"))
        self.pushButton_EDIT_4.setText(_translate("MainWindow", "Paramter"))
from analoggaugewidget import AnalogGaugeWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
