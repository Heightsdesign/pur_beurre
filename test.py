from API import ProductDownloader
from API import clean_prod
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor

"""TEST !!!"""

class Product:

    def __init__(self, id, name, nutriscore, ingredients, stores, url, categories):

        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.ingredients = ingredients
        self.stores = stores
        self.url = url
        self.categories = categories

class ProductManager: 

    def list_products(self):
        pass
        products_data = ProductDownloader().response()
        


#list of product objects
products = [Product(id, name, nutriscore, ingredients, stores, url, categories) for id, name, nutriscore, ingredients, stores, url, categories in clean_prod ]

#list of categories
products_categories = [Product.categories for Product in products]

#splitting the categories 
categories_names = [category for index in products_categories for category in index.split(',')]

#creating an id for each category
def add_id():
    ids = []
    for i in range(0, len(categories_names)):
        i += 1
        ids.append(i)
    return ids

# zipping the the ids with the names of the categories in a dictionnary
categories = {id : name for id, name in zip (add_id(), categories_names)}


""""Create an object Category with an id and a name as attributes"""
class Category:
    pass
    def __init__(self, id, name):

        self.id = id
        self.name = name


#products_categories_instances = 
#cat_names = [Category.name for Category in products_categories_instances]
print(categories)





