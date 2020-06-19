"""This file is used to contact the api and download data from it"""

import requests


class ProductDownloader:
    """imports products from api"""
     
    url = "https://fr.openfoodfacts.org/cgi/search.pl"
    params = {
        "action" : "process",
        "sort_by" : "unique_scans_n",
        "page" : 1,
        "page_size" : 1000,
        "json" : 1
        }

    """This class method will use our Productdownloader class and update the category we want, passed as and argument"""
    @classmethod
    def get_products_by_category(cls, category):
        
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
        #sends request to API

        return requests.get(self.url, params=self.params)

    
    def response(self):
        #stores response from API in a json format
        
        data = []
        try:
          response = self.request()
        except requests.ConnectionError:
           pass
        else:
            if response.status_code == 200:
                # -tc- Attention à faire de la gestion des erreurs
                data = response.json()
        return data

