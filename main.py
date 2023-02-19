
from tkinter import *
import os

from lib.library import *
from tkinter import filedialog

fenetre=Tk()
fenetre.withdraw()
zoneText=Text(fenetre)
root=editeurText(fenetre,zoneText)
root.creaFenetre()
root.creaZoneText()
root.creaMenu()
root.genererFen()