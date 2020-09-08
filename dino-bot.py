from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replaybtn=(480,356)   #change the cordinates according to your screen
    dinasaur=(258,375)    #change the cordinates according to your screen

def restartgame():
    pyautogui.click(Cordinates.replaybtn)


def pressspace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def imagegrab():
    box = (Cordinates.dinasaur[0]+80,Cordinates.dinasaur[1],Cordinates.dinasaur[0]+120,Cordinates.dinasaur[1]+30)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    print(a.sum())
    return(a.sum())


def main():
    restartgame()
    while True:
        if(imagegrab()!=1455):    #this value would be different for your cordinates(hint: run the code, the value which is printed repetadlly is the one)
            pressspace()


main()
