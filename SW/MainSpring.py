 # -*- coding: utf-8 -*-
'''
    Python 3.8
        install : https://itheo.tech/install-python-38-on-a-raspberry-pi

    QT designer
        downloard : https://build-system.fman.io/qt-designer-download
        version 5.11
    Window Spring Main Program
    Editor: Tony Gh Chen

    Raspi >> python3 -O MainSpring.py
        Supervisor mode# sudo python3 -O MainSpring.py

    Power On AutoRun:
        shell:
            sh /home/pi/Test/autostart.sh

        autostart.sh -
            #!/bin/bash
            (
                cd /home/pi/Test
                python3 -O MainSpring.py > /home/pi/Test/log.log 2>&1
            )
            # 2>&1 : 2: 錯誤輸出 導到 1 螢幕輸出
        Autorun.desktop :
            Exec=sh /home/pi/Test/autostart.sh

    Convert Py to exe:
        pyinstaller -F my_sum.py

    Disable RsPi Power saving
        \etc\lightdm\lightdm.conf
        Adds: xserver-command=X -s 0 -dpms
        reference : https://zhuanlan.zhihu.com/p/138039191

    Get setup environment
        pip freeze > requirements.txt
    Install environment (安裝過所有的 pip 套件)
        pip install -r requirements.txt
    APT --- ??  UART ......

    Spend Time check
        start = time.time()
        end = time.time()
        print("Time:", end - start)

    grc 資源檔 Complier
        pyrcc5 ..\Doc\ICON.qrc -o ICON_rc.py
    
    2023/5/3 安裝 plotly
        pip install pyqtgraph   繪圖用
        
    2023/6/10
        pip install PyQtChart

    2023/6/14
        pip install matplotlib
'''
#from asyncio.windows_events import NULL
from cmath import isclose
from contextlib import nullcontext
from fileinput import close

import serial
import sys
import os
import copy
import Language as Language
import EditTable as EditTable
import DataFormat as DataFormat

import matplotlib.pyplot as plt
import pyqtgraph as pg
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QSlider, QLabel, QGraphicsView
from PyQt5.QtGui  import QCursor, QColor, QPainter,QPixmap
from PyQt5.QtCore import Qt
#from analoggaugewidget import *
from Ui_MainForm import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from PyQt5.QtWidgets import QGraphicsScene


# ----------------------------------------------------------------------
# UART Setting
# ----------------------------------------------------------------------
if os.name=='posix': # Raspi Testing
    #Serial Port initialize
    ser = serial.Serial("/dev/ttyS0",115200)
    ser.ReadBufferSize  = 12800
    ser.WriteBufferSize = 12800
    ser.timeout = 0.5          #non-block read 0.5s
    ser.writeTimeout = 0.5     #timeout for write 0.5s
    ser.xonxoff = False    #disable software flow control
    ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False     #disable hardware (DSR/DTR) flow control
else:
    # Debug_Error
    ser = serial.Serial()
#    ser = serial.Serial('COM5',115200, timeout=0.5 )
    try:
        ser = serial.Serial('COM5')
        #115200,N,8,1
        ser.baudrate = 115200
        ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        ser.parity = serial.PARITY_NONE #set parity check
        ser.stopbits = serial.STOPBITS_ONE #number of stop bits
        ser.timeout = 0.5          #non-block read 0.5s
    except:
        ser.timeout = 0.5          #non-block read 0.5s

# ----------------------------------------------------------------------
# Http Download
# ----------------------------------------------------------------------
gVersion = "0.0.1"

# ----------------------------------------------------------------------
# Globle Definition
# ----------------------------------------------------------------------
# Graph Setup
y1       = []
x        = []
width    = []

BarColor = pg.mkBrush(color=(0, 0, 230))        # R G B

# ------------------------------------------------------------------
#   Parameter
# ------------------------------------------------------------------
gdicTableData       = dict()        # Table data
gGraphBarh          = dict()

# 宣告一个 8x1000 的空数组
gaGraphBarh = [[None]*8 for i in range(1000)]
gGraphText          = dict()

# ------------------------------------------------------------------
#   EDIT Tab
# ------------------------------------------------------------------
# Table Mode
defDefaultTableCol  = 0
defDefaultTableRow  = 0

defTableMaxCol      = 1000            # default Table total Rows
defTablePageCol     = 10
giEditTableCurRow   = defDefaultTableRow
giEditTableLastRow  = giEditTableCurRow
giEditTableCurCol   = defDefaultTableCol    # Default Row at N
giEditTableLastCol  = giEditTableCurCol


gdicTableTemp       = dict()    # Keyin Tamp 為按下 Enter 暫存用

