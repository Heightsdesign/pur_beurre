"""Creating Database and Tables"""

from mysql_connector import dbcursor


class Database:

     def __init__(self, command):

          self.command = command
     
     # executes the command (as argument) to mysql
     def databasecreator(self):

          return dbcursor.execute(self.command)




"""Creating Table object"""
class Table:

     def __init__(self, name, attrs):

          self.name = name
          self.attrs = attrs

     def create_table(self):

          dbcursor.execute("USE pur_beurre;")
          dbcursor.execute("CREATE TABLE IF NOT EXISTS {}({}) ENGINE=INNODB;".format(self.name, self.attrs))


"""Main fonctions to execute, create database and then the tables"""
def main_database():

     database = Database("CREATE DATABASE IF NOT EXISTS pur_beurre CHARACTER SET 'utf8';")
     database.databasecreator()

     product_table_attrs = "id BIGINT UNSIGNED NOT NULL, name VARCHAR(100) NOT NULL, nutriscore CHAR(1) NOT NULL, ingredients TEXT, PRIMARY KEY(id) "
     product_table = Table("Product", product_table_attrs)
     product_table.create_table()

     product_categories_table_attrs = "id_product BIGINT UNSIGNED NOT NULL, id_category SMALLINT UNSIGNED NOT NULL"
     product_categories_table = Table("Product-Category", product_categories_table_attrs)
     product_categories_table.create_table()

     categories_table_attrs = "id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(100)"
     categories_table = Table("Categories", categories_table_attrs)
     categories_table.create_table()


