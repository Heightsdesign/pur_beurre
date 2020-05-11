import mysql.connector
from API import cleaned_products


db_pur_beurre = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eugenia06240',
    database = 'pur_beurre'
)

dbcursor = db_pur_beurre.cursor()

class Product_storage:

    def __init__(self, data):

        self.data = data

    def save(self):

       save_formula = "INSERT INTO product (id, name, nutrition_grade, ingredients, stores, url, categories) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
       dbcursor.executemany(save_formula, self.data)
       db_pur_beurre.commit()


Product_storage(cleaned_products).save()

