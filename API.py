# -tc- Attention, le nom d'un module python the doit pas contenir de majuscules
# -tc- Tu fais du doc driven development. Décrire chaque méthode avec une docstring avant son développement

import requests

"""imports products from api""" # -tc- la docstring va en dessous de la classe
class ProductDownloader:
     
    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    params = {
        "action" : "process",
        "sort_by" : "unique_scans_n",
        "page" : 1,
        "page_size" : 20,
        "json" : 1
        }

    @classmethod
    def get_products_by_category(cls, category): # -tc- Pourquoi une méthode de classe ? De toute manière tu instancees         
        cls.category = category
        cls.params.update(
            {
            "action" : "process",
            "sort_by" : "unique_scans_n",
            "page" : 1,
            "page_size" : 20,
            "json" : 1,
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": cls.category
            }
            )
        return cls()


    def request(self):

        return requests.get(self.url, params=self.params)

    def response(self):

        response = self.request()
        # -tc- Attention à faire de la gestion des erreurs
        self.data = response.json()
        return self.data

    def get_products_data(self):
   
        products_data = self.data["products"]
        return products_data 



class ProductParser:

    def __init__(self, parameter):
        # -tc- Instancier Product Downloader dans le parser ne semble pas logique ici. la liste de prodin't est définie à l' instanciation. Si j' appelle parser() plusieurs fois, ce sera toujours les mêmes données
        self.parameter = parameter
        self.data = ProductDownloader().response()

    def parser(self):
         
        cleanproducts = []
        rawproducts = self.data["products"]
        for product in rawproducts:
            # -tc- Attention à valider les données. C'est le role n°1 de ce parser
            cleanproducts.append([
                product["code"],
                product["product_name_fr"], 
                product["nutrition_grade_fr"].upper(), 
                product["ingredients_text_fr"],
                product["stores"],
                product["url"],
                product["categories"]
                ])
        return cleanproducts

param_1 = ProductDownloader().response()
# -tc- plus logique ProductParser().parse(param_1)
clean_prod = ProductParser(param_1).parser()

# -tc- faux si tu méthode est une méthode de classe
param_2 = ProductDownloader().get_products_by_category("pizza").response()
clean_prod_by_cat = ProductParser(param_2).parser()

#print(clean_prod_by_cat)
