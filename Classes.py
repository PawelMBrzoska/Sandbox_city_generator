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
        self.problematic: str =""

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
            self.People += self.entities_dict[entity]['People']*self.entities[entity]
            self.Food += self.entities_dict[entity]['Food']*self.entities[entity]
            self.Buildings += self.entities_dict[entity]['Buildings']*self.entities[entity]
            self.Tools += self.entities_dict[entity]['Tools']*self.entities[entity]
            self.Materials += self.entities_dict[entity]['Materials']*self.entities[entity]
            self.Other += self.entities_dict[entity]['Other']*self.entities[entity]
            self.Safety += self.entities_dict[entity]['Safety']*self.entities[entity]
            self.Fun += self.entities_dict[entity]['Fun']*self.entities[entity]
            self.Wood += self.entities_dict[entity]['Wood']*self.entities[entity]
            self.Stone += self.entities_dict[entity]['Stone']*self.entities[entity]
            self.Herbs += self.entities_dict[entity]['Herbs']*self.entities[entity]
            self.Transport += self.entities_dict[entity]['Transport']*self.entities[entity]

    def Update_resources_up(self):
        ranking = {}
        
        City2 = city()
        
        for entity in self.entities:
            Suma = 0
            City2 = copy.copy(self)
            City2.Get_resources()
            City2.People += self.entities_dict[entity]['People']
            City2.Food += self.entities_dict[entity]['Food']
            City2.Buildings += self.entities_dict[entity]['Buildings']
            City2.Tools += self.entities_dict[entity]['Tools']
            City2.Materials += self.entities_dict[entity]['Materials']
            City2.Other += self.entities_dict[entity]['Other']
            City2.Safety += self.entities_dict[entity]['Safety']
            City2.Fun += self.entities_dict[entity]['Fun']
            City2.Wood += self.entities_dict[entity]['Wood']
            City2.Stone += self.entities_dict[entity]['Stone']
            City2.Herbs += self.entities_dict[entity]['Herbs']
            City2.Transport += self.entities_dict[entity]['Transport']
            for i, res in enumerate(resources):
                City2.Suma += getattr(City2, res)**2
            City2.Suma -= getattr(City2, "People")**2
            Suma = City2.Suma/City2.People # This is basically a optimization function. As city size inflated margin of error, we get an error per person
            Suma = round(math.log10(Suma),3) # And as it is HUGE often we get log10 to comprehend this number ;D
            
            ranking[entity] = Suma
            sorted_tests = sorted(ranking.items(), key=lambda x: x[1])

            #if tested_suma < New_suma: 
            #    New_suma = tested_suma
            #    New_entity = entity
            
        return(sorted_tests[0][0])

    def Update_resources_down(self):
        New_suma = self.Suma
        New_entity = ""
        for entity in self.entities:
            tested_suma = New_suma
            tested_suma -= self.entities_dict[entity]['Food']**2
            tested_suma -= self.entities_dict[entity]['Buildings']**2
            tested_suma -= self.entities_dict[entity]['Tools']**2
            tested_suma -= self.entities_dict[entity]['Materials']**2
            tested_suma -= self.entities_dict[entity]['Other']**2
            tested_suma -= self.entities_dict[entity]['Safety']**2
            tested_suma -= self.entities_dict[entity]['Fun']**2
            tested_suma -= self.entities_dict[entity]['Wood']**2
            tested_suma -= self.entities_dict[entity]['Stone']**2
            tested_suma -= self.entities_dict[entity]['Herbs']**2
            tested_suma -= self.entities_dict[entity]['Transport']**2
            tested_suma = tested_suma/(self.People+self.entities_dict[entity]['People'])
            tested_suma = round(math.log10(tested_suma),3)
            if tested_suma < New_suma: 
                New_suma = tested_suma
                New_entity = entity

        return(New_entity)

if __name__ == "__main__":
    pass
