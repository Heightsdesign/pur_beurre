""" -tc- Ajouter une docstring: tu dois faire du 
driven-development. Ecris chaque docstring avant de coder.
"""
# -tc- Pourquoi importes-tu mysql.conneector? Attention à respecter la PEP8
# -tc- dans les imports
import mysql.connector
from API import cleaned_products
from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor


# -tc- Attention à utiliser des noms de classe conformes: ProductStorage
class Product_storage:
    """ -tc- Ajouter une docstring: tu dois faire du 
    driven-development. Ecris chaque docstring avant de coder.
    """

    # -tc- passer les données via self n'est pas une bonne idée, car ta classe
    # -tc- ProductStorage ne doit pas servir qu'à faire un save. Passe ton
    # -tc- instance de product directement à save.
    def __init__(self, data):
        """ -tc- Ajouter une docstring: tu dois faire du 
        driven-development. Ecris chaque docstring avant de coder.
        """
        self.data = data

    # -tc- typiquement, on s'attend à ce que save reçoive une instance de la
    # -tc- classe product en paramètre
    def save(self):
        """ -tc- Ajouter une docstring: tu dois faire du 
        driven-development. Ecris chaque docstring avant de coder.
        """
        # -tc- attention à ne pas dépasser les 79 caractères
        # -tc- attention à ne pas stocker categories et stores dans product.
        save_formula = "INSERT INTO product (id, name, nutrition_grade, ingredients, url, categories, stores) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        dbcursor.executemany(save_formula, self.data)
        db_pur_beurre.commit()

    # -tc- save(self, produit) étant un nom naturel pour sauver une instance
    # -tc- de produit en base. Créer un save_all pour tout sauver.


# -tc- Créer des CategoryStorage, StoreStorage et FavoriteStorage pour gérer
# -tc- chaque table de ta base

Product_storage(cleaned_products).save()
