import requests
import mysql.connector

db_pur_beurre = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eugenia06240'
    database = 'pur_beurre'
)

dbcusor = db_pur_beurre.cursor()

class Get_data:

    def __init__(self, url, params):

        self.url = url
        self.params = params
        response = requests.get(self.url, params=self.params)
        self.data = response.json()


    def clean(self):

        cleanproducts = []
        rawproducts = self.data["products"]
        for product in rawproducts:
            cleanproducts.append([
                {product["code"] : [
                product["product_name_fr"], 
                product["nutrition_grade_fr"].upper(), 
                product["ingredients_text_fr"],
                product["url"],
                product["categories"],
                product["stores"]]}
                ])
        return cleanproducts


parametre_1 = Get_data("https://fr.openfoodfacts.org/cgi/search.pl", {
            "action" : "process",
            "sort_by" : "unique_scans_n",
            "page" : 1,
            "page_size" : 20,
            "json" : 1
        })

cleaned_products = parametre_1.clean()


"""print(cleaned_products)"""
print(db_pur_beurre)

