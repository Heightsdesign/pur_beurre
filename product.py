"""This file uses the data collected from the api file and creates and object Product from it and adds the object in a list"""

from api import ProductDownloader
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor
import constants


class Product:
    """Creating Product object"""

    def __init__(self, id, name, nutriscore, ingredients, stores, url, categories):
        # initializes the object with attributes passed as arguments

        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.ingredients = ingredients
        self.stores = stores
        self.url = url
        self.categories = categories


class ProductParser:
    """Iterates through the data and creates objects from of it and adds them to a list"""

    def __init__(self):
        # initializes object ProductParser, the parameters passed as an argument are determined in the ProductDownloader class

        self.data = ProductDownloader().response()

    def is_valid(self, prod):
        # verifies if products attributes are valid

        self.prod = prod

        # keys = attributes considered necessary to add a product to our list
        keys = ("code", "product_name_fr", "nutrition_grade_fr", "categories")
        for key in keys:
            # checking if the attributes or their value exists
            if key not in prod or not prod[key]:
                return False
        return True

    def parser(self):
        """Iterates through data, creates object from it and adds them to a list"""
        obj_list = []
        for page in self.data:
            products = page["products"]
            for prod in products:
                if self.is_valid(prod):
                    product = Product(
                        prod["code"],
                        prod["product_name_fr"],
                        prod["nutrition_grade_fr"],
                        prod.get("ingredients_text_fr", ""),
                        prod.get("stores", ""),
                        prod["url"],
                        prod["categories"]
                    )
                obj_list.append(product)
        return obj_list

class ProductManager:
    """Methods to execute with product objects"""

    def __init__(self, products):

        self.product_list = products

    def save(self):
        # Inserts products in database

        dbcursor.execute("USE pur_beurre;")
        for product in self.product_list:
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

    def products_category_fetcher(self):
        # Gets products from the selected category

        dbcursor.execute("USE pur_beurre")

        dbcursor.execute(
            "SELECT products.id, products.name "
            "FROM products "
            "INNER JOIN product_categories ON product_categories.idproduct = products.id "
            "INNER JOIN categories ON product_categories.idcategory = categories.id "
            "WHERE categories.name = %(category)s",
            {'category': constants.categories_menu_list[int(constants.categories_menu) - 1]})

        self.result = dbcursor.fetchall()

        return self.result

    def get_product_nutriscore(self):
        #Gets the product nutriscore 
        dbcursor.execute("USE pur_beurre")

        dbcursor.execute(
            "SELECT products.nutriscore "
            "FROM products "
            "WHERE products.id = %(prod)s",
            {'prod': str(self.result[int(constants.product_input) - 1]).replace('(', '').replace(')', '').replace(',', '').replace("'", '')})

        nutriscore = dbcursor.fetchall()
        
        return nutriscore

    def get_product_categories(self):
        
        dbcursor.execute("USE pur_beurre")

        dbcursor.execute(
            "SELECT categories.name "
            "FROM categories "
            "INNER JOIN product_categories ON product_categories.idcategory = categories.id "
            "INNER JOIN products ON product_categories.idproduct = products.id "
            "WHERE products.id = %(prod)s",
            {'prod': str(self.result[int(constants.product_input) - 1]).replace('(', '').replace(')', '').replace(',', '').replace("'", '')})

        product_cats = dbcursor.fetchall()

        return product_cats

    def get_product_substitutes(self):

        self.substitutes_categories = []
        self.substitutes = {}
    
        dbcursor.execute("USE pur_beurre")

        dbcursor.execute(
            "SELECT products.id "
            "FROM products "
            "INNER JOIN product_categories ON product_categories.idproduct = products.id "
            "INNER JOIN categories ON product_categories.idcategory = categories.id "
            "WHERE categories.name IN (SELECT categories.name "
            "FROM categories "
            "INNER JOIN product_categories ON product_categories.idcategory = categories.id "
            "INNER JOIN products ON product_categories.idproduct = products.id "
            "WHERE products.id = %(product)s)",
            {'product': str(self.result[int(constants.product_input) - 1]).replace('(', '').replace(')', '').replace(',', '').replace("'", '')})
        # 1. gets all products(possible substitutes) with at least one common category

        substitutes_ids = dbcursor.fetchall()

        for substitute in substitutes_ids:
            dbcursor.execute("USE pur_beurre")
            dbcursor.execute(
                "SELECT categories.name "
                "FROM categories "
                "INNER JOIN product_categories ON product_categories.idcategory = categories.id "
                "INNER JOIN products ON product_categories.idproduct = products.id "
                "WHERE products.id = %(substitute)s",
                {'substitute': str(substitute).replace('(', '').replace(')', '').replace(',', '').replace("'", '')})
            # 2.  gets all the categories names attached to the possible substitutes found in step 1

            fetcher = dbcursor.fetchall()
            

            self.substitutes_categories.append(fetcher)
            for categories in self.substitutes_categories:
                self.substitutes.update([(substitute, categories)])
                # zips the possible substitutes and their categories in a dict
        
        return self.substitutes

    def get_product_substitutes_2(self):

        substitutes_final = []
        for substitute, categories in self.substitutes.items():
            shared_categories = 0
            for category in categories:
                if category in self.get_product_categories():
                    shared_categories += 1
            self.substitutes.update([(substitute, shared_categories)])

        sorted_substitutes = sorted(
            self.substitutes.items(), key=lambda x: x[1], reverse=True)
            # sorts the substitutes by most shared categories with the original product

        for key, shared_cat in sorted_substitutes:
            
            if shared_cat > 1:
            #verifies if they have more than 1 category in common
                dbcursor.execute("USE pur_beurre")
                dbcursor.execute(
                    "SELECT products.name, products.id, products.ingredients, products.nutriscore, products.url "
                    "FROM products "
                    "WHERE products.id = %(name)s ",
                    {'name': str(key[0]).replace('(', '').replace(')', '').replace(
                        ',', '').replace("'", '').strip()}
                )
                substitutes_fetcher = dbcursor.fetchall()
                substitutes_final.append(substitutes_fetcher)

        return substitutes_final



