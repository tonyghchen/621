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

'''
#from asyncio.windows_events import NULL
from cmath import isclose
from contextlib import nullcontext
from fileinput import close
import serial
import sys
import os
#import analoggaugewidget #as analoggaugewidget


from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt, QPoint

#from analoggaugewidget import *

from Ui_MainForm import *

# ----------------------------------------------------------------------
# Http Download
# ----------------------------------------------------------------------
gVersion = "1.6.3"

# ----------------------------------------------------------------------
# Globle Definition
# ----------------------------------------------------------------------

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

# ------------------------------------------------------------------
#   Parameter
# ------------------------------------------------------------------

# ----------------------------------------------------------------------
# Main Window
# ----------------------------------------------------------------------
class MyMainWindow(QMainWindow, Ui_MainWindow):

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

        self.pushButton_Reset.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_StopCycle.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_Test.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_MPG.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_SPHome.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_Home.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_VR.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')
        self.pushButton_Auto.setStyleSheet('background-color: rgb(244, 249, 253);border-radius: 10px; border: 3px groove gray;border-style: outset;')

        # 创建一个 QLabel 控件用于显示方框的大小
        #self.label = QLabel('Size: 50', self)
        #self.label_Silder.setGeometry(160, 40, 80, 30)     # 设置 QLabel 的位置和大小

        # 设置窗口标题和大小，并显示窗口
        self.setWindowTitle('QSlider Example')
        self.setGeometry(300, 300, 250, 150)
        self.show()

    # ----------------------------------------------------------------------
    # Description:  Init UI 
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
        
# ----------------------------------------------------------------------
# Function : Main Program
# ----------------------------------------------------------------------
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')

    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

