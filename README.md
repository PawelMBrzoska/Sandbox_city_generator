# Sandbox_city_generator
My little project to manage worlds for RGPs

The plan is:

# Running the app

The app is easy and strightforward. Run Main.py. 
Then you can:
- Create and balance cities
    - Put the number of workshops and stuff and calculate whether it sums up or not. Then use some tools to optimize it. 
    - Use "$" anywhere to lock the workshops number. 

## Generating world

The plan is to be able to generate entire worlds with this script. 
With: Continents->Countries->Domains->Towns
For now we are in the Domains scale with space for towns customization

## Generating Towns

For now generating towns is semi-automatic and need a initial input and further optimization. 

# Rules and assumptions

## Population

## Workshops and production

For now the production backend is build on estimation from various sources (see References.txt)
The most important ones:
- Everything is based on cca XIII - XVI centuries so mid-late medieval.
- Prices are in penny (d, see: http://medieval.ucdavis.edu/120D/Money.html) more or less changed to RPG reality. 
- Nearly all production is level based and higher level production needs workers of lower levels. The levels are:
>    - 1lvl = unskilled begginer
>    - 2lvl = apprentice/journeyman who can craft basic stuff alone. Their are bread and butter of small towns. Their often had one unskilled worker.
>    - 3lvl = ~master level in medieval/historical meaning. More a skilled worker in RPG meaning. A workperson who can build or craft most of the stuff available in the setting. Have a workshop and few (avg 2) apprentice. 
>    - 4lvl = top level crafter, an RPG master crafter. Chief of the big craftguild in large city, who can build/craft magical items etc. Have a master-workshop with avg 4 3lvl workspersons as employees.
>    - 5lvl = Legendary level crafters who have nearly all knowledge of the certain craft domain. These can craft legendary-level items. To work they need legendary-workshop and a lot of masters to help. Place them in the setting wisely.
- All the calculations assume that people produce resources and spend another resources in nearly equal amount. E.g., the Smith produce Tools but need food, housing, fun, materials, and other stuff
There are few key resources:
>   - People (just to track)
>   - Food - to eat (~ 100d of food/person/year). Fancy food can be trated as Fun
>   - Buildings/housing/architecture - for all kind of rent, housing, workshops, buildings, even castles and other BIG structures.  
>   - Tools - This account for metal tools for everyday work of crafters. 
>   - Materials - This is mainly metals for Tools.
>   - Other - Everyone needs some less important for RPG gameplay stuff like candles, clothing, lamp oil, etc. This all are here.
>   - Fun - Everybody also needs fun. This is basicly a main way of spending wealth. If someone produce much more than need in materials, the difference is spend on some fun (including fancy food, feasts, parties, art, etc.) 
>   - Safety - This is for warfare and guards. Everyone needs to feel save which is a (a) defense structures like walls, and (b) guards. With this we can estimate the number of guard for example.
>   - Wood - This is mainly for architecture needs. 
>   - Stone - This is mainly for architecture needs. 


# Changelog

- 1.0 Working app
- 1.1 Basic optimization
- 1.2 Up and down optimization 
- 1.3 Optimization and force locking
- 2.0 New procedure -> starting with Domain level
# Plans
- Matching population distribution to the "Medieval Demographics Made Easy" by John Ross on the town scale. Or smthg?
- Reworking all the workshops
- Consideration of the terrain and geographic during generation of domain (where the cities will be and where the resources are produced)
- Terrain generation