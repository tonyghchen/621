# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\621\SW\MainForm.ui'
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
        self.tabWidget.setGeometry(QtCore.QRect(140, 50, 1280, 960))
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
        self.horizontalSlider.setGeometry(QtCore.QRect(390, 800, 371, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_Silder = QtWidgets.QLabel(self.tab_Home)
        self.label_Silder.setGeometry(QtCore.QRect(950, 770, 161, 24))
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
        self.tabWidget_Home = QtWidgets.QTabWidget(self.tab_Home)
        self.tabWidget_Home.setGeometry(QtCore.QRect(380, 0, 741, 860))
        self.tabWidget_Home.setObjectName("tabWidget_Home")
        self.tab_TimeLine = QtWidgets.QWidget()
        self.tab_TimeLine.setObjectName("tab_TimeLine")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_TimeLine)
        self.graphicsView.setGeometry(QtCore.QRect(130, 0, 700, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget_VHeader = QtWidgets.QTableWidget(self.tab_TimeLine)
        self.tableWidget_VHeader.setEnabled(True)
        self.tableWidget_VHeader.setGeometry(QtCore.QRect(10, 50, 120, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_VHeader.sizePolicy().hasHeightForWidth())
        self.tableWidget_VHeader.setSizePolicy(sizePolicy)
        self.tableWidget_VHeader.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_VHeader.setSizeIncrement(QtCore.QSize(7, 4))
        self.tableWidget_VHeader.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget_VHeader.setFont(font)
        self.tableWidget_VHeader.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_VHeader.setAutoFillBackground(False)
        self.tableWidget_VHeader.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(42, 150, 171);\n"
"selection-color: rgb(250, 250, 130);")
        self.tableWidget_VHeader.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableWidget_VHeader.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget_VHeader.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_VHeader.setLineWidth(1)
        self.tableWidget_VHeader.setMidLineWidth(1)
        self.tableWidget_VHeader.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_VHeader.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_VHeader.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_VHeader.setAutoScroll(False)
        self.tableWidget_VHeader.setAutoScrollMargin(15)
        self.tableWidget_VHeader.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_VHeader.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_VHeader.setIconSize(QtCore.QSize(10, 10))
        self.tableWidget_VHeader.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_VHeader.setShowGrid(True)
        self.tableWidget_VHeader.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_VHeader.setWordWrap(True)
        self.tableWidget_VHeader.setCornerButtonEnabled(True)
        self.tableWidget_VHeader.setRowCount(15)
        self.tableWidget_VHeader.setColumnCount(1)
        self.tableWidget_VHeader.setObjectName("tableWidget_VHeader")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_VHeader.setVerticalHeaderItem(14, item)
        self.tableWidget_VHeader.horizontalHeader().setVisible(False)
        self.tableWidget_VHeader.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_VHeader.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_VHeader.horizontalHeader().setHighlightSections(True)
        self.tableWidget_VHeader.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget_VHeader.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_VHeader.verticalHeader().setVisible(False)
        self.tableWidget_VHeader.verticalHeader().setDefaultSectionSize(32)
        self.tableWidget_VHeader.verticalHeader().setHighlightSections(False)
        self.tableWidget_VHeader.verticalHeader().setMinimumSectionSize(32)
        self.tableWidget_VHeader.raise_()
        self.graphicsView.raise_()
        self.tabWidget_Home.addTab(self.tab_TimeLine, "")
        self.tab_Table = QtWidgets.QWidget()
        self.tab_Table.setObjectName("tab_Table")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_Table)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(170, 20, 500, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setSizeIncrement(QtCore.QSize(7, 4))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(42, 150, 171);\n"
"selection-color: rgb(250, 250, 130);")
        self.tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setIconSize(QtCore.QSize(10, 10))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(32)
        self.tabWidget_Home.addTab(self.tab_Table, "")
        self.tab_Repeat = QtWidgets.QWidget()
        self.tab_Repeat.setObjectName("tab_Repeat")
        self.tabWidget_Home.addTab(self.tab_Repeat, "")
        self.tab_Limit = QtWidgets.QWidget()
        self.tab_Limit.setObjectName("tab_Limit")
        self.tabWidget_Home.addTab(self.tab_Limit, "")
        self.tab_Config = QtWidgets.QWidget()
        self.tab_Config.setObjectName("tab_Config")
        self.tabWidget_Home.addTab(self.tab_Config, "")
        self.pushButton_Left = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_Left.setGeometry(QtCore.QRect(50, 340, 161, 51))
        self.pushButton_Left.setObjectName("pushButton_Left")
        self.pushButton_Right = QtWidgets.QPushButton(self.tab_Home)
        self.pushButton_Right.setGeometry(QtCore.QRect(230, 340, 161, 51))
        self.pushButton_Right.setObjectName("pushButton_Right")
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
        self.tabWidget_Home.setCurrentIndex(0)
        self.pushButton_Left.clicked.connect(MainWindow.f4RowClick) # type: ignore
        self.pushButton_Right.clicked.connect(MainWindow.f5RowClick) # type: ignore
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
        item = self.tableWidget_VHeader.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "X1"))
        item = self.tableWidget_VHeader.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "X2"))
        item = self.tableWidget_VHeader.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "X3"))
        item = self.tableWidget_VHeader.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "X4"))
        item = self.tableWidget_VHeader.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "X5"))
        item = self.tableWidget_VHeader.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "X6"))
        item = self.tableWidget_VHeader.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "X7"))
        item = self.tableWidget_VHeader.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "X8"))
        item = self.tableWidget_VHeader.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget_VHeader.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "RW"))
        item = self.tableWidget_VHeader.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "RQ"))
        item = self.tableWidget_VHeader.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Slide1"))
        item = self.tableWidget_VHeader.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Slide2"))
        item = self.tableWidget_VHeader.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Slide3"))
        item = self.tableWidget_VHeader.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "Slide4"))
        self.tabWidget_Home.setTabText(self.tabWidget_Home.indexOf(self.tab_TimeLine), _translate("MainWindow", "TimeLine"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Row"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_Home.setTabText(self.tabWidget_Home.indexOf(self.tab_Table), _translate("MainWindow", "Table"))
        self.tabWidget_Home.setTabText(self.tabWidget_Home.indexOf(self.tab_Repeat), _translate("MainWindow", "Repeat"))
        self.tabWidget_Home.setTabText(self.tabWidget_Home.indexOf(self.tab_Limit), _translate("MainWindow", "Limit"))
        self.tabWidget_Home.setTabText(self.tabWidget_Home.indexOf(self.tab_Config), _translate("MainWindow", "Config"))
        self.pushButton_Left.setText(_translate("MainWindow", "Left"))
        self.pushButton_Right.setText(_translate("MainWindow", "Right"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Home), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_File), _translate("MainWindow", "File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Paramter), _translate("MainWindow", "Paramter"))
        self.pushButton_EDIT.setText(_translate("MainWindow", "Home Page"))
        self.pushButton_EDIT_2.setText(_translate("MainWindow", "File Manage"))
        self.pushButton_EDIT_3.setText(_translate("MainWindow", "Edit"))
        self.pushButton_EDIT_4.setText(_translate("MainWindow", "Paramter"))
from analoggaugewidget import AnalogGaugeWidget
