"""This file inserts the data in the intermidiate table product_categories"""

from mysql_connector import dbcursor, db_pur_beurre
from product import productlist
import categories


class TableInserter:
    """use this cass to insert data into the product_categories table"""
    def __init__(self, product):

        self.product = product

    def insert(self):
        
        dbcursor.execute("USE pur_beurre;")
        for product in productlist: 
            for category in product.categories.split(','):

                dbcursor.execute(
            "INSERT IGNORE INTO product_categories (idproduct, idcategory) "
            "VALUES (%(product_code)s, (SELECT id FROM categories WHERE name=%(category_name)s))",
            {"category_name": category,  "product_code": product.id}
        )

            db_pur_beurre.commit()

tableinserter = TableInserter("product")
tableinserter.insert()