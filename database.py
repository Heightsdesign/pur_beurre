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
          dbcursor.execute("CREATE TABLE IF NOT EXISTS {}({})".format(self.name, self.attrs))


"""Main fonctions to execute, create database and then the tables"""
def main_database():

     database = Database("CREATE DATABASE IF NOT EXISTS pur_beurre CHARACTER SET 'utf8';")
     database.databasecreator()

     products_table_attrs = "id BIGINT UNSIGNED NOT NULL, name VARCHAR(100) NOT NULL, nutriscore CHAR(1) NOT NULL, ingredients TEXT, url TINYTEXT, PRIMARY KEY(id) "
     products_table = Table("Products", products_table_attrs)
     
     products_categories_table_attrs = "id INT PRIMARY KEY AUTO_INCREMENT, idproduct BIGINT UNSIGNED NOT NULL, idcategory INT NOT NULL, FOREIGN KEY (idproduct) REFERENCES Products (id), FOREIGN KEY (idcategory) REFERENCES Categories (id)"
     products_categories_table = Table("Products_Categories", products_categories_table_attrs)
     

     categories_table_attrs = "id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100), PRIMARY KEY(id)"
     categories_table = Table("Categories", categories_table_attrs)

     products_table.create_table()
     categories_table.create_table()
     products_categories_table.create_table()


main_database()