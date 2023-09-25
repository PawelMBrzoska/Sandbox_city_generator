# Sandbox_city_generator
My little project to manage worlds for RGPs

The plan is:
![The Algorithm](https://github.com/PawelMBrzoska/Sandbox_city_generator/assets/125125417/8b6dc59f-6b12-4102-b410-50d80ed729ec)

# Running the app

The app is easy and straightforward. Run Main.py. 
Then you can:
- Create and balance cities
    - Put the number of workshops and stuff and calculate whether it sums up. Then use some tools to optimize it. 
    - Use "$" anywhere to lock the workshop number. 

## Generating world

The plan is to be able to generate entire worlds with this script. 
With: Continents->Countries->Domains->Towns
For now, we are in the Domain scale with space for Town customization

## Generating Towns

For now, generating towns is semi-automatic and needs an initial input and further optimization. 

# Rules and assumptions

## Population

## Domain functioning
![Domain graph](https://github.com/PawelMBrzoska/Sandbox_city_generator/assets/125125417/1ae6abe2-986e-4a94-8cf8-34f082244d89)

## Workshops and production

For now, the production backend is built on estimation from various sources (see References.txt)
The most important ones:
- Everything is based on cca XIII - XVI centuries so mid-late medieval.
- Prices are in a penny (d, see: http://medieval.ucdavis.edu/120D/Money.html) more or less changed to RPG reality. 
- Nearly all production is level based and higher level production needs workers of lower levels. The levels are:
>    - 1lvl = unskilled begginer
>    - 2lvl = apprentice/journeyman who can craft basic stuff alone. They are the bread and butter of small towns. They often had one unskilled worker.
>    - 3lvl = ~master level in medieval/historical meaning. More a skilled worker in RPG meaning. A workperson who can build or craft most of the stuff available in the setting. Have a workshop and a few (avg 2) apprentices. 
>    - 4lvl = top-level crafter, an RPG master crafter. Chief of the big craft guild in a large city, who can build/craft magical items etc. Have a master workshop with avg 4 3lvl workspersons as employees.
>    - 5lvl = Legendary level crafters who have nearly all knowledge of the certain craft domain. These can craft legendary-level items. To work they need legendary-workshop and a lot of masters to help. Place them in the setting wisely.
- All the calculations assume that people produce resources and spend another resource in nearly equal amounts. E.g., the Smiths produce Tools but need food, housing, fun, materials, and other stuff
There are a few key resources:
>   - People (just to track)
>   - Food - to eat (~ 100d of food/person/year). Fancy food can be treated as Fun
>   - Buildings/housing/architecture - for all kind of rent, housing, workshops, buildings, even castles and other BIG structures.  
>   - Tools - This accounts for metal tools for the everyday work of crafters. 
>   - Materials - This is mainly metals for Tools.
>   - Other - Everyone needs some less important RPG gameplay stuff like candles, clothing, lamp oil, etc. This all is here.
>   - Fun - Everybody also needs fun. This is basically the main way of spending wealth. If someone produces much more than needed in materials, the difference is spent on some fun (including fancy food, feasts, parties, art, etc.) 
>   - Safety - This is for warfare and guards. Everyone needs to feel safe which is a (a) defense structures like walls, and (b) guards. With this, we can estimate the number of guards for example.
>   - Wood - This is mainly for architectural needs. 
>   - Stone - This is mainly for architectural needs. 


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
