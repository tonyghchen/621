def fGetDigitFormatFromType (digitFormat):
    switch = {"Digs1_Format" : Digs1_Format, 
              "Digs2_Format" : Digs2_Format, 
              "Digs3_Format" : Digs3_Format, 
              "Digs4_Format" : Digs4_Format, 
              "Digs5_Format" : Digs5_Format, 
              "Digs6_Format" : Digs6_Format, 
              "Digs7_Format" : Digs7_Format, 
              "Digs8_Format" : Digs8_Format, 
              "Digs1Dot1_Format" : Digs1Dot1_Format, 
              "Digs1Dot2_Format" : Digs1Dot2_Format,
              "Digs4Dot2_Format" : Digs4Dot2_Format,
              "Digs3Dot1_Format" : Digs3Dot1_Format,
              "Digs2Dot1_Format" : Digs2Dot1_Format,
              "Digs1_PN_Format" : Digs1_PN_Format,
              "Digs3_PN_Format" : Digs3_PN_Format,
              "Digs5_PN_Format" : Digs5_PN_Format,
              "Digs6_PN_Format" : Digs6_PN_Format,
              "Digs7_PN_Format" : Digs7_PN_Format,         
              "Digs4Dot2_PN_Format" : Digs4Dot2_PN_Format,
              "Digs3Dot2_PN_Format" : Digs3Dot2_PN_Format,
              "Digs4Dot1_PN_Format" : Digs4Dot1_PN_Format,
              "Digs5Dot1_PN_Format" : Digs5Dot1_PN_Format,
              }
    
    return switch.get(digitFormat, Digs1_Format)  

# ------------------------------------------------------------------
#   UART Map
# ------------------------------------------------------------------

ArrDecode_Command= {
	"MOVE_X"        : 0x00,
	"MOVE_Y"        : 0x01,
	"MOVE_Z"        : 0x02,
	"MOVE_A"        : 0x03,
	"MOVE_B"        : 0x04,
	"MOVE_C"        : 0x05,
	"MOVE_D"        : 0x06,
	"MOVE_E"        : 0x07,
	"UPDATE_LINE"   : 0x08,
	"SET_AIR"       : 0x09,
	"CLR_AIR"       : 0x0a,
	"SET_TOUCH"     : 0x0b,
	"CLR_TOUCH"     : 0x0c,
	"CLR_LOOP_AIR"  : 0x0d,
	"ZRT_Z"         : 0x0e,
	"ZRT_A"         : 0x0f,
	"ZRT_B "        : 0x10,
	"ZRT_C"         : 0x11,
	"ZRT_D "        : 0x12,
	"ZRT_E "        : 0x13,
	"MISS_X"        : 0x14,
	"MISS_Y"        : 0x15,
	"MISS_Z"        : 0x16,
	"MISS_A"        : 0x17,
	"MISS_B"        : 0x18,
	"MISS_C"        : 0x19,
	"MISS_D"        : 0x1a,
	"MISS_E"        : 0x1b,
	"MISS_UPDATE_LINE": 0x1c,
	"MISS_SET_AIR"  : 0x1d,
	"LOOP_X"        : 0x1e,
	"LOOP_Y"        : 0x1f,
	"LOOP_Z"        : 0x20,
	"LOOP_A"        : 0x21,
	"LOOP_B"        : 0x22,
	"LOOP_C"        : 0x23,
	"LOOP_D "       : 0x24,
	"LOOP_E "       : 0x25,
	"LOOP_UPDATE_LINE": 0x26,
	"LOOP_START"    : 0x27,
	"LOOP_CHECK"    : 0x28,
	"LOOP_END"      : 0x29,
	"MID_CHK"       : 0x2a,
	"END_ACT"       : 0x2b,
	"NULL_ACT_CMD"  : 0x2c,
	"CNT8254_CMD"   : 0x2d,
	"OFFSET_Y "     : 0x2e,
	"OFFSET_Y_M"    : 0x2f,
	"INCY"          : 0x30,
	"SET_DELAY"     : 0x31,
	"WAIT_DELAY"    : 0x32,
	"WAIT_MOTOR_NEAR_IN_LOOP": 0x33,
	"WAIT_MOTOR_NEAR_X" : 0x34,
	"WAIT_MOTOR_NEAR_Y" : 0x35,
	"WAIT_MOTOR_NEAR"   : 0x36,
	"WAIT_MOTOR_HOOK "  : 0x37,
	"WAIT_ZRT_X "       : 0x38,
	"LOC_PLUS_MINUS"    : 0x39,
	"LOC_MINUS_PLUS "   : 0x3a,
	"MODIFY_Y"          : 0x3b,
    "SAVE_Y"            : 0x3c,
	"SAVE_Y_MOV"        : 0x3d,
	"WAIT_MOTOR_NEAR_SERVO": 0x3e,
	"CHK_SPIN_ZRT"      : 0x3f,
	"WAIT_SPIN_ZRT"     : 0x40,
	"SETSPEED_PMFUN"    : 0x41,
	"T_STOP_MDYVAL"     : 0x42,
	"T_STOP_OFFSET"     : 0x43,
	"T_STOP_OFFSETA"    : 0x44,
	"WAIT_EXTERNAL_ENCODER": 0x45,
	"WAIT_STOP_Y_MOTOR" : 0x46,
	"CHK_TOUCH"         : 0x47,
	"DISABLE_REPAIR_Y"  : 0x48,
	"Airtbl_SET_AIR"       : 0x49,
	"Airtbl_CLR_AIR"       : 0x4A,
	"Airtbl_SET_TOUCH"     : 0x4B,
	"Airtbl_CLR_TOUCH"     : 0x4C,
}

