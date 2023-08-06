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
import Classes


def Domain(New_domain):
    window = Tk()
    frm = ttk.Frame(window, padding=10) #Creating the GUI frame
    frm.grid()
    window.title("Test window")

    ###########################################
    #             Additional cells            #
    ###########################################

    small_farms_var = StringVar(frm, New_domain.small_farms)
    small_farms = Entry(frm, textvariable=small_farms_var)
    small_farms.grid(column=2, row=2)

    big_farms_var = StringVar(frm, New_domain.big_farms)
    big_farms = Entry(frm, textvariable=big_farms_var)
    big_farms.grid(column=2, row=3)

    population_var = StringVar(frm, New_domain.population)
    population = Entry(frm, textvariable=population_var)
    population.grid(column=2, row=6)

    productivity_small_farms = 180 # do not work now
    productivity_var = StringVar(frm, productivity_small_farms)
    productivity = Entry(frm, textvariable=productivity_var)
    productivity.grid(column=3, row=2)

    ###########################################
    #                 Functions               #
    ###########################################

    def XXXX():
        New_domain.population = int(population_var.get())
        New_domain.small_farms = int(small_farms_var.get())
        New_domain.big_farms = int(big_farms_var.get())
        New_domain.population = New_domain.small_farms*59
        print(New_domain.population)
        population_var.set(New_domain.population)
        small_farms_var.set(New_domain.small_farms)

    Label(frm, text = "Small villages").grid(column=1, row=2)
    Label(frm, text = "Big villages").grid(column=1, row=3)
    Label(frm, text = "how many?").grid(column=2, row=1)
    Label(frm, text = "Productivity").grid(column=3, row=1)
    Label(frm, text = "Population").grid(column=1, row=6)
    Button(frm, text="Generate based on villages", command=XXXX).grid(column=2, row=4, columnspan=2)
    Button(frm, text="Generate based on population", command=XXXX).grid(column=2, row=5, columnspan=2)

    
    window.mainloop()