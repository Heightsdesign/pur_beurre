"""This file contains everything related to the categories"""
from mysql_connector import dbcursor, db_pur_beurre



# class Category:
#     """"Create an object Category with an id and a name as attributes"""

#     def __init__(self, name):

#         self.id = 0
#         self.name = name

    


# #category = Category("name")
# #categories = category._get_names()
# #print(category._get_names())


class CategoryManager:
    """Methods to execute on category objects"""

    def __init__(self, products):

        self.products = products

    def save(self):
        #Inserts category data in database

        categories = self._get_names()

        dbcursor.execute("USE pur_beurre;")
        command = "INSERT IGNORE INTO Categories (name) VALUES (%(name)s);"
        for name in categories:
                dbcursor.execute(command,{'name': name})
        db_pur_beurre.commit()

    # def save_in_list(self):

    #     categories = self._get_names()

    #     categories_variable = []
    #     for name in categories:
    #         #for name in cat:
    #         categories_variable.append(name)
    #     return categories_variable

    def _get_names(self):
    #get the names for the categories

        categories_names = [product.categories for product in self.products]
        categories_obj_list = []
        for names_list in categories_names:
            names = names_list.split(',')
            for name in names:
                if not (name in categories_obj_list):
                    categories_obj_list.append(name.strip())
        return categories_obj_list



    