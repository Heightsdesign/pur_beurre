""" -tc- Ajouter une docstring: tu dois faire du 
doc-driven-development. Ecris chaque docstring avant de coder.
"""

import requests

# -tc- attention à ne pas choisir les noms de tes classes selon des actions
# -tc- mais des noms de choses: par exemple ProductDownloader
class Get_data:
    """ -tc- Ajouter une docstring: tu dois faire du 
    driven-development. Ecris chaque docstring avant de coder.
    """

    def __init__(self, url, params):
        """ -tc- Ajouter une docstring: tu dois faire du 
        driven-development. Ecris chaque docstring avant de coder.
        """
        # -tc- recevoir les paramètres et l'url de l'extérieur ne me semble
        # -tc- pas une bonne idée dans ce cas.
        self.url = url
        self.params = params
        # -tc- gérer le fait que requests.get peut échouer et éviter de faire
        # -tc- l'appel à l'API dans le constructeur. Créer des méthodes
        # -tc- get_by_category, get_by_nutriscore, get, etc
        response = requests.get(self.url, params=self.params)
        self.data = response.json()

    # -tc- Utiliser une classe séparée pour le cleaning
    def clean(self):
        """ -tc- Ajouter une docstring: tu dois faire du 
        driven-development. Ecris chaque docstring avant de coder.
        """
        cleanproducts = []
        rawproducts = self.data["products"]
        for product in rawproducts:
            # -tc- utiliser une liste ne me semble pas approprié.
            # -tc- ta boucle va s'arrêter dès qu'une clé sera absente du
            # -tc- dictionnaire. Tu dois valider que toutes ses clés sont dans
            # -tc- le dictionnaire du produit.
            cleanproducts.append(
                [
                    product["code"],
                    product["product_name_fr"],
                    product["nutrition_grade_fr"].upper(),
                    product["ingredients_text_fr"],
                    product["stores"],
                    product["url"],
                    product["categories"],
                ]
            )
        return cleanproducts


# -tc- si tu fais des tests, fais-le dans un autre fichier

parametre_1 = Get_data(
    "https://fr.openfoodfacts.org/cgi/search.pl",
    {
        "action": "process",
        "sort_by": "unique_scans_n",
        "page": 1,
        "page_size": 20,
        "json": 1,
    },
)

cleaned_products = parametre_1.clean()

# -tc- éviter print pour faire du debug. Apprend à utiliser le débogueur qui
# -tc- facilitera bien la vie.
"""print(cleaned_products[0])"""
