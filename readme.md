# Food Tracker
This app is supposed to track calories consumed by the user and show him
how much calories he has left before reaching his or her limit. And what 
kinds of food the user is allowed to eat before said limit is reached.
The app should not only track those data from food the user eats but also
support making recipes from with a combination of ingredients. The user should
also be able to change those recipes or use them as a blueprint for future recipes.
The user shall be enabled to eat only part of a recipe. 
Normal known foods shall be taken from a food databank such as openfoodfacts.

---

### resources:
- https://openfoodfacts.github.io/openfoodfacts-server/api/tutorial-off-api/
- https://github.com/openfoodfacts/openfoodfacts-python/tree/develop?tab=readme-ov-file
- https://openfoodfacts.github.io/openfoodfacts-python/usage/
- https://world.openfoodfacts.org/data
- https://static.openfoodfacts.org/data/data-fields.txt


- might be easier to download the csv or json file to retrieve the needed data
  for the production of the app
- mongodb
- python openfoodfacts api
  - loading dataset
- csv


### Features of the app:
- search for foods and their information
- save them in a favourites list
- track eaten foods and their caloric and nutritional value
- give suggestions on what foods can be consumed with calories left
- create dishes
- give suggestions for foods or ingredients based on users profile or
  goals
- share recepies on databank so others can use them with the ingredients they have at home


- sometimes in the future even combine with a grocery list
- telling us what to buy where to buy why to buy
- telling us which ingredients we need for cooking
- telling us which ingredients might be spoiling soon


- user profile
    - setting caloric limit and nutritional goals
    - Create a list of recipes for frequently consumed foods and own creations
    - store data about the user such as
        - weight
        - age
        - height
        - caloric limit
        - training?

### Dependencies
python 3.12.3
openfoodfacts 0.3.0
pandas 2.2.2
mongodb or csv

graphical interface like tkinter?
barcode reader for easily reading barcodes from products
