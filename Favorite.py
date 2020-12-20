"""This file is the favorite object and favorite manager"""

from mysql_connector import db_pur_beurre
from mysql_connector import dbcursor


class Favorite:
    # This is the Favorite object class

    def __init__(self, id):
        self.id = id

    def save(self):
        # Saves the id (id_product) attribute of the favorite
        # in the Favorites table of the database

        dbcursor.execute("USE pur_beurre;")
        dbcursor.execute(
            "INSERT IGNORE into Favorites(id_product) "
            "VALUES('%s');" % (self.id)
        )

        db_pur_beurre.commit()

    def fetcher(self):
        # This method gets all the favorites
        # saved by the user in the db
        # it retreives them by searching the
        # id_product column saved in the Favorites tab
        # to the corresponding codes in the
        # id column in the products tab

        dbcursor.execute("USE pur_beurre;")
        dbcursor.execute(
            "SELECT * FROM Products "
            "INNER JOIN Favorites ON Products.id = Favorites.id_product "
            "WHERE Products.id = Favorites.id_product;"
        )

        stored_favorites = dbcursor.fetchall()

        # print(self.stored_favorites)

        return stored_favorites

    def parser(self):
        # Prints the inforamtion retrieved by the
        # fetcher method in a readable manner.

        self.fetcher()

        for product in self.fetcher():
            print(
                "_______________________________________________________"
                + "____________________________________________________"
                + "\n"
            )
            print("Nom: " + str(product[1]) + "\n")
            print("Nutriscore: " + str(product[2]) + "\n")
            print("Ingredients: " + str(product[3]) + "\n")
            print("URL: " + str(product[4]) + "\n")
