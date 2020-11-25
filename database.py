"""Creating Database and Tables"""

from mysql_connector import dbcursor
from product import ProductManager
from categories import CategoryManager
from product_categories import TableInserter

"""Creating Table object"""
class Table:

     def __init__(self, name, attrs):

          self.name = name
          self.attrs = attrs

     def create_table(self):

          dbcursor.execute("USE pur_beurre;")
          dbcursor.execute("CREATE TABLE IF NOT EXISTS {}({})".format(self.name, self.attrs))

class Database:

     def __init__(self, products):
          self.products = products
          dbcursor.execute("CREATE DATABASE IF NOT EXISTS pur_beurre CHARACTER SET 'utf8';")

     """Main fonctions to execute, create database and then the tables"""
     def main_database(self): #RANGA metttre dans une classe
          products_table_attrs = "id BIGINT UNSIGNED NOT NULL, name VARCHAR(255) NOT NULL, nutriscore VARCHAR(1) NOT NULL, ingredients TEXT, url VARCHAR(255) NOT NULL, PRIMARY KEY(id) "

          products_table = Table("Products", products_table_attrs)
          
          product_categories_table_attrs = "id INT PRIMARY KEY AUTO_INCREMENT, idproduct BIGINT UNSIGNED NOT NULL, idcategory INT NOT NULL, FOREIGN KEY (idproduct) REFERENCES Products (id), FOREIGN KEY (idcategory) REFERENCES Categories (id)"

          product_categories_table = Table("Product_Categories", product_categories_table_attrs)
          
          categories_table_attrs = "id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL UNIQUE, PRIMARY KEY(id)"
          categories_table = Table("Categories", categories_table_attrs)

          stores_table_attrs = "id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL UNIQUE, PRIMARY KEY(id)"
          stores_table = Table("Stores", stores_table_attrs)

          product_stores_table_attrs = "id INT PRIMARY KEY AUTO_INCREMENT, idproduct BIGINT UNSIGNED NOT NULL, idstore INT, FOREIGN KEY (idproduct) REFERENCES Products (id), FOREIGN KEY (idstore) REFERENCES Stores (id)"
          product_stores_table = Table("Product_Stores", product_stores_table_attrs)

          favorites_table_attrs  = "id SMALLINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, id_product BIGINT UNSIGNED NOT NULL, FOREIGN KEY (id_product) REFERENCES Products (id)"
          favorites_table = Table("Favorites", favorites_table_attrs)


          products_table.create_table()
          categories_table.create_table()
          product_categories_table.create_table()
          stores_table.create_table()
          product_stores_table.create_table()
          favorites_table.create_table()

     def database_constructor(self):
         self.main_database()
         product_manager = ProductManager(self.products)
         product_manager.save()
         CategoryManager(self.products).save()
         TableInserter(self.products).insert()
         return product_manager
         # categories.
         # stores.storemanager.save()
         # product_categories.tableinserter.insert()
         # store_products.tableinserterII.insert()

