"""This file contains everything related to the stores"""

from product import productlist
from mysql_connector import dbcursor, db_pur_beurre

class Store:
    """"Create an object stores with an id and a name as attributes"""

    def __init__(self, name):

        self.id = 0
        self.name = name

    
    def get_names(self):
        #get the names for the stores

        stores_names = [product.stores for product in productlist]
        stores_obj_list = []
        for names in stores_names:
            for name in names.split(','):
                self.name = name
                stores_obj_list.append(store.name)
        return stores_obj_list

store = Store("name")
#print(store.get_names())

class StoreManager:
    """Methods to execute on category objects"""

    def __init__(self, store):

        self.store = store

    def save(self):
        #Inserts store data in database

        stores = self.store.get_names()

        dbcursor.execute("USE pur_beurre;")
        command = "INSERT IGNORE INTO Stores (id, name) VALUES (NULL, %(name)s);"
        for name in stores:
            dbcursor.execute(command,{'name': name.strip()})
        db_pur_beurre.commit()

storemanager = StoreManager(store)
storemanager.save()