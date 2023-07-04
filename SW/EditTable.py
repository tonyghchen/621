
def fEDIT_GetTableFormatFromGCode (GCode):
    switch = {"0": ArrEDIT_TableDataG0, 
              "1": ArrEDIT_TableDataG1, 
              "2": ArrEDIT_TableDataG2, 
              "3": ArrEDIT_TableDataG3, 
              "4": ArrEDIT_TableDataG4, 
              "5": ArrEDIT_TableDataG5, 
              "6": ArrEDIT_TableDataG6, 
              "7": ArrEDIT_TableDataG7, 
              "8": ArrEDIT_TableDataG8, 
              "9": ArrEDIT_TableDataG9
              }
    
    return switch.get(GCode, dict())

# ------------------------------------------------------------------
#   Edit Table List
# ------------------------------------------------------------------
EditTableList = {
    #ID     Asix
    7   :   "X8",
    6   :   "X7",
    5   :   "X6",
    4   :   "X5",
    3   :   "X4",
    2   :   "X3",
    1   :   "X2",
    0   :   "X1",
}

def fEDIT_GetAsixCode(GCode):
    for lID, lAxis in EditTableList.items():
        if GCode == lAxis :
            return  lID     
    return ("")

# --------------------------------------------------------
#               Table Data
# --------------------------------------------------------
ArrEDIT_TableList= {
    "X1"       :{ "Location"  : 0,  "Location_Y":  185,  "Barh Color" :   "#000080" ,"Border Color" :   "blue" },
    "X2"       :{ "Location"  : 1,  "Location_Y":  175,  "Barh Color" :   "#ccaa00" ,"Border Color" :   "blue" },
    "X3"       :{ "Location"  : 2,  "Location_Y":  165,  "Barh Color" :   "#000080" ,"Border Color" :   "blue" },
    "X4"       :{ "Location"  : 3,  "Location_Y":  155,  "Barh Color" :   "#ccaa00" ,"Border Color" :   "blue" },
    "X5"       :{ "Location"  : 4,  "Location_Y":  145,  "Barh Color" :   "#000080" ,"Border Color" :   "blue" },
    "X6"       :{ "Location"  : 5,  "Location_Y":  135,  "Barh Color" :   "#ccaa00" ,"Border Color" :   "blue" },
    "X7"       :{ "Location"  : 6,  "Location_Y":  125,  "Barh Color" :   "#000080" ,"Border Color" :   "blue" },
    "X8"       :{ "Location"  : 7,  "Location_Y":  115,  "Barh Color" :   "#ccaa00" ,"Border Color" :   "blue" },
    }


# ------------------------------------------------------------------
#   Edit tab Mode Name
# ------------------------------------------------------------------
# all Table Template
ArrEDIT_TableMark= {
    "X_tmp"     : "",
    "X_G0"      : "RETURN N",
    "X_Arrow"   : "▶",
    "X1_N"      : "N",
    "X2_N"      : "N",
    "Y_X"      : "X",
    "X2_G5"     : "",
    "Z_ZERO"    : "▶ZERO",
    "A_ZERO"    : "▶ZERO",
    "B_ZERO"    : "▶ZERO",
    "C_ZERO"    : "▶ZERO",
    "D_ZERO"    : "▶ZERO",
    "E_ZERO"    : "▶ZERO",
    "X_Delay"   : "延遲時間 = ",
    "Y_Add"     : "Y 增量",
    "X_ms"      : "ms",
    }

# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG1= {
    "Row"       :{ "Location8" : 0,  "Group" : "Row"    , "Width8" : 40, "Editable" : 1,  "DigitFormat" : "Digs3_Format"},
    "X1"        :{ "Location8" : 1,  "Group" : "X"      , "Width8" : 18, "Editable" : 1,  "DigitFormat" : "Digs1_Format"},
    "X2"        :{ "Location8" : 2,  "Group" : "X"      , "Width8" : 55, "Editable" : 0},
    "X3"        :{ "Location8" : 3,  "Group" : "X"      , "Width8" : 16, "Editable" : 0},    
    "X4"        :{ "Location8" : 4,  "Group" : "X"      , "Width8" : 55, "Editable" : 1,  "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue":  99999},
    "X5"        :{ "Location8" : 5,  "Group" : "X"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "X6"        :{ "Location8" : 6,  "Group" : "X"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "X7"        :{ "Location8" : 7,  "Group" : "X"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "X8"        :{ "Location8" : 8,  "Group" : "X"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "F"         :{ "Location8" : 9,  "Group" : "F"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "RW"        :{ "Location8" : 10, "Group" : "R"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "RQ"        :{ "Location8" : 11, "Group" : "R"      , "Width8" : 91, "Editable" : 1,  "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Slide1"    :{ "Location8" : 12, "Group" :"Slide"   , "Width8" : 36, "Editable" : 1,  "DigitFormat" : "MultiFormat"},
    "Slide2"    :{ "Location8" : 13, "Group" :"Slide"   , "Width8" : 13, "Editable" : 2,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "Slide3"    :{ "Location8" : 14, "Group" :"Slide"   , "Width8" : 13, "Editable" : 2,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "Slide4"    :{ "Location8" : 15, "Group" :"Slide"   , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T1"        :{ "Location8" : 16, "Group" :"T"       , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T2"        :{ "Location8" : 17, "Group" :"T"       , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T3"        :{ "Location8" : 18, "Group" :"T"       , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T4"        :{ "Location8" : 19, "Group" :"T"       , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_1"    :{ "Location8" : 20, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_2"    :{ "Location8" : 21, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_3"    :{ "Location8" : 22, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_0"    :{ "Location8" : 23, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_1"    :{ "Location8" : 24, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_2"    :{ "Location8" : 25, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_3"    :{ "Location8" : 26, "Group" :"AIR"     , "Width8" : 13, "Editable" : 1,  "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    }

# --------------------------------------------------------
#               SubTable Disaply by G Mode
# --------------------------------------------------------
AxisNoMapping = {
    "X": 0,
    "Y": 1,
    "Z": 2,
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6,
    "E": 7, 
}

# G0 Mode SubTable
#  [ Col Location, 6 axis ColWidth, 8 Axis ColWidth, Col Editable]
ArrEDIT_TableDataG0= {
    "Row"       :{ "Location6" : 0, "Width6" : 45,  "Location8" : 0, "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",         "DigitFormat" : "Digs3_Format"},
    "G"         :{ "Location6" : 1, "Width6" : 20,  "Location8" : 1, "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",         "DigitFormat" : "Digs1_Format"},
    "X_G0"      :{ "Location6" : 2, "Width6" : 110, "Location8" : 2, "Width8" : 92, "Editable" : 0, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_ReturnN"},
    "X1_G0"     :{ "Location6" : 3, "Width6" : 40,  "Location8" : 3, "Width8" : 34, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "lineEdit_EditWin_ReturnN",    "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999}
    }

# G1 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG1= {
    "Row"       :{ "Location6" : 0,  "Width6" : 45,  "Location8" : 0,  "Group" : "Row"      , "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",       "DigitFormat" : "Digs3_Format"},
    "G"         :{ "Location6" : 1,  "Width6" : 20,  "Location8" : 1,  "Group" : "G"        , "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",       "DigitFormat" : "Digs1_Format"},
    "X_tmp"     :{ "Location6" : 2,  "Width6" : 60,  "Location8" : 2,  "Group" : "X"        , "Width8" : 55, "Editable" : 0, "AxisNo" : 1},
    "X_Arrow"   :{ "Location6" : 3,  "Width6" : 20,  "Location8" : 3,  "Group" : "X"        , "Width8" : 16, "Editable" : 0, "AxisNo" : 1},
    "X_EndPos"  :{ "Location6" : 4,  "Width6" : 60,  "Location8" : 4,  "Group" : "X_EndPos" , "Width8" : 55, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_X",           "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue":  99999},
    "Y"         :{ "Location6" : 5,  "Width6" : 110, "Location8" : 5,  "Group" : "Y"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Y",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Z"         :{ "Location6" : 6,  "Width6" : 110, "Location8" : 6,  "Group" : "Z"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_Z",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "A"         :{ "Location6" : 7,  "Width6" : 110, "Location8" : 7,  "Group" : "A"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_A",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "B"         :{ "Location6" : 8,  "Width6" : 110, "Location8" : 8,  "Group" : "B"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_B",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "C"         :{ "Location6" : 9,  "Width6" : 110, "Location8" : 9,  "Group" : "C"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_C",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "D"         :{ "Location6" : 99, "Width6" : 0,   "Location8" : 10, "Group" : "D"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_D",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "E"         :{ "Location6" : 99, "Width6" : 0,   "Location8" : 11, "Group" : "E"        , "Width8" : 91, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_E",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "SPD"       :{ "Location6" : 10, "Width6" : 50,  "Location8" : 12, "Group" :"SPD"       , "Width8" : 36, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Speed",       "DigitFormat" : "MultiFormat"},
    "T"         :{ "Location6" : 11, "Width6" : 18,  "Location8" : 13, "Group" :"T"         , "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_T",           "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T_Delay"   :{ "Location6" : 12, "Width6" : 18,  "Location8" : 14, "Group" :"T_Delay"   , "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "pushButton_EditWin_TDelay", "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "AIR1_0"    :{ "Location6" : 13, "Width6" : 18,  "Location8" : 15, "Group" :"AIR1_0"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Air",         "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_1"    :{ "Location6" : 14, "Width6" : 18,  "Location8" : 16, "Group" :"AIR1_1"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_2"    :{ "Location6" : 15, "Width6" : 18,  "Location8" : 17, "Group" :"AIR1_2"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_3"    :{ "Location6" : 16, "Width6" : 18,  "Location8" : 18, "Group" :"AIR1_3"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_0"    :{ "Location6" : 17, "Width6" : 18,  "Location8" : 19, "Group" :"AIR2_0"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_1"    :{ "Location6" : 18, "Width6" : 18,  "Location8" : 20, "Group" :"AIR2_1"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_2"    :{ "Location6" : 19, "Width6" : 18,  "Location8" : 21, "Group" :"AIR2_2"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_3"    :{ "Location6" : 20, "Width6" : 18,  "Location8" : 22, "Group" :"AIR2_3"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    }

# G2 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable,Axis]
ArrEDIT_TableDataG2= {
    "Row"       :{ "Location6" : 0,  "Width6" : 45,  "Location8" : 0,  "Group" :"Row"       , "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",       "DigitFormat" : "Digs3_Format"},
    "G"         :{ "Location6" : 1,  "Width6" : 20,  "Location8" : 1,  "Group" :"G"         , "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",       "DigitFormat" : "Digs1_Format"},
    "X_StartPos":{ "Location6" : 2,  "Width6" : 60 , "Location8" : 2,  "Group" :"X_StartPos", "Width8" : 56, "Editable" : 1, "AxisNo" : 1,                                             "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue": 99999},
    "X_Arrow"   :{ "Location6" : 3,  "Width6" : 20 , "Location8" : 3,  "Group" :"X"         , "Width8" : 14, "Editable" : 0, "AxisNo" : 1},
    "X_EndPos"  :{ "Location6" : 4,  "Width6" : 60 , "Location8" : 4,  "Group" :"X_EndPos"  , "Width8" : 56, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_X",           "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue": 99999},
    "Y"         :{ "Location6" : 5,  "Width6" : 110, "Location8" : 5,  "Group" :"Y"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Y",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Z"         :{ "Location6" : 6,  "Width6" : 110, "Location8" : 6,  "Group" :"Z"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_Z",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "A"         :{ "Location6" : 7,  "Width6" : 110, "Location8" : 7,  "Group" :"A"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_A",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "B"         :{ "Location6" : 8,  "Width6" : 110, "Location8" : 8,  "Group" :"B"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_B",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "C"         :{ "Location6" : 9,  "Width6" : 110, "Location8" : 9,  "Group" :"C"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_C",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "D"         :{ "Location6" : 99, "Width6" : 0  , "Location8" : 10, "Group" :"D"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_D",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "E"         :{ "Location6" : 99, "Width6" : 0  , "Location8" : 11, "Group" :"E"         , "Width8" : 91, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_E",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "SPD"       :{ "Location6" : 10, "Width6" : 50 , "Location8" : 12, "Group" :"SPD"       , "Width8" : 36, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Speed",       "DigitFormat" : "MultiFormat"},
    "T"         :{ "Location6" : 11, "Width6" : 18 , "Location8" : 13, "Group" :"T"         , "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_T",           "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T_Delay"   :{ "Location6" : 12, "Width6" : 18 , "Location8" : 14, "Group" :"T_Delay"   , "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "pushButton_EditWin_TDelay", "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_0"    :{ "Location6" : 13, "Width6" : 18 , "Location8" : 15, "Group" :"AIR1_0"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Air",         "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_1"    :{ "Location6" : 14, "Width6" : 18 , "Location8" : 16, "Group" :"AIR1_1"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_2"    :{ "Location6" : 15, "Width6" : 18 , "Location8" : 17, "Group" :"AIR1_2"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_3"    :{ "Location6" : 16, "Width6" : 18 , "Location8" : 18, "Group" :"AIR1_3"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_0"    :{ "Location6" : 17, "Width6" : 18 , "Location8" : 19, "Group" :"AIR2_0"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_1"    :{ "Location6" : 18, "Width6" : 18 , "Location8" : 20, "Group" :"AIR2_1"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_2"    :{ "Location6" : 19, "Width6" : 18 , "Location8" : 21, "Group" :"AIR2_2"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_3"    :{ "Location6" : 20, "Width6" : 18 , "Location8" : 22, "Group" :"AIR2_3"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    }   

# G3 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG3= {
    "Row"        :{ "Location6" : 0,  "Width6" : 45, "Location8" : 0,  "Group" : "Row"      , "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",       "DigitFormat" : "Digs3_Format"},
    "G"          :{ "Location6" : 1,  "Width6" : 20, "Location8" : 1,  "Group" : "G"        , "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",       "DigitFormat" : "Digs1_Format"},
    "X_StartPos" :{ "Location6" : 2,  "Width6" : 60, "Location8" : 2,  "Group" : "X_StartPos", "Width8" : 56, "Editable" : 1, "AxisNo" : 1,                                             "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue": 99999},
    "X_Arrow"    :{ "Location6" : 3,  "Width6" : 20, "Location8" : 3,  "Group" : "X"         , "Width8" : 14, "Editable" : 0, "AxisNo" : 1},
    "X_EndPos"   :{ "Location6" : 4,  "Width6" : 60, "Location8" : 4,  "Group" : "X_EndPos"  , "Width8" : 56, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_X",           "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue": 999999},
    "Y"          :{ "Location6" : 6,  "Width6" : 90, "Location8" : 6,  "Group" : "Y"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Y",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Y_seq"      :{ "Location6" : 5,  "Width6" : 20, "Location8" : 5,  "Group" : "Y"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Yseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     1, "MaxValue":      5},
    "Z"          :{ "Location6" : 8,  "Width6" : 90, "Location8" : 8,  "Group" : "Z"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_Z",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Z_seq"      :{ "Location6" : 7,  "Width6" : 20, "Location8" : 7,  "Group" : "Z"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_Zseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "A"          :{ "Location6" : 10, "Width6" : 90, "Location8" : 10, "Group" : "A"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_A",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "A_seq"      :{ "Location6" : 9,  "Width6" : 20, "Location8" : 9,  "Group" : "A"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_Aseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "B"          :{ "Location6" : 12, "Width6" : 90, "Location8" : 12, "Group" : "B"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_B",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "B_seq"      :{ "Location6" : 11, "Width6" : 20, "Location8" : 11, "Group" : "B"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_Bseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "C"          :{ "Location6" : 14, "Width6" : 90, "Location8" : 14, "Group" : "C"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_C",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "C_seq"      :{ "Location6" : 13, "Width6" : 20, "Location8" : 13, "Group" : "C"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_Cseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "D"          :{ "Location6" : 99, "Width6" : 0,  "Location8" : 16, "Group" : "D"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_D",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "D_seq"      :{ "Location6" : 99, "Width6" : 0,  "Location8" : 15, "Group" : "D"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_Dseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "E"          :{ "Location6" : 99, "Width6" : 0,  "Location8" : 18, "Group" : "E"        , "Width8" : 77, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_E",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "E_seq"      :{ "Location6" : 99, "Width6" : 0,  "Location8" : 17, "Group" : "E"        , "Width8" : 14, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_Eseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "SPD"        :{ "Location6" : 15, "Width6" : 50, "Location8" : 19, "Group" :"SPD"       , "Width8" : 36, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Speed",       "DigitFormat" : "MultiFormat"},
    "T"          :{ "Location6" : 16, "Width6" : 18, "Location8" : 20, "Group" :"T"         , "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_T",           "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "T_Delay"    :{ "Location6" : 17, "Width6" : 18, "Location8" : 21, "Group" :"T_Delay"   , "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "pushButton_EditWin_TDelay", "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR1_0"     :{ "Location6" : 18, "Width6" : 18, "Location8" : 22, "Group" :"AIR1_0"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Air",         "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR1_1"     :{ "Location6" : 19, "Width6" : 18, "Location8" : 23, "Group" :"AIR1_1"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR1_2"     :{ "Location6" : 20, "Width6" : 18, "Location8" : 24, "Group" :"AIR1_2"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR1_3"     :{ "Location6" : 21, "Width6" : 18, "Location8" : 25, "Group" :"AIR1_3"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR2_0"     :{ "Location6" : 22, "Width6" : 18, "Location8" : 26, "Group" :"AIR2_0"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR2_1"     :{ "Location6" : 23, "Width6" : 18, "Location8" : 27, "Group" :"AIR2_1"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR2_2"     :{ "Location6" : 24, "Width6" : 18, "Location8" : 28, "Group" :"AIR2_2"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    "AIR2_3"     :{ "Location6" : 25, "Width6" : 18, "Location8" : 29, "Group" :"AIR2_3"    , "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":       1},
    }

# G4 Mode SubTabl6
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG4= {
    "Row"        :{ "Location6" : 0,  "Width6" : 45, "Location8" : 0,  "Group" : "Row",     "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",       "DigitFormat" : "Digs3_Format"},
    "G"          :{ "Location6" : 1,  "Width6" : 20, "Location8" : 1,  "Group" : "G",       "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",       "DigitFormat" : "Digs1_Format"},
    "X_StartPos" :{ "Location6" : 2,  "Width6" : 60, "Location8" : 2,  "Group" : "X_StartPos","Width8" : 56, "Editable" : 1, "AxisNo" : 1,                                             "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue":  99999},
    "X_Arrow"    :{ "Location6" : 3,  "Width6" : 20, "Location8" : 3,  "Group" : "X"         ,"Width8" : 14, "Editable" : 0, "AxisNo" : 1},
    "X_EndPos"   :{ "Location6" : 4,  "Width6" : 60, "Location8" : 4,  "Group" : "X_EndPos"  ,"Width8" : 56, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_X",           "DigitFormat" : "Digs5_Format"    , "MinValue":     0, "MaxValue":  99999},
    "Y"          :{ "Location6" : 6,  "Width6" : 90, "Location8" : 6,  "Group" : "Y",       "Width8" : 77, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Y",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Y_seq"      :{ "Location6" : 5,  "Width6" : 20, "Location8" : 5,  "Group" : "Y",       "Width8" : 14, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Yseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "Z"          :{ "Location6" : 8,  "Width6" : 90, "Location8" : 8,  "Group" : "Z",       "Width8" : 77, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_Z",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "Z_seq"      :{ "Location6" : 7,  "Width6" : 20, "Location8" : 7,  "Group" : "Z",       "Width8" : 14, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_Zseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "A"          :{ "Location6" : 10, "Width6" : 90, "Location8" : 10, "Group" : "A",       "Width8" : 77, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_A",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "A_seq"      :{ "Location6" : 9,  "Width6" : 20, "Location8" : 9,  "Group" : "A",       "Width8" : 14, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_Aseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "B"          :{ "Location6" : 12, "Width6" : 90, "Location8" : 12, "Group" : "B",       "Width8" : 77, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_B",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "B_seq"      :{ "Location6" : 11, "Width6" : 20, "Location8" : 11, "Group" : "B",       "Width8" : 14, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_Bseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "C"          :{ "Location6" : 14, "Width6" : 90, "Location8" : 14, "Group" : "C",       "Width8" : 77, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_C",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "C_seq"      :{ "Location6" : 13, "Width6" : 20, "Location8" : 13, "Group" : "C",       "Width8" : 14, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_Cseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "D"          :{ "Location6" : 99, "Width6" : 0,  "Location8" : 16, "Group" : "D",       "Width8" : 77, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_D",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "D_seq"      :{ "Location6" : 99, "Width6" : 0,  "Location8" : 15, "Group" : "D",       "Width8" : 14, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_Dseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "E"          :{ "Location6" : 99, "Width6" : 0,  "Location8" : 18, "Group" : "E",       "Width8" : 77, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_E",           "DigitFormat" : "AxisFormat"      , "MinValue":     0, "MaxValue": 999999},
    "E_seq"      :{ "Location6" : 99, "Width6" : 0,  "Location8" : 17, "Group" : "E",       "Width8" : 14, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_Eseq",        "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      5},
    "SPD"        :{ "Location6" : 15, "Width6" : 50, "Location8" : 19, "Group" : "SPD",     "Width8" : 36, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Speed",       "DigitFormat" : "MultiFormat"     , "MinValue":     0, "MaxValue":     99},
    "T"          :{ "Location6" : 16, "Width6" : 18, "Location8" : 20, "Group" : "T",       "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_T",           "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "T_Delay"    :{ "Location6" : 17, "Width6" : 18, "Location8" : 21, "Group" : "T_Delay", "Width8" : 13, "Editable" : 2, "AxisNo" : 0, "EditWinObj" : "pushButton_EditWin_TDelay", "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_0"     :{ "Location6" : 18, "Width6" : 18, "Location8" : 22, "Group" : "AIR1_0",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Air",         "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_1"     :{ "Location6" : 19, "Width6" : 18, "Location8" : 23, "Group" : "AIR1_1",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_2"     :{ "Location6" : 20, "Width6" : 18, "Location8" : 24, "Group" : "AIR1_2",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR1_3"     :{ "Location6" : 21, "Width6" : 18, "Location8" : 25, "Group" : "AIR1_3",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_0"     :{ "Location6" : 22, "Width6" : 18, "Location8" : 26, "Group" : "AIR2_0",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_1"     :{ "Location6" : 23, "Width6" : 18, "Location8" : 27, "Group" : "AIR2_1",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_2"     :{ "Location6" : 24, "Width6" : 18, "Location8" : 28, "Group" : "AIR2_2",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    "AIR2_3"     :{ "Location6" : 25, "Width6" : 18, "Location8" : 29, "Group" : "AIR2_3",  "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                             "DigitFormat" : "Digs1_Format"    , "MinValue":     0, "MaxValue":      1},
    }

# G5 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG5= {
    "Row"           :{ "Location6" : 0, "Width6" : 45, "Location8" : 0, "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",      "DigitFormat" : "Digs3_Format"},
    "G"             :{ "Location6" : 1, "Width6" : 20, "Location8" : 1, "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",      "DigitFormat" : "Digs1_Format"},
    "X1_N"          :{ "Location6" : 2, "Width6" : 20, "Location8" : 2, "Width8" : 17, "Editable" : 0, "AxisNo" : 1},
    "StartRow"      :{ "Location6" : 3, "Width6" : 40, "Location8" : 3, "Width8" : 39, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_Repeat",     "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999},
    "X_Arrow"       :{ "Location6" : 4, "Width6" : 20, "Location8" : 4, "Width8" : 14, "Editable" : 0, "AxisNo" : 1},
    "X2_N"          :{ "Location6" : 5, "Width6" : 20, "Location8" : 5, "Width8" : 17, "Editable" : 0, "AxisNo" : 1},
    "EndRow"        :{ "Location6" : 6, "Width6" : 40, "Location8" : 6, "Width8" : 39, "Editable" : 1, "AxisNo" : 1,                                            "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999},
    "Y_X"           :{ "Location6" : 7, "Width6" : 20, "Location8" : 7, "Width8" : 17, "Editable" : 0, "AxisNo" : 2},
    "RepeatTurn"    :{ "Location6" : 8, "Width6" : 90, "Location8" : 8, "Width8" : 74, "Editable" : 1, "AxisNo" : 2,                                            "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999}
    }

# G6 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG6= {
    "Row"        :{ "Location6" : 0,  "Width6" : 45,  "Location8" : 0,  "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",      "DigitFormat" : "Digs3_Format"},
    "G"          :{ "Location6" : 1,  "Width6" : 20,  "Location8" : 1,  "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",      "DigitFormat" : "Digs1_Format"},
    "X_StartPos" :{ "Location6" : 2,  "Width6" : 60,  "Location8" : 2,  "Width8" : 56, "Editable" : 1, "AxisNo" : 1,                                            "DigitFormat" : "Digs5_Format"      , "MinValue":     0, "MaxValue": 99999},
    "X_Arrow"    :{ "Location6" : 3,  "Width6" : 20,  "Location8" : 3,  "Width8" : 14, "Editable" : 0, "AxisNo" : 1},
    "X_EndPos"   :{ "Location6" : 4,  "Width6" : 60,  "Location8" : 4,  "Width8" : 56, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_X",          "DigitFormat" : "Digs5_Format"      , "MinValue":     0, "MaxValue": 99999},
    "Y"          :{ "Location6" : 5,  "Width6" : 110, "Location8" : 5,  "Width8" : 91, "Editable" : 1, "AxisNo" : 2, "EditWinObj" : "Lebel_EditWin_Y",          "DigitFormat" : "Digs6_PN_Format"   , "MinValue":     0, "MaxValue": 999999},
    "Z_G6"       :{ "Location6" : 6,  "Width6" : 20,  "Location8" : 6,  "Width8" : 14, "Editable" : 1, "AxisNo" : 3, "EditWinObj" : "Lebel_EditWin_ZG6",        "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "Z_ZERO"     :{ "Location6" : 7,  "Width6" : 90,  "Location8" : 7,  "Width8" : 77, "Editable" : 0, "AxisNo" : 3},
    "A_G6"       :{ "Location6" : 8,  "Width6" : 20,  "Location8" : 8,  "Width8" : 14, "Editable" : 1, "AxisNo" : 4, "EditWinObj" : "Lebel_EditWin_AG6",        "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "A_ZERO"     :{ "Location6" : 9,  "Width6" : 90,  "Location8" : 9,  "Width8" : 77, "Editable" : 0, "AxisNo" : 4},
    "B_G6"       :{ "Location6" : 10, "Width6" : 20,  "Location8" : 10, "Width8" : 14, "Editable" : 1, "AxisNo" : 5, "EditWinObj" : "Lebel_EditWin_BG6",        "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "B_ZERO"     :{ "Location6" : 11, "Width6" : 90,  "Location8" : 11, "Width8" : 77, "Editable" : 0, "AxisNo" : 5},
    "C_G6"       :{ "Location6" : 12, "Width6" : 20,  "Location8" : 12, "Width8" : 14, "Editable" : 1, "AxisNo" : 6, "EditWinObj" : "Lebel_EditWin_CG6",        "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "C_ZERO"     :{ "Location6" : 13, "Width6" : 90,  "Location8" : 13, "Width8" : 77, "Editable" : 0, "AxisNo" : 6},
    "D_G6"       :{ "Location6" : 99, "Width6" : 0,   "Location8" : 14, "Width8" : 14, "Editable" : 1, "AxisNo" : 7, "EditWinObj" : "Lebel_EditWin_DG6",        "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "D_ZERO"     :{ "Location6" : 99, "Width6" : 0,   "Location8" : 15, "Width8" : 77, "Editable" : 0, "AxisNo" : 7},
    "E_G6"       :{ "Location6" : 99, "Width6" : 0,   "Location8" : 16, "Width8" : 14, "Editable" : 1, "AxisNo" : 8, "EditWinObj" : "Lebel_EditWin_EG6",        "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "E_ZERO"     :{ "Location6" : 99, "Width6" : 0,   "Location8" : 17, "Width8" : 77, "Editable" : 0, "AxisNo" : 8},
    "SPD"        :{ "Location6" : 14, "Width6" : 86,  "Location8" : 18, "Width8" : 62, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Speed",      "DigitFormat" : "MultiFormat"       , "DefautlValue": "S"},
    "AIR1_0"     :{ "Location6" : 15, "Width6" : 18,  "Location8" : 19, "Width8" : 13, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_Air",        "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR1_1"     :{ "Location6" : 16, "Width6" : 18,  "Location8" : 20, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR1_2"     :{ "Location6" : 17, "Width6" : 18,  "Location8" : 21, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR1_3"     :{ "Location6" : 18, "Width6" : 18,  "Location8" : 22, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR2_0"     :{ "Location6" : 19, "Width6" : 18,  "Location8" : 23, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR2_1"     :{ "Location6" : 20, "Width6" : 18,  "Location8" : 24, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR2_2"     :{ "Location6" : 21, "Width6" : 18,  "Location8" : 25, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    "AIR2_3"     :{ "Location6" : 22, "Width6" : 18,  "Location8" : 26, "Width8" : 13, "Editable" : 1, "AxisNo" : 0,                                            "DigitFormat" : "Digs1_Format"      , "MinValue":     0, "MaxValue":      1},
    }

# G7 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG7= {
    "Row"       :{ "Location6" : 0, "Width6" : 45,  "Location8" : 0, "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo", "DigitFormat" : "Digs3_Format"},
    "G"         :{ "Location6" : 1, "Width6" : 20,  "Location8" : 1, "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode", "DigitFormat" : "Digs1_Format"},
    "X_Delay"   :{ "Location6" : 2, "Width6" : 110, "Location8" : 2, "Width8" : 95, "Editable" : 0, "AxisNo" : 1},
    "X_G7"      :{ "Location6" : 3, "Width6" : 80,  "Location8" : 3, "Width8" : 77, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_Delay", "DigitFormat" : "Digs6_Format", "MinValue":     0, "MaxValue":   999999},
    "X_ms"      :{ "Location6" : 4, "Width6" : 60,  "Location8" : 4, "Width8" : 45, "Editable" : 0, "AxisNo" : 1}
    }
# G8 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG8= {
    "Row"       :{ "Location6" : 0, "Width6" : 45, "Location8" : 0, "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",          "DigitFormat" : "Digs3_Format"},
    "G"         :{ "Location6" : 1, "Width6" : 20, "Location8" : 1, "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",          "DigitFormat" : "Digs1_Format"},
    "X1_N"      :{ "Location6" : 2, "Width6" : 20, "Location8" : 2, "Width8" : 20, "Editable" : 0, "AxisNo" : 1},
    "StartRow"  :{ "Location6" : 3, "Width6" : 40, "Location8" : 3, "Width8" : 35, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_RackSpeedUp",    "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999},
    "X_Arrow"   :{ "Location6" : 4, "Width6" : 20, "Location8" : 4, "Width8" : 15, "Editable" : 0, "AxisNo" : 1},
    "X2_N"      :{ "Location6" : 5, "Width6" : 20, "Location8" : 5, "Width8" : 20, "Editable" : 0, "AxisNo" : 1},
    "EndRow"    :{ "Location6" : 6, "Width6" : 40, "Location8" : 6, "Width8" : 35, "Editable" : 1, "AxisNo" : 1,                                                "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999},
    }

# G5 Mode SubTable
# [ Col Location, ColWidth, Col Name, Col Editable]
ArrEDIT_TableDataG9= {
    "Row"       :{ "Location6" : 0, "Width6" : 45,  "Location8" : 0, "Width8" : 40, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_RowNo",         "DigitFormat" : "Digs3_Format"},
    "G"         :{ "Location6" : 1, "Width6" : 20,  "Location8" : 1, "Width8" : 18, "Editable" : 1, "AxisNo" : 0, "EditWinObj" : "Lebel_EditWin_GCode",         "DigitFormat" : "Digs1_Format"},
    "X1_N"      :{ "Location6" : 2, "Width6" : 20,  "Location8" : 2, "Width8" : 15, "Editable" : 0, "AxisNo" : 1},
    "X1_G9"     :{ "Location6" : 3, "Width6" : 40,  "Location8" : 3, "Width8" : 40, "Editable" : 1, "AxisNo" : 1, "EditWinObj" : "Lebel_EditWin_FIncrements",   "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999},
    "X_Arrow"   :{ "Location6" : 4, "Width6" : 20,  "Location8" : 4, "Width8" : 15, "Editable" : 0, "AxisNo" : 1},
    "X2_N"      :{ "Location6" : 5, "Width6" : 20,  "Location8" : 5, "Width8" : 15, "Editable" : 0, "AxisNo" : 1},
    "X2_G9"     :{ "Location6" : 6, "Width6" : 40,  "Location8" : 6, "Width8" : 41, "Editable" : 1, "AxisNo" : 1,                                               "DigitFormat" : "Digs3_Format", "MinValue":     0, "MaxValue":   999},
    "Y_Add"     :{ "Location6" : 7, "Width6" : 110, "Location8" : 7, "Width8" : 91, "Editable" : 0, "AxisNo" : 2},
    "Y_G9"      :{ "Location6" : 8, "Width6" : 110, "Location8" : 8, "Width8" : 91, "Editable" : 1, "AxisNo" : 2,                                               "DigitFormat" : "Digs4Dot2_PN_Format", "MinValue":     0, "MaxValue":   999999}
    }


# --------------------------------------------------------
#               Set Cylindar Table Size
# --------------------------------------------------------
# [ Col Location, ColWidth, Col Editable]
#                           0: Non-Editable/ 1: Editable
ArrEDIT_TableCylidar = {
    "AIR_START_X":{ "Location6" : 0,  "Width6" : 60, "Location8" : 0,  "Width8" : 60, "Editable" : 1, "DigitFormat" : "Digs5_Format"},
    "X_Arrow"   :{ "Location6" : 1,  "Width6" : 20, "Location8" : 1,  "Width8" : 20, "Editable" : 0},
    "AIR_END_X" :{ "Location6" : 2,  "Width6" : 60, "Location8" : 2,  "Width8" : 60, "Editable" : 1, "DigitFormat" : "Digs5_Format"},
    "T"         :{ "Location6" : 3,  "Width6" : 18, "Location8" : 3,  "Width8" : 18, "Editable" : 0, "DigitFormat" : "Digs1_Format"},
    "T_Delay"   :{ "Location6" : 4,  "Width6" : 18, "Location8" : 4,  "Width8" : 18, "Editable" : 0, "DigitFormat" : "Digs1_Format"},
    "AIR1_0"    :{ "Location6" : 5,  "Width6" : 18, "Location8" : 5,  "Width8" : 18, "Editable" : 1, "DigitFormat" : "Digs1_Format"},
    "AIR1_1"    :{ "Location6" : 6,  "Width6" : 18, "Location8" : 6,  "Width8" : 18, "Editable" : 1, "DigitFormat" : "Digs1_Format"},
    "AIR1_2"    :{ "Location6" : 7,  "Width6" : 18, "Location8" : 7,  "Width8" : 18, "Editable" : 1, "DigitFormat" : "Digs1_Format"},
    "AIR1_3"    :{ "Location6" : 8,  "Width6" : 18, "Location8" : 8,  "Width8" : 18, "Editable" : 1, "DigitFormat" : "Digs1_Format"},
    "AIR2_0"    :{ "Location6" : 9,  "Width6" : 18, "Location8" : 9,  "Width8" : 18, "Editable" : 1},
    "AIR2_1"    :{ "Location6" : 10, "Width6" : 18, "Location8" : 10, "Width8" : 18, "Editable" : 1},
    "AIR2_2"    :{ "Location6" : 11, "Width6" : 18, "Location8" : 11, "Width8" : 18, "Editable" : 1},
    "AIR2_3"    :{ "Location6" : 12, "Width6" : 18, "Location8" : 12, "Width8" : 18, "Editable" : 1}
    }

# --------------------------------------------------------
# Set Table Title of Header , Size of Header and Main Table
# --------------------------------------------------------
ArrEDIT_MainHeader = {
    "N"         :{ "Location6" : 0,  "Width6" : 45,  "Location8" : 0,  "Width8" : 40 },
    "G"         :{ "Location6" : 1,  "Width6" : 20,  "Location8" : 1,  "Width8" : 16 },
    "X"         :{ "Location6" : 2,  "Width6" : 140, "Location8" : 2,  "Width8" : 126, "AxisNo" : 0, "BeforeText" : "X-"},
    "Y"         :{ "Location6" : 3,  "Width6" : 110, "Location8" : 3,  "Width8" : 91 , "AxisNo" : 1, "BeforeText" : "Y-"},
    "Z"         :{ "Location6" : 4,  "Width6" : 110, "Location8" : 4,  "Width8" : 91 , "AxisNo" : 2, "BeforeText" : "Z-"},
    "A"         :{ "Location6" : 5,  "Width6" : 110, "Location8" : 5,  "Width8" : 91 , "AxisNo" : 3, "BeforeText" : "A-"},
    "B"         :{ "Location6" : 6,  "Width6" : 110, "Location8" : 6,  "Width8" : 91 , "AxisNo" : 4, "BeforeText" : "B-"},
    "C"         :{ "Location6" : 7,  "Width6" : 110, "Location8" : 7,  "Width8" : 91 , "AxisNo" : 5, "BeforeText" : "C-"},
    "D"         :{ "Location6" : 8,  "Width6" : 0,   "Location8" : 8,  "Width8" : 91 , "AxisNo" : 6, "BeforeText" : "D-"},
    "E"         :{ "Location6" : 8,  "Width6" : 0,   "Location8" : 9,  "Width8" : 91 , "AxisNo" : 7, "BeforeText" : "E-"},
    "SPD"       :{ "Location6" : 8,  "Width6" : 50,  "Location8" : 10, "Width8" : 36 },
    "T"         :{ "Location6" : 9,  "Width6" : 36,  "Location8" : 11, "Width8" : 26 },
    "AIR"       :{ "Location6" : 10, "Width6" : 146, "Location8" : 12, "Width8" : 106}
    }

# Set Table Title of Header , Size of Header and Main Table
ArrEDIT_HeaderCylidar = {
    "X"         :{ "Location6" : 0, "Width6" : 140 , "Location8" : 0, "Width8" : 140},
    "T"         :{ "Location6" : 1, "Width6" : 36  , "Location8" : 1, "Width8" : 36 },
    "AIR"       :{ "Location6" : 2, "Width6" : 146 , "Location8" : 2, "Width8" : 146}
    }
ArrFILE_USBRead = {
    0  :{ "Display" : "USB -> 機台目前調機程式", "ExecObj" : "ReadCurrFile" },
    1  :{ "Display" : "USB -> 機台全部調機程式", "ExecObj" : "ReadAllFiles" },
    2  :{ "Display" : "USB -> 機台參數設定程式", "ExecObj" : "ReadParamter" },
    3  :{ "Display" : "USB -> 機台系統版本檔案", "ExecObj" : None           },
}
ArrFILE_USBSave = {
    0  :{ "Display" : "機台目前調機程式 -> USB", "ExecObj" : "SaveCurrFile" },
    1  :{ "Display" : "機台全部調機程式 -> USB", "ExecObj" : "SaveAllFiles" },
    2  :{ "Display" : "機台參數設定程式 -> USB", "ExecObj" : "SaveParamter" },
    3  :{ "Display" : "機台系統版本檔案 -> USB", "ExecObj" : None           },
}