"""Test"""
from mysql_connector import dbcursor
from product import Product, ProductParser, ProductManager



#creating an id for each category
"""def add_id():
    ids = []
    for i in range(0, len(categories_names)):
        i += 1
        ids.append(i)
    return ids"""

# zipping the the ids with the names of the categories in a dictionnary
#categories = {id : name for id, name in zip (add_id(), categories_names)}

def cheatcodes():
    dbcursor.execute("DROP DATABASE IF EXISTS pur_beurre")

#cheatcodes()

"""for product in productlist:
    for i in range(20):
        print(product.id)"""

#products = [Product(id, name, nutriscore, ingredients, stores, url, categories) for id, name, nutriscore, ingredients, stores, url, categories in productlist]