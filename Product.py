"""This file uses the data collected from the api file and creates and object Product from it and adds the object in a list"""

from api import ProductDownloader
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor

"""Creating Product object"""
class Product:

    #initializes the object with attributes passed as arguments
    def __init__(self, id, name, nutriscore, ingredients, stores, url, categories):

        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.ingredients = ingredients
        self.stores = stores
        self.url = url
        self.categories = categories


"""Iterates through the data and creates objects from of it and adds them to a list"""
class ProductParser: 

    #initializes object ProductParser, the parameters passed as an argument are determined in the ProductDownloader class
    def __init__(self, parameter):

        self.parameter = parameter
        self.data = ProductDownloader().response()

    #verifies if products attributes are valid
    def is_valid(self, prod): 

        self.prod = prod

        #keys = attributes considered necessary to add a product to our list
        keys = ("code", "product_name_fr", "nutrition_grade_fr", "categories")
        for key in keys:
            #checking if the attributes or their value exists
            if key not in prod or not prod[key]:
                return False
        return True

    """Iterates through data, creates object from it and adds them to a list"""
    def parser(self):

        products = self.data["products"]
        obj_list = []
        for prod in products:
            if self.is_valid(prod):
                product = Product(
                    prod["code"], 
                    prod["product_name_fr"], 
                    prod["nutrition_grade_fr"], 
                    prod["ingredients_text_fr"], 
                    prod["stores"], 
                    prod["url"], 
                    prod["categories"])
            obj_list.append(product)
        return obj_list


param_1 = ProductDownloader().response()
productlist = ProductParser(param_1).parser()

print(productlist)



class ProductManager:

    def save(self):
        pass


products = [Product(id, name, nutriscore, ingredients, stores, url, categories) for id, name, nutriscore, ingredients, stores, url, categories in productlist]