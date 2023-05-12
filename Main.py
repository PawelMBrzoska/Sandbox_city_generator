# Main of the Sandbox city generator
import pandas as pd
from tkinter import *
from tkinter import ttk
import os
import sys
import Classes
import string
import ctypes
import math
import copy

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

workshops = ["Farmy", "Łowcy", "Gotowanie", "Architekci", "Kowale", "Metalurgia", "Cieśla", "Alchemik", "Tkacz", "Kamieniarz", "Drwal", "Zbieracz"]
resources = ["People", "Food", "Buildings", "Tools", "Materials", "Other", "Safety", "Fun", "Wood","Stone", "Herbs", "Transport"]

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

    #Label(frm, text="CO\lvl").grid(column=0, row=0)

    # Define X and Y Axis Lists
    xAxis = range(1, 6)
    yAxis = range(0, 12)
    City.cells = {}
    City.labels = {}

    ###########################################
    #            Workshops labels             #
    ###########################################
     
    for i, y in enumerate(workshops):
        label = Label(frm, text = y, width=12, anchor="w").grid(row=i + 1, column=0)
    for i, x in enumerate(xAxis):
        label = Label(frm, text = x, width=6, anchor="n").grid(row=0, column=i + 1)
    
    ###########################################
    #             Workshops Cells             #
    ###########################################

    for i, workshop in enumerate(workshops):
        for xcoor, x in enumerate(xAxis):
            # Generate a Unique ID for the cells
            id = f'{workshop}_{x}'
            var = StringVar(frm, City.df[id], id)
            # Make Entry and label, offset each axis by one because of the lables
            e = Entry(frm, textvariable=var, width=6)
            e.grid(row=i + 1, column=xcoor + 1)
            
            City.cells[id] = var
    
    ###########################################
    #              Resources sums             #
    ###########################################

    for i, res in enumerate(resources):
        id = f'{res}'
        var = StringVar(frm, "", id)
        Label(frm, text=f"{res} = ", width=12, anchor="w").grid(column=0, row=13+i)
        Label(frm, textvariable=var, width=6, anchor="e").grid(column=1, row=13+i)
        City.labels[id] = var

    var = StringVar(frm, "", "suma")
    Label(frm, text = "Suma = ", width=12, anchor="w").grid(column=0, row=25)
    Label(frm, textvariable=var, width=6, anchor="e").grid(column=1, row=25)
    City.labels["suma"] = var

    ###########################################
    #                 Exports                 #
    ###########################################

    Label(frm, text="Export", width=12, anchor="n").grid(column=2, row=13,columnspan=4)
    for i, (name, value) in enumerate(City.df.filter(like = 'Export').items()):
        Label(frm, text=name[7:], width=12, anchor="w").grid(column=2, row=i+14,columnspan=2)
        id = name
        var = StringVar(frm, value, id)
        e = Entry(frm, textvariable=var, width=12)
        e.grid(column=4, row=i+14, columnspan=2)
        City.cells[id] = var

    ###########################################
    #             Additional cells            #
    ###########################################

    for i, (name, value) in enumerate(City.df['kobiety pracujące (inne)':'uprawa ziela 4 poz'].items()):
        Label(frm, text=name, width=30, anchor="w").grid(column=8, row=i)
        id = name
        var = StringVar(frm, value, id)
        e = Entry(frm, textvariable=var, width=5)
        e.grid(column=9, row=i)
        City.cells[id] = var

    ###########################################
    #                Functions                #
    ###########################################

    def Load_from_file():
        for cell in City.cells:
            City.cells[cell].set(City.df[cell])
    
    def Push_to_city():
        City.Suma = 0
        Suma = 0
        for cell in City.cells:
            City.entities[cell] = int(City.cells[cell].get())

        City.Get_resources()
        for i, res in enumerate(resources):
            text = getattr(City, res)
            City.labels[res].set(text)
            City.Suma += getattr(City, res)**2
        City.Suma -= getattr(City, "People")**2
        Suma = City.Suma/City.People # This is basically a optimization function. As city size inflated margin of error, we get an error per person
        Suma = round(math.log10(Suma),3) # And as it is HUGE often we get log10 to comprehend this number ;D
        City.labels["suma"].set(Suma)

    def Optimize_up():
        value = int(City.cells[City.Update_resources_up()].get())
        value+=1
        City.cells[City.Update_resources_up()].set(value)
        Push_to_city()

    Button(frm, text="Load", command=Load_from_file).grid(column=6, row=0)
    Button(frm, text="Push", command=Push_to_city).grid(column=6, row=1)
    Button(frm, text="Opt_up", command=Optimize_up).grid(column=6, row=2)

    window.mainloop()

if __name__ == "__main__":

    City = Classes.city(number = 0)
    City.df = Get_city(number = City.number)
    City.Get_entities_dict()

    Start(City)
    