# ------------------------------------------------------------------
#   Parameter
# ------------------------------------------------------------------
Graph_line_1 = pg.InfiniteLine(movable=True,  angle=90) #Vertical Line Display
Graph_line_2 = pg.InfiniteLine(movable=False, angle=90) #Vertical Line Display
Graph1_Label = None

# Mapline Setting
GraphLableXPos = 1
GraphLableYPos = -3
plt.style.use('dark_background')            # Set black ground
Graphfig, Graphax = plt.subplots()
Graphline       = Graphax.axvline(GraphLableXPos, color='r', linestyle='-', linewidth=1)
Graphline_2     = Graphax.axvline(10, color='b', linestyle='-', linewidth=1)
GraphlineLable  = Graphax.text(GraphLableXPos , GraphLableYPos, GraphLableXPos , ha='left', va='top', color='r')
gGraphline_Click = 0

# Graphic Display initialize
Graph_X1= None
Graph_X2= None
Graph_X3= None
Graph_X4= None
Graph_X5= None
Graph_X6= None
Graph_X7= None
Graph_X8= None

# ----------------------------------------------------------------------
# Main Window
# ----------------------------------------------------------------------
class MyMainWindow(QMainWindow, Ui_MainWindow):

    
    #-------------------------------------------------------------
    # Initialize Windows Key interrupt
    # Description: Key press interrupt procedure
    # Input : None
    # Return: None
    #-------------------------------------------------------------
    def Init_Keyinterrupt(self):
        #Key Press Interrupt Setting
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("0"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_0)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("1"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_1)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("2"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_2)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("3"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_3)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("4"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_4)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("5"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_5)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("6"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_6)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("7"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_7)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("8"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_8)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("9"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_9)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Space"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Spece)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Backspace"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Backspace)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Page Up"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_PageUp)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Page Down"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_PageDown)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Delete"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Delete)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Insert"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Insert)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Right"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Right)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Left"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Left)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Up"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Up)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Down"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Down)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Enter)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Tab"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Tab)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("-"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Sign)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Y"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_YSwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Z"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_ZSwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("A"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_ASwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("B"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_BSwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("C"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_CSwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("D"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_DSwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("E"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_ESwitch)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("M"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_MODE)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("T"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_TCylindar)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("R"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_RPMDisplay)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("P"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Probe)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("O"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Probe_DELAY)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("S"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Single_Variable)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("J"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_ProgramEnd)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("ESC"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_RESET)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Y"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_CtrlY)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Z"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_CtrlZ)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+F"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Y_SCALE)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+C"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Cylindar)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+C"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_CylindarSetting)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+T"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_Test)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+F"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_LoadFromUsb)
        self.ctrl_n = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+S"), self)
        self.ctrl_n.activated.connect(self.fKeyPress_SaveToUsb)

    # ----------------------------------------------------------------------
    # Number keyin management by Keyboard
    # Description: Key in Process
    # Input : None
    # Return: None
    # ----------------------------------------------------------------------
    def fKeyPress_0(self):                  self.fAll_KeyDecode("0")
    def fKeyPress_1(self):                  self.fAll_KeyDecode("1")
    def fKeyPress_2(self):                  self.fAll_KeyDecode("2")
    def fKeyPress_3(self):                  self.fAll_KeyDecode("3")
    def fKeyPress_4(self):                  self.fAll_KeyDecode("4")
    def fKeyPress_5(self):                  self.fAll_KeyDecode("5")
    def fKeyPress_6(self):                  self.fAll_KeyDecode("6")
    def fKeyPress_7(self):                  self.fAll_KeyDecode("7")
    def fKeyPress_8(self):                  self.fAll_KeyDecode("8")  # Down Key
    def fKeyPress_9(self):                  self.fAll_KeyDecode("9")
    def fKeyPress_A(self):                  self.fAll_KeyDecode("A")
    def fKeyPress_B(self):                  self.fAll_KeyDecode("B")
    def fKeyPress_C(self):                  self.fAll_KeyDecode("C")
    def fKeyPress_D(self):                  self.fAll_KeyDecode("D")
    def fKeyPress_E(self):                  self.fAll_KeyDecode("E")
    def fKeyPress_F(self):                  self.fAll_KeyDecode("F")
    def fKeyPress_G(self):                  self.fAll_KeyDecode("G")
    def fKeyPress_H(self):                  self.fAll_KeyDecode("H")
    def fKeyPress_I(self):                  self.fAll_KeyDecode("I")
    def fKeyPress_J(self):                  self.fAll_KeyDecode("J")
    def fKeyPress_K(self):                  self.fAll_KeyDecode("K")
    def fKeyPress_L(self):                  self.fAll_KeyDecode("L")
    def fKeyPress_M(self):                  self.fAll_KeyDecode("M")
    def fKeyPress_N(self):                  self.fAll_KeyDecode("N")
    def fKeyPress_O(self):                  self.fAll_KeyDecode("O")
    def fKeyPress_P(self):                  self.fAll_KeyDecode("P")
    def fKeyPress_Q(self):                  self.fAll_KeyDecode("Q")
    def fKeyPress_R(self):                  self.fAll_KeyDecode("R")
    def fKeyPress_S(self):                  self.fAll_KeyDecode("S")
    def fKeyPress_T(self):                  self.fAll_KeyDecode("T")
    def fKeyPress_U(self):                  self.fAll_KeyDecode("U")
    def fKeyPress_V(self):                  self.fAll_KeyDecode("V")
    def fKeyPress_W(self):                  self.fAll_KeyDecode("W")
    def fKeyPress_X(self):                  self.fAll_KeyDecode("X")
    def fKeyPress_Y(self):                  self.fAll_KeyDecode("Y")
    def fKeyPress_Z(self):                  self.fAll_KeyDecode("Z")
    def fKeyPress_Spece(self):              self.fAll_KeyDecode("Space")
    def fKeyPress_Backspace(self):          self.fAll_KeyDecode("Backspace")
    def fKeyPress_Right(self):              self.fAll_KeyDecode("Right")       # Right Key
    def fKeyPress_Left(self):               self.fAll_KeyDecode("Left")        # Left Key
    def fKeyPress_Down(self):               self.fAll_KeyDecode("Down")
    def fKeyPress_Up(self):                 self.fAll_KeyDecode("Up")          # Up Key
    def fKeyPress_PageUp(self):             self.fAll_KeyDecode("PageUp")
    def fKeyPress_PageDown(self):           self.fAll_KeyDecode("PageDown")    # Page Down Key
    def fKeyPress_Delete(self):             self.fAll_KeyDecode("Delete")
    def fKeyPress_Insert(self):             self.fAll_KeyDecode("Insert")    # Page Down Key
    def fKeyPress_Tab(self):                self.fAll_KeyDecode("Tab")
    def fKeyPress_Enter(self):              self.fAll_KeyDecode("Enter")
    def fKeyPress_Sign(self):               self.fAll_KeyDecode("Sign")
    def fKeyPress_YSwitch(self):            self.fAll_KeyDecode("SW_Y")
    def fKeyPress_ZSwitch(self):            self.fAll_KeyDecode("SW_Z")
    def fKeyPress_ASwitch(self):            self.fAll_KeyDecode("SW_A")
    def fKeyPress_BSwitch(self):            self.fAll_KeyDecode("SW_B")
    def fKeyPress_CSwitch(self):            self.fAll_KeyDecode("SW_C")
    def fKeyPress_DSwitch(self):            self.fAll_KeyDecode("SW_D")
    def fKeyPress_ESwitch(self):            self.fAll_KeyDecode("SW_E")
    def fKeyPress_MODE(self):               self.fAll_KeyDecode("MODE")
    def fKeyPress_RESET(self):              self.fAll_KeyDecode("RESET")
    def fKeyPress_TCylindar(self):          self.fAll_KeyDecode("FILE_Copy") # Testing #FILE_Copy
    def fKeyPress_RPMDisplay(self):         self.fAll_KeyDecode("RPMDisplay")
    def fKeyPress_CtrlY(self):              self.fAll_KeyDecode("CtrlY")
    def fKeyPress_CtrlZ(self):              self.fAll_KeyDecode("CtrlZ")
    def fKeyPress_Probe(self):              self.fAll_KeyDecode("Probe")
    def fKeyPress_Probe_DELAY(self):        self.fAll_KeyDecode("Probe_DELAY")
    def fKeyPress_Single_Variable(self):    self.fAll_KeyDecode("Single_Variable")
    def fKeyPress_Y_SCALE(self):            self.fAll_KeyDecode("Y_SCALE")
    def fKeyPress_Cylindar(self):           self.fAll_KeyDecode("Cylindar") 
    def fKeyPress_CylindarSetting(self):    self.fAll_KeyDecode("CylindarSetting") 
    def fKeyPress_ProgramEnd(self):         self.fAll_KeyDecode("Program_End") 
    def fKeyPress_Test(self):               self.fAll_KeyDecode("TEST") 
    def fKeyPress_LoadFromUsb(self):        self.fAll_KeyDecode("LoadFromUsb") 
    def fKeyPress_SaveToUsb(self):          self.fAll_KeyDecode("SaveToUsb") 

    # ----------------------------------------------------------------------
    # Function : Key in decode
    # Description: Tab Buttom color update
    # Input : None
    # Return: None
    # ----------------------------------------------------------------------
    def fAll_KeyDecode(self, sKeycode):

        # ================================================================
        #  Home/File/Parameter Tab Page Process
        # ================================================================
        lCurrentTab = self.tabWidget.currentWidget().objectName()

        if lCurrentTab == "tab_Home":

            lNextTab = self.tabWidget_Home.currentWidget().objectName()
            # ================================================================
            #  TimeLine  Tab Page Process
            # ================================================================
            if lNextTab == "tab_Table" :
                if sKeycode in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","Space"]:
                    self.fEDIT_TableKeyDigits(sKeycode)

                elif sKeycode in ["Left", "Right", "Up", "Down", "PageUp", "PageDown"]:
                    self.fEDIT_TableDirectionChange(sKeycode)

        print("Keyin:",sKeycode)

        #self.tableWidget.setCurrentCell(giEditTableCurRow, giEditTableCurCol)   # Set default Cell location

    # -----------------------------------------------------------------
    # Description:     EDIT Table
    # Function: Key Digits
    # Input :   sKeyNumber
    # Return:   None
    # -----------------------------------------------------------------
    def fEDIT_TableKeyDigits(self,iKeyNumber):
        
        global gdicTableData
        global giEditTableCurCol, giEditTableCurRow

        liAxisName = EditTable.EditTableList[giEditTableCurRow]

        # check data exist
        try:
            if gdicTableData[liAxisName] is None :
                gdicTableData[liAxisName] = {}
        except:
            gdicTableData[liAxisName] = {}

        if iKeyNumber == "Space":       # Delete all string
            if gdicTableData[liAxisName].get(giEditTableCurCol) is not None:
                gdicTableData[liAxisName][giEditTableCurCol] = ""
                self.tableWidget.setItem(giEditTableCurRow, giEditTableCurCol, QTableWidgetItem(""))  # Col 1 display reset

            print("Data Delete")
            self.Graph_TableDisplay()

        else:
            if gdicTableData[liAxisName].get(giEditTableCurCol) is None:
                gdicTableData[liAxisName][giEditTableCurCol] = None

            lsAxisData = gdicTableData[liAxisName].get(giEditTableCurCol)

            if lsAxisData is None:
                gdicTableData[liAxisName][giEditTableCurCol] = iKeyNumber 
            else:
                if len(lsAxisData) >= 4 :
                    lsAxisData = lsAxisData[1:]

                lsAxisData  = int(lsAxisData) * 10 + int(iKeyNumber)              
                gdicTableData[liAxisName][giEditTableCurCol]= str(lsAxisData)


            self.Graph_TableDisplay()

            # if gdicTableData[giEditTableCurCol].get(liAxisName) is None:
            #     gdicTableData[giEditTableCurCol][liAxisName] = None

            # lsAxisData = gdicTableData[giEditTableCurCol].get(liAxisName)

            # if lsAxisData is None:
            #     gdicTableData[giEditTableCurCol][liAxisName] = iKeyNumber 
            # else:
            #     if len(lsAxisData) >= 4 :
            #         lsAxisData = lsAxisData[1:]

            #     lsAxisData  = int(lsAxisData) * 10 + int(iKeyNumber)              
            #     gdicTableData[giEditTableCurCol][liAxisName] = str(lsAxisData)
        
            self.tableWidget.setItem(giEditTableCurRow, giEditTableCurCol, QTableWidgetItem(str(gdicTableData[liAxisName][giEditTableCurCol])))  # Col 1 display reset

            #print("Data:", gdicTableData[giEditTableCurCol][liAxisName])
        print("Data:", gdicTableData)
            
    # ----------------------------------------------------------------------
    # Function : Find SubTable Column start and End location
    # Input: Sub TableWidge
    # Return: None
    # ----------------------------------------------------------------------
    def fEDIT_GetEditTableStartEnd(self):

        liTableColStart = 0
        liTableColEnd   = 100

        return liTableColStart, liTableColEnd    

    # -----------------------------------------------------------------
    # Description:  EDIT Table
    # Function:     Direction Change
    # Input :       sKeyDirection
    # Return:       None
    # -----------------------------------------------------------------
    def fEDIT_TableDirectionChange(self, sKeyDirection):

        global giEditTableCurCol, giEditTableCurRow
        global giEditTableLastCol, giEditTableLastRow

        if sKeyDirection == "Up":
            giEditTableLastRow = giEditTableCurRow
            if giEditTableCurRow <= 0:  # When Row at first Row, no move
                giEditTableCurRow = 0                           # Always on bottom side
            else:
                giEditTableCurRow -= 1
                giEditTableLastCol = giEditTableCurCol


       # Key Down
        elif sKeyDirection == "Down":
            giEditTableLastRow = giEditTableCurRow
            if giEditTableCurRow >= (defTableMaxCol-1) :  # When Row at last Row, no move
                giEditTableCurRow = defTableMaxCol-1
            else:
                giEditTableCurRow += 1
                giEditTableLastCol = giEditTableCurCol
                self.tableWidget.setCurrentCell(giEditTableCurRow, giEditTableCurCol)   # Set default Cell location

        elif  sKeyDirection == "Left":
            litableColStart, litableColEnd = self.fEDIT_GetEditTableStartEnd()
            
            giEditTableLastRow = giEditTableCurRow
            giEditTableLastCol = giEditTableCurCol

            if giEditTableCurCol <= litableColStart:
                giEditTableCurCol = litableColStart
            else:
                giEditTableCurCol -= 1

        elif  sKeyDirection == "Right":
            litableColStart, litableColEnd = self.fEDIT_GetEditTableStartEnd()

            giEditTableLastRow = giEditTableCurRow
            giEditTableLastCol = giEditTableCurCol
            
            if giEditTableCurCol >= litableColEnd:
                giEditTableCurCol = 1       # back to G col
            else:
                giEditTableCurCol += 1

        elif sKeyDirection == "PageUp":
            giEditTableLastCol = giEditTableCurCol
            giEditTableCurCol -= defTablePageCol

            if giEditTableCurCol <= 0 :    # check Row change to bottom side
                giEditTableCurCol = 0       # Always on bottom side

        elif  sKeyDirection == "PageDown":

            giEditTableLastCol = giEditTableCurCol

            if giEditTableCurCol >= defTableMaxCol :   # check Row change to bottom side
                giEditTableCurCol = defTableMaxCol -1       # Always on bottom side

       
        self.tableWidget.setCurrentCell(giEditTableCurRow, giEditTableCurCol)   # Set default Cell location
        print("Direction Right- Current Col: " + str(giEditTableCurCol) + ", Last Col: " + str(giEditTableLastCol) )

