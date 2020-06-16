"""This file uses the data collected from the api file and creates and object Product from it and adds the object in a list"""

from api import ProductDownloader
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor


class Product:
    """-tc- Class representing a product."""

    # initializes the object with attributes passed as arguments
    def __init__(
        self, id, name, nutriscore, ingredients, stores, url, categories
    ):
        """ -tc- Initializes a product object."""

        self.id = id
        self.name = name
        self.nutriscore = nutriscore
        self.ingredients = ingredients
        self.stores = stores
        self.url = url
        self.categories = categories


"""Iterates through the data and creates objects from of it and adds them to a list"""
# -tc- Décrit plus une action qu'une classe (famille d'objets)


class ProductParser:

    # initializes object ProductParser, the parameters passed as an argument are determined in the ProductDownloader class
    # -tc- utiliser une docstring pour documenter le constructeur
    def __init__(self, parameter):

        self.parameter = parameter  # -tc- à quoi sert ce paramètre
        # -tc- pas une bonne idée de coupler ProductDownloader et ProductParser.
        # -tc- plutôt exécuter ProductDownloader().response() hors de la classe
        # -tc- et passer la liste en argument de ta méthode parser: parser(liste_de_produits)
        self.data = ProductDownloader().response()

    # verifies if products attributes are valid
    def is_valid(self, prod):

        self.prod = prod

        # keys = attributes considered necessary to add a product to our list
        keys = ("code", "product_name_fr", "nutrition_grade_fr", "categories")
        for key in keys:
            # checking if the attributes or their value exists
            if key not in prod or not prod[key]:
                return False
        return True

    """Iterates through data, creates object from it and adds them to a list"""

    def parser(self):
        """-tc- ajouter une docstring descriptive."""
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
                    prod["categories"],
                )
            obj_list.append(product)
        return obj_list


param_1 = ProductDownloader().response()
# -tc- Plus logique:
# productlist = ProductDownloader().response()
# productlist = ProductParser().parser(productlist)
productlist = ProductParser(param_1).parser()

"""for product in productlist:
    print(product.id)"""


class ProductManager:
    """-tc- ajouter une docstring descriptive."""

    # -tc- Ajouter un paramètre à la méthode, sinon, on ne sait quoi sauver
    def save(self):
        """-tc- ajouter une docstring descriptive."""
        # products = [Product(id, name, nutriscore, ingredients, stores, url, categories) for id, name, nutriscore, ingredients, stores, url, categories in productlist]
        dbcursor.execute(
            "USE pur_beurre;"
        )  # -tc- à priori, dès la connexion, on se connecte à la base. L'utilisateur pourrait ne pas l'appeler pur beurre
        for product in productlist:
            dbcursor.execute(
                # ne pas utiliser de format avec une requête d'insersion. Voir la documentation de mysql
                "INSERT into Products(id, name, nutriscore, ingredients, url) VALUES({},{},{},{},{})".format(
                    product.id,
                    product.name,
                    product.nutriscore,
                    product.ingredients,
                    product.url,
                )
            )
