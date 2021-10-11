import json
from datetime import datetime as dt
import subprocess
import time
import pyautogui as gui
import link
import os

os.system("TASKKILL /F /IM zoom.exe")
time.sleep(5)

def openZoom():
    subprocess.Popen(r"C:\Users\UserName\AppData\Roaming\Zoom\bin\Zoom.exe")
    time.sleep(10)
    buttonClick()

def buttonClick():
    gui.click(672, 315)     #default small screen
    time.sleep(3)

def buttonWrite(text):
    gui.write(text)
    time.sleep(1)
    gui.press('enter')  

def joinClass():
    print("Yay")
    try:
        print("Yay")
        idm = link.ID
        pasm = link.PASS
        #idm = "1234567890"
        #pasm = "123456"
        print("Yay")
        openZoom()
        print("Here")
        buttonWrite(idm)
        time.sleep(6)
        buttonWrite(pasm)
        time.sleep(2)
    except:
        print("Nay")
        check = False
        

joinClass()


#Replace UserName with yours
#you will have to replace coordinates in line 18 with your own
#http://www.brenz.net/snippets/xy.asp - get your cursor's coordinates here
#go full screen, open zoom and check the coordinates of the join button