#        self.fEdit_SelectedColorUpdate()       

    # ----------------------------------------------------------------------
    # Description:  Edit
    # Function:     Initail Various Table Data
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def fEdit_InitTableData(self, isSubTableOnly = False):

        global gdicTableData
        global gdicTableTemp

        # Clear dictionary and reset it 
        gdicTableData.clear()
        gdicTableTemp.clear()

        # Initialize Row count
        gdicTableTemp["Col"] = 0

    # ----------------------------------------------------------------------
    # Description:  Init UI 
    # Function:     initUi
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def initUI(self):
        
        # 创建一个 QSlider 控件
        #self.slider = QSlider(Qt.Horizontal, self)
        self.horizontalSlider.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider.setRange(10, 800)               # 设置滑块的取值范围
        self.horizontalSlider.setValue(50)                    # 设置滑块的初始值
        #self.horizontalSlider.setGeometry(30, 40, 100, 30)    # 设置滑块的位置和大小

        self.horizontalSlider.valueChanged[int].connect(self.changeValue)  # 绑定滑块的 valueChanged 信号和 changeValue 槽函数
        self.horizontalSlider_gauge.valueChanged[int].connect(self.changeGaugeValue)  # 绑定滑块的 valueChanged 信号和 changeValue 槽函数

        #self.horizontalSlider_gauge.setTickPosition(2)          # 下方加入刻度線
        #self.horizontalSlider_gauge.setTickInterval(50)         # 刻度線間距 ( 會有十條刻度線 )

        # Setup Gauge H slider type
        self.horizontalSlider_gauge.setStyleSheet('''
            QSlider {
                border-radius: 10px;
            }
            QSlider::groove:horizontal {
                height: 5px;
                background: #bbb;
            }
            QSlider::handle:horizontal{
                background: #08d;
                width: 16px;
                height: 16px;
                margin:-6px 0;
                border-radius:8px;
            }
            QSlider::sub-page:horizontal{
                background:#08d;
            }
        ''')

        # Push button style setting
        self.pushButton_Reset.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_StopCycle.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_Test.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_MPG.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_SPHome.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_Home.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_VR.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_Auto.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')

        # Table Widge initialize
        self.tableWidget.horizontalHeader().setVisible(True)                    # Table Widge initialize
        self.tableWidget_VHeader.verticalHeader().setVisible(True)
        self.tableWidget.setCurrentCell(giEditTableCurRow, giEditTableCurCol)   # Set default Cell location

