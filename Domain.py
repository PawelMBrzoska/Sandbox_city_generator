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

people_in_farm = 100

def Domain(New_domain):
    Window = Tk()
    frm = ttk.Frame(Window, padding=10) #Creating the GUI frame
    frm.grid()
    Window.title("Test window")
    City_population_var = StringVar(frm, 0)

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

    productivity_small_farms = 100
    productivity_var = StringVar(frm, productivity_small_farms)
    productivity = Entry(frm, textvariable=productivity_var)
    productivity.grid(column=3, row=2)

    towns_number = 0
    towns_number_var = StringVar(frm, towns_number)

    cities_number = 0
    cities_number_var = StringVar(frm, cities_number)

    capital_population = 0
    capital_population_var = StringVar(frm, capital_population)    


    ###########################################
    #                 Functions               #
    ###########################################
    def gen_cities():
        pop = int(City_population_var.get())
        if pop<250: 
            capital_population_var.set(0)
            towns_number_var.set(0)
            cities_number_var.set(0)

        elif pop<2000: 
            capital_population_var.set(pop)
            towns_number_var.set(0)
            cities_number_var.set(0)

        elif pop<4000:
            capital_population_var.set(int(pop*0.6))
            town_pop = int(pop*0.4)
            towns_number_var.set(1)
            cities_number_var.set(0)

        elif pop<10000:
            capital_population_var.set(int(pop*0.5))
            town_pop = int(pop*0.5)
            towns_number_var.set(town_pop/1500)
            cities_number_var.set(0)

        elif pop<20000:
            capital_population_var.set(int(pop*0.2))
            town_pop = int(pop*0.8)
            towns_number_var.set(town_pop/1500)
            cities_number_var.set(0)

        elif pop<80000:
            capital_population_var.set(int(pop*0.2))
            city_pop = int(pop*0.1)
            cities_number_var.set(city_pop/5000)
            town_pop = int(pop*0.7)
            towns_number_var.set(town_pop/1500)

        else:
            capital_population_var.set(int(pop*0.1))
            city_pop = int(pop*0.2)
            cities_number_var.set(city_pop/5000)
            town_pop = int(pop*0.7)
            towns_number_var.set(town_pop/1500)


    def gen_on_villages():
        #New_domain.population = int(population_var.get())
        New_domain.small_farms = int(small_farms_var.get())
        #New_domain.big_farms = int(big_farms_var.get()) # dodać % dużych-małych
        New_domain.population = int(New_domain.small_farms*(float(productivity_var.get())*people_in_farm/93))+1 # 93 is an average food consumption per person per year
        population_var.set(New_domain.population)
        small_farms_var.set(New_domain.small_farms)
        City_population_var.set(New_domain.population - (New_domain.small_farms*people_in_farm)) # In square mile farm town should be ~ 50-300 people. The rest in cities
        gen_cities()

    def gen_on_population():
        New_domain.population = int(population_var.get())+1
        New_domain.small_farms = int(New_domain.population*93/((float(productivity_var.get())*people_in_farm)))
        #New_domain.small_farms = int(New_domain.population/(float(productivity_var.get())/93)) # dodać % dużych-małych
        New_domain.population = int(New_domain.small_farms*((float(productivity_var.get())*people_in_farm))/93)+1
        population_var.set(New_domain.population)
        small_farms_var.set(New_domain.small_farms)
        City_population_var.set(New_domain.population - (New_domain.small_farms*people_in_farm)) # In square mile farm town should be ~ 50-300 people. The rest in cities
        gen_cities()

    def Exit():
        Window.destroy()

    Label(frm, text = "Small villages").grid(column=1, row=2)
    Label(frm, text = "Big villages").grid(column=1, row=3)
    Label(frm, text = "how many?").grid(column=2, row=1)
    Label(frm, text = "Productivity").grid(column=3, row=1)
    Label(frm, text = "Minimum is 94").grid(column=4, row=2) # This is how many food produce 1 worker. As 1 person eats 93 of food tha balnce should be positive ^^'
    Label(frm, text = "Population").grid(column=1, row=6)
    Label(frm, text = "Population in Cities").grid(column=1, row=7)
    Label(frm, textvariable=City_population_var).grid(column=2, row=7)
    Button(frm, text="Generate based on villages", command=gen_on_villages).grid(column=2, row=4, columnspan=2)
    Button(frm, text="Generate based on population", command=gen_on_population).grid(column=2, row=5, columnspan=2)
    Label(frm, text = "Towns").grid(column=1, row=8)
    Label(frm, text = "Cities").grid(column=1, row=9)
    Label(frm, text = "Capital population").grid(column=1, row=10)
    Label(frm, textvariable=towns_number_var).grid(column=2, row=8)
    Label(frm, textvariable=cities_number_var).grid(column=2, row=9)
    Label(frm, textvariable=capital_population_var).grid(column=2, row=10)
    Label(frm, text = "avg. population = 1500").grid(column=3, row=8)
    Label(frm, text = "avg. population = 5000").grid(column=3, row=9)
    Button(frm, text="Exit", command=Exit).grid(column=4, row=7)

    Window.mainloop()

if __name__ == "__main__":
    New_domain = Classes.domain()
    Domain(New_domain)
