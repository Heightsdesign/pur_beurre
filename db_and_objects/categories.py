"""This file contains everything related to the categories"""
from connexion.mysql_connector import dbcursor, db_pur_beurre


class CategoryManager:
    """Methods to execute on category objects"""

    def __init__(self, products):

        self.products = products

    def save(self):
        # Inserts category data in database

        categories = self._get_names()

        dbcursor.execute("USE pur_beurre;")
        command = "INSERT IGNORE INTO Categories (name) VALUES (%(name)s);"
        for name in categories:
            dbcursor.execute(command, {"name": name})
        db_pur_beurre.commit()

    def _get_names(self):
        # gets the names for the categories

        categories_names = [product.categories for product in self.products]
        categories_obj_list = []
        for names_list in categories_names:
            names = names_list.split(",")
            for name in names:
                if not (name in categories_obj_list):
                    categories_obj_list.append(name.strip())
        return categories_obj_list