#        self.Graph_DisplayUpdate()
#         Graph_line_1.sigDragged.connect(self.Graph_LineMove)    # Line move event
        
        # Windows Key interrupt initialize
        self.Init_Keyinterrupt()

        # 隐藏 matplotlib 工具条
        # https://developer.aliyun.com/article/396490
        Graphax.get_yaxis().set_visible(False)           # Y 座標隱藏
        Graphax.xaxis.set_ticks_position('top')          # X 座標顯示在上邊

        #ax.tick_params(axis='x', pad=-10)
        Graphax.grid(True, color='white', linestyle='--', linewidth=0.5)   # 顯示 Vertical line
        #Graphax.axvspan(2, 18, facecolor='gray', alpha=0.3)    
        # 添加文字標籤
        plt.ylim(0,200)     # Set Y display range
        plt.xlim(0,10)     # Set Y display range

        canvas = FigureCanvas(Graphfig)  # 创建一个 FigureCanvas 对象
        canvas.setGeometry(self.graphicsView.rect())
        scene = QGraphicsScene()  # 创建一个 QGraphicsScene 对象并设置大小
        scene.setSceneRect(60, 45, 600, 600)
        scene.addWidget(canvas)  # 将 FigureCanvas 添加到 QGraphicsScene 中
        self.graphicsView.setScene(scene)  # 创建一个 QGraphicsView 对象并设置场景
        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # 自动缩放场景以适应视图的大小
        #self.graphicsView.fitInView(scene.sceneRect(), Qt.IgnoreAspectRatio)

        # 设置 canvas 在 graphicsView 中的位置和大小
        #canvas_rect = QRect(-80, 0, 600, 500)
        #canvas.setGeometry(canvas_rect)

        # Graph event handling
        Graphfig.canvas.mpl_connect('button_press_event', self.Graph_mouse_click)
        Graphfig.canvas.mpl_connect('motion_notify_event',self.Graph_mouse_move)
        Graphfig.canvas.mpl_connect('button_release_event', self.Graph_mouse_release)

        # tableWidget event handling
        self.tableWidget.cellClicked.connect(self.TableWidget_clicked)  

    # ----------------------------------------------------------------------
    # Event Functions 
    # ----------------------------------------------------------------------
    # Description:  Graph_mouse_click
    # Function:     Graphic screen mouse click 
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def TableWidget_clicked(self, row, column):

        global giEditTableCurCol, giEditTableCurRow

        # Update column, row
        giEditTableCurCol = column
        giEditTableCurRow = row
        print("Clicked cell:", row, "Colume:", column)

    # ----------------------------------------------------------------------
    # Description:  TableWidget_clicked
    # Function:     TableWidget cell click check 滑鼠按鈕按下事件處理函數
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def Graph_mouse_click(self,event):

        global  gGraphline_Click

        if event.button == 1 and event.inaxes == Graphax:

            lGraphX = Graphline.get_xdata()       

            if lGraphX[0] == round(event.xdata) :
                gGraphline_Click = 1
            else:
                gGraphline_Click = 0
            
            print("Click:",lGraphX[0], ",Graph:", round(event.xdata))

        # Check mouse click x, y position
