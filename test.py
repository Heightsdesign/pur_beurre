from API import Get_data
from API import cleaned_products
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor

"""TEST !!!"""

class Product:

    def __init__(self, id, name, nutriscore, ingredients, stores, url, categories):

        self.id = "code"
        self.name = "product_name_fr"
        self.nutriscore = "nutrition_grade_fr"
        self.ingredients = "ingredients_text_fr"
        self.stores = "stores"
        self.url = "url"
        self.categories = "categories"

class ProductManager:

   """ def get_product(self):

        for i, data in enumerate (cleaned_products):"""

    def save(self, product):
        
        self.product = product

        save_formula = "INSERT INTO product (id, name, nutrition_grade, ingredients, stores, url, categories) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        dbcursor.execute(save_formula, self.product)
        db_pur_beurre.commit() 



"""class Category:
    pass
    def __init__(self, category):

        self.category = category"""
