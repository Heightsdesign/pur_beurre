"""This file uses the data collected from the api file and creates and object Product from it and adds the object in a list"""

from api import ProductDownloader
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor

class Product:
    """Creating Product object"""
    
    def __init__(self, id, name, nutriscore, ingredients, stores, url, categories):
    #initializes the object with attributes passed as arguments

        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.ingredients = ingredients
        self.stores = stores
        self.url = url
        self.categories = categories



class ProductParser: 
    """Iterates through the data and creates objects from of it and adds them to a list"""
    
    def __init__(self, parameter):
    #initializes object ProductParser, the parameters passed as an argument are determined in the ProductDownloader class

        self.parameter = parameter
        self.data = ProductDownloader().response()

    
    def is_valid(self, prod): 
    #verifies if products attributes are valid

        self.prod = prod

        #keys = attributes considered necessary to add a product to our list
        keys = ("code", "product_name_fr", "nutrition_grade_fr", "categories")
        for key in keys:
            #checking if the attributes or their value exists
            if key not in prod or not prod[key]:
                return False
        return True

    
    def parser(self):
        """Iterates through data, creates object from it and adds them to a list"""

        products = self.data["products"]
        obj_list = []
        for prod in products:
            if self.is_valid(prod):
                product = Product(
                    prod["code"], 
                    prod["product_name_fr"], 
                    prod["nutrition_grade_fr"], 
                    prod.get("ingredients_text_fr",""),
                    prod.get("stores",""),
                    prod["url"], 
                    prod["categories"]
                )
            obj_list.append(product)
        return obj_list


param_1 = ProductDownloader().response()
productlist = ProductParser(param_1).parser()

#for prod in productlist:
    #print(prod.id)
#print(productlist[1].categories)

class ProductManager:
    """Methods to execute with product objects"""

    def __init__(self, product):

        self.product = product

    def save(self):
    #Inserts products in database
        
        
        dbcursor.execute("USE pur_beurre;")
        for product in productlist:
            dbcursor.execute(
                "INSERT IGNORE into Products(id, name, nutriscore, ingredients, url) "
                "VALUES('%s','%s','%s','%s','%s');" %
                (
                    product.id, 
                    product.name.replace("'", " "), 
                    product.nutriscore, 
                    product.ingredients.replace("'", " "), 
                    product.url)
                )
            
        db_pur_beurre.commit()

productmanager = ProductManager("product")
productmanager.save()