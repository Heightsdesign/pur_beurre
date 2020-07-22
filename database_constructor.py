"""This file builds and inserts all the data in tne database"""

import database
import product
import product_categories
import categories
import product_categories
import stores
import store_products

def database_constructor():

    database.main_database()
    product.productmanager.save()
    categories.categorymanager.save()
    stores.storemanager.save()
    product_categories.tableinserter.insert()
    store_products.tableinserterII.insert()

database_constructor()