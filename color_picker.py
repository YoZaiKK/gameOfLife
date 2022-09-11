from tkinter import *
import tkinter.ttk as ttk
from tkcolorpicker import askcolor  

def pick_color(root): 
   
  rgb, root = askcolor((255, 255, 0), root)
  return rgb
   

# if rgb:
#   quit() 