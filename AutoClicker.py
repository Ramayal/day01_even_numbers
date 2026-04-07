import pyautogui
import keyboard
import time

i = True

PositionX = 3097
PositionY = 426  

print("Presiona Q si quieres detener el programa")

while i:
    pyautogui.leftClick(PositionX,PositionY)    
    
    if(keyboard.is_pressed("q")):
        print("Programa Detenido con Exito")
        break
    
    elif(keyboard.is_pressed("s")):
        PositionX1, PositionX2 = pyautogui.position()
        print("Posición guardada:", PositionX, PositionY)
    time.sleep(0.1)
