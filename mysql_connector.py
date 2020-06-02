import mysql.connector


# -tc- Demander à l'utilisateur ses données de connexion dans un fichier de config
db_pur_beurre = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eugenia06240',
    database = 'pur_beurre'
)

# -tc- Créer une connection centralisée Ok. Créer un curseur centralisé n'est pas une super idée
dbcursor = db_pur_beurre.cursor()
