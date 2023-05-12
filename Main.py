# Main of the Sandbox city generator
import pandas as pd
from tkinter import *
from tkinter import ttk
import os
import sys
import Classes
import string
import ctypes

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

workshops = ["Farmy", "Łowcy", "Gotowanie", "Architekci", "Kowale", "Metalurgia", "Cieśla", "Alchemik", "Tkacz", "Kamieniarz", "Drwal", "Zbieracz"]
resources = ["People", "Food", "Buildings", "Tools", "Tools_materials", "Other", "Safety", "Fun", "Stone","Wood", "Herbs", "Transport"]

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

def Get_city(number):
    df = pd.read_excel("Cities.xlsx")
    # Extract the relevant columns
    df = df.loc[number]
    return df

def Start(City):
    window = Tk()
    frm = ttk.Frame(window, padding=10) #Creating the GUI frame
    frm.grid()

    Label(frm, text="CO\lvl").grid(column=0, row=0)

    # Define X and Y Axis Lists
    xAxis = range(1, 6)
    yAxis = range(0, 12)

    cells = {}
    labels = {}
    for i, y in enumerate(workshops):
        label = Label(frm, text = y, width=10, anchor="w").grid(row=i + 1, column=0)
    for i, x in enumerate(xAxis):
        label = Label(frm, text = x, width=5, anchor="n").grid(row=0, column=i + 1)
    
    for i, workshop in enumerate(workshops):
        for xcoor, x in enumerate(xAxis):
            # Generate a Unique ID for the cells
            id = f'{workshop}_{x}'
            var = StringVar(frm, City.df[id], id)
            # Make Entry and label, offset each axis by one because of the lables
            e = Entry(frm, textvariable=var, width=5)
            e.grid(row=i + 1, column=xcoor + 1)
            
            cells[id] = var
    
    for i, res in enumerate(resources):
        id = f'{res}'
        var = StringVar(frm, f"{res} = ", id)
        Label(frm, textvariable=var, anchor="w").grid(column=0+(i % 2)*3, row=13+(i//2),columnspan=3)
        labels[id] = var

    var = StringVar(frm, "Suma = ", "suma")
    Label(frm, textvariable=var).grid(column=0, row=20,columnspan=6)
    labels["suma"] = var

    def Load_from_file():
        for cell in cells:
            cells[cell].set(City.df[cell])
        
    def Push_to_city():
        Suma = 0
        for cell in cells:
            City.entities[cell] = int(cells[cell].get())

        City.Get_resources()
        for i, res in enumerate(resources):
            text = f'{res} = {getattr(City, res)}'
            labels[res].set(text)
            Suma += getattr(City, res)**2
        labels["suma"].set(f"Suma = {Suma}")

    Button(frm, text="Load", command=Load_from_file).grid(column=6, row=0)
    Button(frm, text="Push", command=Push_to_city).grid(column=6, row=1)

    for i, (name, value) in enumerate(City.df['kobiety pracujące (inne)':'uprawa ziela 4 poz'].items()):
        print(name, value)
        Label(frm, text=name, width=40, anchor="w").grid(column=8, row=i)
        id = name
        var = StringVar(frm, value, id)
        e = Entry(frm, textvariable=var, width=5)
        e.grid(column=9, row=i)
        cells[id] = var

    window.mainloop()

if __name__ == "__main__":

    City = Classes.city(number = 3)
    City.df = Get_city(number = City.number)
    City.Get_entities_dict()

    Start(City)
    


