@echo off
echo --------------------------------------------
echo FINALIZANDO PROGRAMA DE MANTER O NOTE LIGADO
echo --------------------------------------------
Get-Process -Name "WindowsTerminal" | Stop-Process -Force
Get-Process -Name "powershell" | Stop-Process -Force
