@echo off
goto :choice

:choice
choice /M "Run file?":
IF ERRORLEVEL 1 goto run
IF ERRORLEVEL 2 exit



:run
python mumien.py < input.txt
goto :choice