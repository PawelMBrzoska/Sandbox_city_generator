import pandas as pd
import os
import sys
import math
import copy

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))
resources = ["People", "Food", "Buildings", "Tools", "Materials", "Other", "Safety", "Fun", "Wood","Stone", "Herbs", "Transport"]

class city:
    def __init__(self, entities = None, number = None): # new materials have to be updated here
        self.entities: dict = {}
        self.entities_dict: dict = {}
        self.entities_unlocked: list = []
        self.People: int = 0
        self.Food: int = 0
        self.Buildings: int = 0
        self.Tools: int = 0
        self.Materials: int = 0
        self.Other: int = 0
        self.Safety: int = 0
        self.Fun: int = 0
        self.Wood: int = 0
        self.Stone: int = 0
        self.Herbs: int = 0
        self.Transport: int = 0
        self.df = None
        self.number:str = number
        self.cells: dict = {}
        self.labels: dict = {}
        self.Suma: float = 0

    def Get_entities_dict(self):
        df = pd.read_excel("test.xlsx")

        # Extract the relevant columns
        entity_names = df['Kto'].tolist()
        entity_attributes = df.drop('Kto', axis=1).to_dict(orient='records')

        # Create a dictionary of entities with their respective attributes
        entities = {}
        for name, attributes in zip(entity_names, entity_attributes):
            entities[name] = attributes
        
        self.entities_dict = entities

    def Reset(self):
        self.People = 0
        self.Food = 0
        self.Buildings = 0
        self.Tools = 0
        self.Materials = 0
        self.Other = 0
        self.Safety = 0
        self.Fun = 0
        self.Wood = 0
        self.Stone = 0
        self.Herbs = 0
        self.Transport = 0
        self.Suma = 0

    def Get_resources(self):

        self.Reset()

        for entity in self.entities:
            for res in resources:
                setattr(self, res, (getattr(self, res)+self.entities_dict[entity][res]*self.entities[entity]))

    def Update_resources_up(self):
        ranking = {}   
        City2 = city()  

        for entity in self.entities_unlocked: #For each possible entity create a new city and add this entity to it 
            Suma = 0
            City2 = copy.copy(self)
            City2.Suma = 0 # Reset the sum
            for res in resources: #Add the resources for the entity
                setattr(City2, res, (getattr(self, res)+self.entities_dict[entity][res]))
            
            for i, res in enumerate(resources):
                City2.Suma += getattr(City2, res)**2

            City2.Suma -= getattr(City2, "People")**2

            Suma = City2.Suma/City2.People # This is basically a optimization function. As city size inflated margin of error, we get an error per person
            Suma = round(math.log10(Suma),3) # And as it is HUGE often we get log10 to comprehend this number ;D    
            ranking[entity] = Suma
            for res in resources: #And substract them
                setattr(City2, res, (getattr(self, res)-self.entities_dict[entity][res]))

        sorted_tests = sorted(ranking.items(), key=lambda x: x[1])
        return(sorted_tests)

    def Update_resources_down(self):
        ranking = {}
        
        City2 = city()
        
        for entity in self.entities_unlocked:
            if int(self.cells[entity].get()) > 0:
                Suma = 0
                City2 = copy.copy(self)
                City2.Suma = 0 # Reset the sum
                for res in resources: #Substract the resources for the entity
                    setattr(City2, res, (getattr(self, res)-self.entities_dict[entity][res]))

                for i, res in enumerate(resources):
                    City2.Suma += getattr(City2, res)**2

                City2.Suma -= getattr(City2, "People")**2

                Suma = City2.Suma/City2.People # This is basically a optimization function. As city size inflated margin of error, we get an error per person
                Suma = round(math.log10(Suma),3) # And as it is HUGE often we get log10 to comprehend this number ;D
                ranking[entity] = Suma

                for res in resources: #And add them back 
                    setattr(City2, res, (getattr(self, res)+self.entities_dict[entity][res]))

        sorted_tests = sorted(ranking.items(), key=lambda x: x[1])
        return(sorted_tests)



class domain:
    def __init__(self): # new materials have to be updated here
        self.small_farms: int = 0
        self.big_farms: int = 0
        self.population: int = 0
        self.Cities: list = []

    def Reset(self):
        self.small_farms = 0
        self.big_farms = 0
        self.population = 0
        self.Cities = []

if __name__ == "__main__":
    pass
