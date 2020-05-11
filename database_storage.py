import mysql.connector
from API import cleaned_products

db_pur_beurre = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eugenia06240',
    database = 'pur_beurre'
)

dbcusor = db_pur_beurre.cursor()

print(cleaned_products)