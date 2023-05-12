
import pandas as pd
import os
import sys

#Setting directory
os.chdir(os.path.dirname(sys.argv[0]))

class city:
    def __init__(self, entities = None, number = None): #, people = None, Buildings = None, Tools = None, Food = None, wood = None
        self.entities: dict = {}
        self.entities_dict: dict = {}
        self.People: int = 0
        self.Food: int = 0
        self.Buildings: int = 0
        self.Tools: int = 0
        self.Tools_materials: int = 0
        self.Other: int = 0
        self.Safety: int = 0
        self.Fun: int = 0
        self.Wood: int = 0
        self.Stone: int = 0
        self.Herbs: int = 0
        self.Transport: int = 0
        self.df = None
        self.number:str = number
        
    #def __str__(self):
    #    return f"""
    #            Game: Elf = {self.elf}, double strike = {self.doublestrike}, Total poison in T2 = {self.t2_damage}, 
    #            Total mana = {self.total_mana} including {self.g_mana} green mana and {self.r_mana} red mana
    #            """

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

    def Get_resources(self):
        self.People = 0
        self.Food = 0
        self.Buildings = 0
        self.Tools = 0
        self.Tools_materials = 0
        self.Other = 0
        self.Safety = 0
        self.Fun = 0
        self.Wood = 0
        self.Stone = 0
        self.Herbs = 0
        self.Transport = 0

        for entity in self.entities:
            self.People += self.entities_dict[entity]['People']*self.entities[entity]
            self.Food += self.entities_dict[entity]['Food']*self.entities[entity]
            self.Buildings += self.entities_dict[entity]['Buildings']*self.entities[entity]
            self.Tools += self.entities_dict[entity]['Tools']*self.entities[entity]
            self.Tools_materials += self.entities_dict[entity]['Tools_materials']*self.entities[entity]
            self.Other += self.entities_dict[entity]['Other']*self.entities[entity]
            self.Safety += self.entities_dict[entity]['Safety']*self.entities[entity]
            self.Fun += self.entities_dict[entity]['Fun']*self.entities[entity]
            self.Wood += self.entities_dict[entity]['Wood']*self.entities[entity]
            self.Stone += self.entities_dict[entity]['Stone']*self.entities[entity]
            self.Herbs += self.entities_dict[entity]['Herbs']*self.entities[entity]
            self.Transport += self.entities_dict[entity]['Transport']*self.entities[entity]



    def Run(self):
        #TU jakoś zrobić żeby sprawdzał czego brakuje i dorzucał rzeczy.
        print(city())



if __name__ == "__main__":
    pass
