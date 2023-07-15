import time
import keyboard

#
# ESTE SCRIPT MANTÉM A TECLA "A" PRESSIONADA A CADA 3 SEGUNDOS
#

while True:
    time.sleep(3)
    keyboard.press("a")
    keyboard.release("a")