ArrKeycode = {
    #0x60    :"HELP", #新
    0x61    :"PageUp" ,
    0x51    :"PageDown",
    0x62    :"Tab",
    0x41    :"Up",
    0x31    :"Down",
    0x30    :"Left",
    0x32    :"Right",

    0x34    :"0"   ,
    0x43    :"1"   ,
    0x44    :"2"   ,
    0x45    :"3"   ,
    0x53    :"4"   ,
    0x54    :"5"   ,
    0x55    :"6"   ,
    0x63    :"7"   ,
    0x64    :"8"   ,
    0x65    :"9"   ,
    0x33    :"Sign",
    0x35    :"Space",
    
    #0x20    :"SPECIAL",
    #0x10    :"X_Up",
    #0xa0    :"X_Down",
    0x21    :"Y_SCALE",
    #0x11    :"Y_Up",
    #0x01    :"Y_Down",
    0x22    :"SW_Z",
    #0x12    :"Z_Up",
    #0x02    :"Z_Down",
    0x23    :"SW_A",
    #0x13    :"A_Up",
    #0x03    :"A_Down",
    0x24    :"SW_B",
    #0x14    :"B_Up",
    #0x04    :"B_Down",
    0x25    :"SW_C",
    #0x15    :"C_Up",
    #0x05    :"C_Down",
    0x27    :"SW_D",
    #0x17    :"D_Up",
    #0x76    :"D_Down",
    0x28    :"SW_E",
    #0x18    :"E_Up",
    #0x8     :"E_Down",

    #0x66    :"ZRT",             #原點
    0x68    :"MODE",            #生產模式
    0x69    :"STEP",            #手輪
    0x77    :"TEST",
    #0x70    :"STOP",            #停機
    
    0x56    :"RUN1",            #單一生產
    0x57    :"Program_End",     # 程式結束
    0x58    :"Single_Variable", # 單行/變速
    #0x59   :"CLR_Y",
    0x78    :"SW_Y",
    #0x71   :"Suspend",         #修改程式

    #0x46   :"SAFE",            #安全裝置
    0x47    :"FILE_Copy",       #檔案複製
    0x48    :"LoadFromUsb",    # 讀取USB
    0x49    :"Probe",           #T
    0x79    :"SaveToUsb",    # 寫入USB
    0x72    :"Insert",          # 插入

    0x36    :"Enter",
    0x37    :"Program_Jump",    # 程式跳行
    0x38    :"Probe_DELAY",     #T延遲
    0x50    :"CylindarSetting",    # 汽缸設定
    0x73    :"Delete",           # 清除

    0x52    :"Produce_Setup",   # 生產設定
    0x26    :"Produce_Qty_0",    # 生產量歸零
    0x29    :"Cylindar",        #汽缸畫面
    0x74    :"AdvancedParam",

    0x16    :"Cut",             # 切刀
    0x42    :"Start_Active",    # 開始動作
    0x75    :"GeneralParam",    
    0x40    :"Finish_Active",   # 結束動作
    0x07    :"RESET",
    0x06    :"START",         
    #0x39    :"MARKER",
  
    0x19    :"CtrlZ",
    0x09    :"CtrlY",           
    0x80    :"OtherKey",
}
ArrStatuscode = {
    0x01    :"MAN_MODE",
    0x02    :"RUN_MODE",
    0x04    :"TEST_MODE",
    0x08    :"STEP_MODE",
    0x10    :"TMODY_MODE",
    0x20    :"SMODY_MODE",
    0x40    :"PARA_MODE",
    0x80    :"HELP_MODE",
    # 0x09    :"DIALOG_MODE",
    # 0x0A    :"INDEX_MODE",
    # 0x0B    :"USB_MODE"
}
# UART Definition
ArrUARTHeadCode = {
    'defUART_wPosition'       : {'HeadCode' : 0x06, 'SendByte' : 1},

    'defUART_wAxisSwitch'     : {'HeadCode' : 0xA5, 'SendByte' : 1},
    'defUART_wAxis'           : {'HeadCode' : 0xA7, 'SendByte' : 1},
    'defUART_wCylindarSetting': {'HeadCode' : 0xA8, 'SendByte' : 1},      #汽缸設定  
    'defUART_wManual'         : {'HeadCode' : 0xAA, 'SendByte' : 1},      #手動
    'defUART_wZeroSpeed'      : {'HeadCode' : 0xAC, 'SendByte' : 2},      #歸零速度
    'defUART_wZeroGo'         : {'HeadCode' : 0xAD, 'SendByte' : 2},      #歸零預走

    'defUART_wMotorFunction'  : {'HeadCode' : 0xAE, 'SendByte' : 2},      #馬達功能
    'defUART_wMotorType'      : {'HeadCode' : 0xAF, 'SendByte' : 2},      #馬達型態
    'defUART_wZRTSignal'      : {'HeadCode' : 0xB0, 'SendByte' : 2},      #原點信號
    'defUART_wZRTOrder'       : {'HeadCode' : 0xB1, 'SendByte' : 2},      #原點順序
    'defUART_wZRTMode'        : {'HeadCode' : 0xB2, 'SendByte' : 2},      #原點模式
    'defUART_wZRTNew'         : {'HeadCode' : 0xB3, 'SendByte' : 3},      #新設原點
    'defUART_wZRTMapping'     : {'HeadCode' : 0xB4, 'SendByte' : 2},      #原點對應
    'defUART_wFeedSignal'     : {'HeadCode' : 0xB5, 'SendByte' : 2},      #回報信號
    'defUART_wMotorStep'      : {'HeadCode' : 0xB6, 'SendByte' : 3},      #馬達格數
    'defUART_wUnitExchange'   : {'HeadCode' : 0xB7, 'SendByte' : 3},      #單位換算
    'defUART_wUnit'           : {'HeadCode' : 0xB8, 'SendByte' : 1},      #單位
    'defUART_wWireTime'       : {'HeadCode' : 0xB9, 'SendByte' : 1},      #線架時間

    'defUART_wFoldAngle'      : {'HeadCode' : 0xBA, 'SendByte' : 2},      #翻線角度
    'defUART_wSlideLimit'     : {'HeadCode' : 0xBB, 'SendByte' : 1},      #滑座極限
    'defUART_wCylinderRel'    : {'HeadCode' : 0xBC, 'SendByte' : 1},      #汽缸解除
    'defUART_wCheckOff'       : {'HeadCode' : 0xBD, 'SendByte' : 1},      #油檢解除
    'defUART_wXreverse'       : {'HeadCode' : 0xBE, 'SendByte' : 1},      #X軸反向
    'defUART_wKeyLock'        : {'HeadCode' : 0xBF, 'SendByte' : 1},      #鍵盤鎖住
    
    'defUART_wMaxLimit'       : {'HeadCode' : 0xD7, 'SendByte' : 3},      #最大極限
    'defUART_wMinLimit'       : {'HeadCode' : 0xD8, 'SendByte' : 3},      #最小極限
    'defUART_wZRTPosition'    : {'HeadCode' : 0xD9, 'SendByte' : 4},      #原點位置
    'defUART_wZRTCNT'         : {'HeadCode' : 0xDA, 'SendByte' : 3},      #原點圈數
    'defUART_wGear0'          : {'HeadCode' : 0xDB, 'SendByte' : 3},      #齒輪比0
    'defUART_wGear1'          : {'HeadCode' : 0xDC, 'SendByte' : 3},      #齒輪比1
    'defUART_wMumer'          : {'HeadCode' : 0xDD, 'SendByte' : 2},      #分周分子
    'defUART_wDemon'          : {'HeadCode' : 0xDE, 'SendByte' : 2},      #分周分母
    'defUART_wABReverse'      : {'HeadCode' : 0xDF, 'SendByte' : 1},      #AB反向

    'defUART_wModel'          : {'HeadCode' : 0xD0, 'SendByte' : 2},      #機器型號
    'defUART_wXencoder'       : {'HeadCode' : 0xD1, 'SendByte' : 1},      #X-編碼器
    'defUART_wY_Encoder'      : {'HeadCode' : 0xD2, 'SendByte' : 1},      #Y-編碼器
    'defUART_wSafeDoor'       : {'HeadCode' : 0xD3, 'SendByte' : 1},      #安全門
    'defUART_wSafeEquip'      : {'HeadCode' : 0xD4, 'SendByte' : 1},      #安全裝置
    'defUART_wAlarm'          : {'HeadCode' : 0xD5, 'SendByte' : 1},      #警示燈
    'defUART_wAutoPower'      : {'HeadCode' : 0xD6, 'SendByte' : 1},      #自動關店

    'defUART_wCurrFail'       : {'HeadCode' : 0xC1, 'SendByte' : 2},      #目前失誤
    'defUART_wSetFail'        : {'HeadCode' : 0xC2, 'SendByte' : 2},      #設定失誤
    'defUART_wCurrQty'        : {'HeadCode' : 0xC3, 'SendByte' : 3},      #目前生產
    'defUART_wSetQty'         : {'HeadCode' : 0xC4, 'SendByte' : 3},      #設定生產
    'defUART_wY_Scale'        : {'HeadCode' : 0xC5, 'SendByte' : 1},
    'defUART_wRate'           : {'HeadCode' : 0xC6, 'SendByte' : 1},
    'defUART_wMode'           : {'HeadCode' : 0xC7, 'SendByte' : 1},

    
    'defUART_wSendChk'        : {'HeadCode' : 0xFF, 'SendByte' : 1},     #SendRaspberryOK
    'defUART_wSendRReal'      : {'HeadCode' : 0xFE, 'SendByte' : 1},     #SendRaspberryOK
}

