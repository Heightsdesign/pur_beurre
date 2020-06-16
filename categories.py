"""This file contains everything related to the categories"""

from product import productlist


""""Create an object Category with an id and a name as attributes"""


class Category:
    def __init__(self, id, name):

        self.id = id
        self.name = name

    # get the names for the categories
    def get_names(self):
        # -tc - Product n'a pas d'attribut de classe categories
        categories_names = [Product.categories for Product in productlist]