#        if event.ydata is not None:
#            print("Event Y:", event.ydata , "Event X:", event.xdata)


    # ----------------------------------------------------------------------
    # Description:  TableWidget_clicked
    # Function:     TableWidget cell click check
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    # 滑鼠Button 放開事件處理函數
    def Graph_mouse_release(self, event):

        global  gdicTableData
        global  gGraphline_Click

        NewTableData = dict()       # New shift locations

        if event.button == 1 and event.inaxes == Graphax and gGraphline_Click == 1:
            liXShift = round(event.xdata)
            Graphline.set_xdata(liXShift)

            for lsAxis, lData in gdicTableData.items():
                NewTableData[lsAxis] = {}               # Create new dictionary
                for lx_Position, lsWidth in lData.items():   

                    if gdicTableData[lsAxis].get(lx_Position) is not None:
                        NewTableData[lsAxis][liXShift] = gdicTableData[lsAxis][lx_Position]

            gdicTableData = NewTableData.copy()         # 複製新移動位置
            self.Graph_TableDisplay()
        
        gGraphline_Click = 0

    # 滑鼠移動事件處理函數
    def Graph_mouse_move(self, event):

        global  GraphlineLable
        global  gGraphline_Click

        if event.button == 1 and event.inaxes == Graphax and gGraphline_Click == 1:
            Graphline.set_xdata(event.xdata)           
            x_position = round(event.xdata)

            GraphlineLable.set_text(str("  "))      # Clear original
            GraphlineLable.set_position((x_position, GraphLableYPos))   # Set display position
            GraphlineLable.set_text(str(x_position))                    # Set display value
            Graphfig.canvas.draw()
                   

    # ----------------------------------------------------------------------
    # Description:  Graph_TableDisplay
    # Function:     Bar 數值的顯示
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def Graph_TableDisplay(self):

        global  Graph_X1,Graph_X2,Graph_X3,Graph_X4,Graph_X5,Graph_X6,Graph_X7,Graph_X8
        global  gGraphBarh
        global  gGraphText
        global  gaGraphBarh
        global  gdicTableData

        lxlimMax = 0

        gdicTableTemp = copy.deepcopy(gdicTableData)

        for lsAxis, lData in gdicTableData.items():
            coord_list = []

            liYDisplay = EditTable.ArrEDIT_TableList[lsAxis].get("Location_Y")      # Display Y Location                   
            liAxis = EditTable.ArrEDIT_TableList[lsAxis].get("Location")

            lx_Position = 0         # Set initiall value

            for lx_Position, lsWidth in lData.items():            

                #globals()["gGraphText[lx_Position]"] = Graphax.text(lx_Position + int(lsWidth)/2, liYDisplay+4, int(lsWidth), ha='center', va='center') # Disply Barh width value              

                if gdicTableData[lsAxis][lx_Position] == "":
                    gaGraphBarh[liAxis][lx_Position].remove()
                    gaGraphBarh[liAxis][lx_Position] = None
                    del gdicTableTemp[lsAxis][lx_Position]
                    print("coord_list Empty")
                else:
                    coord_list.append((lx_Position, int(lsWidth)))                      # 轉換成座標
                    # X start, width / Y start, height      
                    gaGraphBarh[liAxis][lx_Position] = plt.broken_barh(coord_list, (liYDisplay, 8), 
                                                        facecolors =EditTable.ArrEDIT_TableList[lsAxis].get("Color")) # Bar 顯示

            # Find out Max X Lim display
            if lsWidth != "":
                lxlimData = lx_Position + int(lsWidth)
                if lxlimData > lxlimMax :
                    lxlimMax = lxlimData

