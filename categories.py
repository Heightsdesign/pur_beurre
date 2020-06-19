"""This file contains everything related to the categories"""

from product import productlist
from mysql_connector import dbcursor, db_pur_beurre



class Category:
    """"Create an object Category with an id and a name as attributes"""

    def __init__(self, name):

        self.id = 0
        self.name = name

    
    def get_names(self):
        #get the names for the categories

        categories_names = [Product.categories for Product in productlist]
        categories_obj_list = []
        for name in categories_names:
            self.name = name.split(',')
            categories_obj_list.append(category.name)
        return categories_obj_list

category = Category("name")
#print (category.get_names())


class CategoryManager:
    """Methods to execute on category objects"""

    def __init__(self, category):

        self.category = category

    def save(self):
        #Inserts category data in database

        categories = self.category.get_names()

        dbcursor.execute("USE pur_beurre;")
        command = "INSERT INTO Categories (id, name) VALUES (NULL, %(name)s);"
        for cat in categories:
            for name in cat:
                dbcursor.execute(command,{'name': name})
        db_pur_beurre.commit()

categorymanager = CategoryManager(category)
categorymanager.save()


def main_categories():
    pass

    