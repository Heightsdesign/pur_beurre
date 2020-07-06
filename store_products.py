"""This file inserts the data in the intermidiate table product_stores"""

from mysql_connector import dbcursor, db_pur_beurre
from product import productlist
import categories


class TableInserterII:
    """use this cass to insert data into the product_stores table"""
    def __init__(self, product):

        self.product = product

    def insert(self):
        
        dbcursor.execute("USE pur_beurre;")
        for product in productlist: 
            for store in product.stores.split(','):

                dbcursor.execute(
            "INSERT IGNORE INTO product_stores (idproduct, idstore) "
            "VALUES (%(product_code)s, (SELECT id FROM stores WHERE name=%(store_name)s))",
            {"store_name": store,  "product_code": product.id}
        )

            db_pur_beurre.commit()

tableinserterII = TableInserterII("product")
tableinserterII.insert()