#            globals()[lvariable_name] = plt.broken_barh(coord_list, (liYDisplay, 8), 
#                                                        facecolors =EditTable.ArrEDIT_TableList[lsAxis].get("Color")) # Bar 顯示
        gdicTableData = copy.deepcopy(gdicTableTemp)

        if lxlimMax < 10:       lxlimMax = 10       # <10 resize
           
        print("Graph:",globals()["gGraphText"])

        plt.xlim(0,lxlimMax)     # Set Y display range
        plt.xticks(np.arange(0, lxlimMax, int(lxlimMax/10)))       # 设置x轴的刻度值为10的倍数
        plt.draw()      # Redrew display

    # ----------------------------------------------------------------------
    # Description:  Init UI 
    # Function:     initUi
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def Graph_DisplayUpdate(self):

        global Graph_X1, Graph_X2, Graph_X3

        #Graph_X1= plt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors =('tab:red'))
        #Graph_X2= plt.broken_barh([(10, 50), (100, 20), (130, 10)], (10, 9), facecolors =('tab:blue'))
        #Graph_X3= plt.broken_barh([(10, 50), (100, 20), (130, 10)], (0, 9),  facecolors =('tab:red'))


    # ----------------------------------------------------------------------
    # Description:  Init UI 
    # Function:     initUi
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def Graph_LineMove(self):

        global  Graph_line_1, Graph_line_2, Graph1_Label

        Graph_line_2.setValue(Graph_line_1.value()+10)
        Graph_line_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) # ClosedHandCursor

        #if Graph1_Label is not None:   # 如果已經存在InfLineLabel對象，則從圖形中刪除它
        #    self.plotwidget.removeItem(Graph1_Label)            
        sDisplayVal = Graph_line_1.value()
        #Graph1_Label.setPos(QtCore.QPointF(Graph_line_1.pos().x(),10.8))     # 在座標周 Y = 10 位置顯示
        Graph1_Label.setText(DataFormat.Digs2Dot0_Format.format(sDisplayVal))

        #Graph1_Label = pg.InfLineLabel(Graph_line_1, position = 0.1, text = DataFormat.Digs2Dot0_Format.format(sDisplayVal)) #, anchor=(-1, 1))             # 顯示數值       
        font = QtGui.QFont("Arial", 10)  # 創建一個 Arial 字型，大小為 10
        Graph1_Label.setFont(font)
        #self.plotwidget.addItem(Graph1_Label)  

        #sDisplayVal2 = Graph_line_2.value()
        #Graph2_Label = pg.InfLineLabel(Graph_line_2, movable = False, position = 0.1, text = DataFormat.Digs2Dot0_Format.format(sDisplayVal2)) #, anchor=(-1, 1))             # 顯示數值

    # ----------------------------------------------------------------------
    # Description:  fTimeLine_Right
    # Function:     Initail Various Table Data
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def f5RowClick(self):

        global  gaGraphBarh

        #globals()["gGraphText[0]"].remove()

        #Graph_X1.remove()     # 清除特定的绘图范围
        #gGraphText[0].remove()
