# Main of the Sandbox city generator
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import sys
import Classes
import string
import ctypes
import math
import copy
import Town

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

def Get_city(number):
    df = pd.read_excel("Cities.xlsx")
    # Extract the relevant columns
    df = df.loc[number]
    return df

def Start(City):
    Window = Tk()
    Window.title("Second Window")
    frm = ttk.Frame(Window, padding=10) #Creating the GUI frame
    frm.grid()
    Window.title("Test window")

    def Start_town():
        Town.Town(City)

    def Exit():
        Window.destroy()


    Label(frm, text = "Hello user", anchor="w").grid(column=1, row=0)
    Button(frm, text="Start new town", command=Start_town).grid(column=1, row=1)
    Button(frm, text="Exit", command=Exit).grid(column=2, row=1)

    Window.mainloop()

if __name__ == "__main__":

    City = Classes.city(number = 0)
    City.df = Get_city(number = City.number)
    City.Get_entities_dict()

    Start(City)


    
    


