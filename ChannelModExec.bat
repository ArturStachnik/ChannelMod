@echo off
REM Define la ruta al ejecutable de Python
set "pythonPath=python"

REM Define la ruta al script de Python
set "pythonScript=ChannelMod.py"

REM Ejecuta el script de Python
"%pythonPath%" "%pythonScript%"

REM Mantén la ventana de cmd abierta al finalizar la ejecución
pause