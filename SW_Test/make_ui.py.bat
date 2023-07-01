@echo off
set nowYear=%date:~0,4%
set nowMonth=%date:~5,2%
set nowDay=%date:~8,2%
set nowHr=%time:~0,2%
rem 若時小於10，前面補0 例: 9→09, 8→08  
if %nowHr% LSS 10 set nowHr=0%nowHr%
set nowMin=%time:~3,2%
set nowSec=%time:~6,2%

SET curTime=%nowYear%%nowMonth%%nowDay%%nowHr%%nowMin%%nowSec%
IF NOT EXIST uibk mkdir uibk
echo copy "MainForm.ui" to "uibk\MainForm.ui.bk_%curTime%"
copy /Y MainForm.ui uibk\MainForm.ui.bk_%curTime%
echo delete "Ui_MainForm.py"
del /F/Q Ui_MainForm.py
echo gen Ui_MainForm.py
pyuic5 -o Ui_MainForm.py -x MainForm.ui
echo copy "VertualKeyBoard.ui" to "uibk\VertualKeyBoard.ui.bk_%curTime%"
echo copy /Y VertualKeyBoard.ui uibk\VertualKeyBoard.ui.bk_%curTime%
echo done.
pause