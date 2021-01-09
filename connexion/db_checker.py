"""This file contains fonction to check if the database is already created"""
from connexion.mysql_connector import dbcursor

def db_check():
    #this fonction checks if the database pur beurre exists if it does returns 1 else 0
    dbcursor.execute(
        "SELECT schema_name FROM information_schema.schemata "
        "WHERE schema_name = 'pur_beurre';"
        )

    db_exists = dbcursor.fetchall()
    return len(db_exists)