ArrErrorCode = {
	0x01:  {'ErrorCode' : 'Unconnect'       ,'ReciveByte' : 3},
	0x02:  {'ErrorCode' : 'GoHomeFail'      ,'ReciveByte' : 3},
	0x03:  {'ErrorCode' : 'SlideError'       ,'ReciveByte' : 3},
	0x04:  {'ErrorCode' : 'SlideTest'       ,'ReciveByte' : 3},
	0x05:  {'ErrorCode' : 'Miss\n START/TEST/STEP----Continue produce\n RESET------Return To Edit Screen'          ,'ReciveByte' : 3},
	0x06:  {'ErrorCode' : 'Test'          ,'ReciveByte' : 3},
	0x07:  {'ErrorCode' : 'OilError'         ,'ReciveByte' : 2},   
	0x08:  {'ErrorCode' : 'Ext.DeviceError'  ,'ReciveByte' : 2},
	0x09:  {'ErrorCode' : 'ExtEncoderError'  ,'ReciveByte' : 2},
	0x0a:  {'ErrorCode' : 'ServoFail'       ,'ReciveByte' : 2},
	0x0b:  {'ErrorCode' : 'CutterFail'      ,'ReciveByte' : 2},
	0x0c:  {'ErrorCode' : 'OverSlideLimit'  ,'ReciveByte' : 2},
	0x0d:  {'ErrorCode' : 'OverSoftLimit'   ,'ReciveByte' : 2},
    0x0e: {'ErrorCode' : 'GoHome'          ,'ReciveByte' : 2},
    0x0f: {'ErrorCode' : 'SafeError'           ,'ReciveByte' : 2},
    0x10: {'ErrorCode' : 'VirtualHome'           ,'ReciveByte' : 3},
    0x11: {'ErrorCode' : 'AdcNotZero'            ,'ReciveByte' : 2},
    0x12: {'ErrorCode' : 'NoMPG'      ,'ReciveByte' : 2},
    0x13: {'ErrorCode' : 'OverMiss'           ,'ReciveByte' : 2},
    0x14: {'ErrorCode' : 'OverQuan'           ,'ReciveByte' : 2},
    0x15: {'ErrorCode' : 'ManualSet'           ,'ReciveByte' : 3},
    0x16: {'ErrorCode' : 'AutoHome'           ,'ReciveByte' : 3},
    0x17: {'ErrorCode' : 'DispHook'           ,'ReciveByte' : 2},
}

