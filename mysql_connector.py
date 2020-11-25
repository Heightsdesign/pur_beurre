import mysql.connector


db_pur_beurre = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ranga91600'
)

dbcursor = db_pur_beurre.cursor(buffered=True)
dbcursor.execute("CREATE DATABASE IF NOT EXISTS pur_beurre;")