#        xDisplay = 200
#        plt.xlim(0,xDisplay)     # Set display range
#        plt.xticks(np.arange(0, xDisplay, int(xDisplay/10)))       # 设置x轴的刻度值为10的倍数

        # 清除Y軸範圍在10到50的broken_barh
#        for collection in plt.gca().collections:
#            heights = collection.get_paths()[0].vertices[:, 1]
#            if (heights >= 10).any() and (heights <= 50).any():
#                collection.remove()

        gaGraphBarh[2][0].remove()
        plt.draw()          # Refresh Display


    def f4RowClick(self):

        global  gaGraphBarh
        #if  Graph_X2 is not None:
        #    Graph_X2.remove()     # 清除特定的绘图范围       
        #Graph_X2.remove()
        #gGraphText[0].remove()


        gaGraphBarh[1][0].remove()
        plt.draw()          # Refresh Display


        #xDisplay = 1000
        #plt.xlim(0,xDisplay)     # Set display range
        #plt.xticks(np.arange(0, xDisplay, int(xDisplay/10)))       # 设置x轴的刻度值为10的倍数

        #plt.draw()          # Refresh Display

    # ----------------------------------------------------------------------
    # Description:  Change Gauge Value
    # Function:     changeValue
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def changeValue(self, value):
        self.label_Silder.setText(str(value))  # 更新 QLabel 的文本
        self.update()  # 调用 update() 方法触发重绘

    def changeGaugeValue(self, value):
        #self.label_Gauge.setText(str(value))  # 更新 QLabel 的文本
        self.widget.updateValue(value)

    # ----------------------------------------------------------------------
    # Description:  Init UI 
    # Function:     initUi
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    # 重写 QWidget 的绘图事件，绘制一个方框
    def paintEvent(self, event):

        painter = QPainter(self)                # 创建一个 QPainter 对象，用于绘制图形
        painter.setPen(QColor(0, 0, 0))         # 设置画笔的颜色为黑色
        painter.setBrush(QColor(0, 0, 255))     # 设置画刷的颜色为白色
        # 计算方框的位置和大小，使其在窗口中居中显示

        x = 50 #(self.width() - self.horizontalSlider.value()) / 2
        y = 520 #(self.height() - self.horizontalSlider.value()) / 2
        width = self.horizontalSlider.value()
        height = 30 #self.horizontalSlider.value()
        # 绘制方框
        painter.drawRect(x, y, width, height)

    # ----------------------------------------------------------------------
    # Description:  Main Window initialize
    # Function:     Main System All initialize
    # Input :       
    # Return:       None
    # ----------------------------------------------------------------------
    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.initUI()
        self.fEdit_InitTableData()

    # ----------------------------------------------------------------------
    # Description:     File
    # Function: Save Edit Table
    # Input : None
    # Return: None
    # ----------------------------------------------------------------------
    def fFILE_SaveEditTable(self, fileNo):
        global gdicTableData
        global gProgramConfig_Data
        global linuxProgramPath,defProgramPath
        global gFileUSBMode,gProgramPath

        # USB mode
        if gFileUSBMode == 1 :
            # Check USB
            if self.fFile_USBCheckExist() == False :
                return
        if not os.path.isdir(gProgramPath): os.mkdir(gProgramPath)
        #if not os.path.isdir(gProgramPath + "/" + fileNo): os.mkdir(gProgramPath + "/" + fileNo)
        
        sfilename = defEditTableFile + str(fileNo)
        fileName = gProgramPath + "/" + sfilename
        print("EditTable Save: " + fileName)
        # Save EditTable
        with open(fileName,'w',encoding='utf-8') as fileStream:
            json.dump(gdicTableData, fileStream, indent = 2, ensure_ascii = False)  #save file to Json file

        # Save Red Cell
        #fileName = gProgramPath + "/" + fileNo + "/" + gEditRedCellFile
        #with open(fileName,'w',encoding='utf-8') as fileStream:
        #    json.dump(gArrRedCell, fileStream, indent = 2, ensure_ascii = False)  #save file to Json file

        sfilename = defProgramConfigFile + str(fileNo)
        fileName = gProgramPath + "/" + sfilename
        print("ProgramConfig Save: " + fileName)
        with open(fileName,'w',encoding='utf-8') as fileStream:
            json.dump(gProgramConfig_Data, fileStream, indent = 2, ensure_ascii = False)  #save file to Json file    

# ----------------------------------------------------------------------
# Function : Main Program
# ----------------------------------------------------------------------
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')

    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

