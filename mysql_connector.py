import mysql.connector


db_pur_beurre = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eugenia06240',
    #database = 'pur_beurre'
)

dbcursor = db_pur_beurre.cursor()
