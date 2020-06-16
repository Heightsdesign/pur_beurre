"""This file is used to contact the api and download data from it"""

import requests

"""imports products from api"""


class ProductDownloader:

    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    params = {
        "action": "process",
        "sort_by": "unique_scans_n",
        "page": 1,
        "page_size": 100,
        "json": 1,
    }

    """This class method will use our Productdownloader class and update the category we want, passed as and argument"""

    @classmethod
    def get_products_by_category(cls, category):
        """-tc- La docstring vient ici."""
        cls.category = category
        cls.params.update(
            {
                "action": "process",
                "sort_by": "unique_scans_n",
                "page": 1,
                "page_size": 20,
                "json": 1,
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": cls.category,
            }
        )
        return cls()

    # sends request to API
    def request(self):
        """-tc- documenter"""
        return requests.get(self.url, params=self.params)

    # stores response from API in a json format
    def response(self):
        """-tc- documenter"""
        response = self.request()
        # -tc- attention à gérer les erreurs
        self.data = response.json()
        return self.data


# -tc- pourquoi segmenter en 3 méthodes ici? Quel avantage pour l'utilisateur
# -tc- de ta classe ainsi que pour toi?