# ------------------------------------------------------------------
#   Digits format - https://mkaz.blog/code/python-string-format-cookbook/
# ------------------------------------------------------------------

Digs1_Format     = "{:0>1d}"        # "0"
Digs2_Format     = "{:0>2d}"        # "00"
Digs3_Format     = "{:0>3d}"        # "000"
Digs4_Format     = "{:0>4d}"        # "0000"
Digs5_Format     = "{:0>5d}"        # "00000"
Digs6_Format     = "{:0>6d}"        # "00000"
Digs7_Format     = "{:0>7d}"        # "000000"
Digs8_Format     = "{:0>8d}"        # "0000000"
Digs2Dot0_Format = "{:02.0f}"       # "0.0",
Digs1Dot1_Format = "{:03.1f}"       # "0.0",
Digs1Dot2_Format = "{:04.2f}"       # "0.00"
Digs4Dot2_Format = "{:07.2f}"       # "0000.00"
Digs3Dot1_Format = "{:05.1f}"       # "000.0"
Digs2Dot1_Format = "{:04.1f}"       # "00.0"

Digs1_PN_Format  = "{:+01d}"         # "+0"
Digs3_PN_Format  = "{:+04d}"         # "+000"
Digs5_PN_Format  = "{:+06d}"        # "+00000"
Digs6_PN_Format  = "{:+07d}"        # "+000000"
Digs7_PN_Format  = "{:+08d}"        # "+000000"

Digs4Dot2_PN_Format = "{:+08.2f}"  # "+0000.00"
Digs3Dot2_PN_Format = "{:+07.2f}"  # "+000.00"
Digs4Dot1_PN_Format = "{:+07.1f}"  # "+000.00"
Digs5Dot1_PN_Format = "{:+08.1f}"   #"+00000.0",