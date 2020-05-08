import requests

class Get_data:

    def __init__(self, url, params):

        self.url = url
        self.params = params
        response = requests.get(self.url, params=self.params)
        self.data = response.json()


param1 = Get_data("https://fr.openfoodfacts.org/cgi/search.pl", {
            "action" : "process",
            "sort_by" : "unique_scans_n",
            "page" : 1,
            "page_size" : 20,
            "json" : 1
        })

products = param1.data["products"]

first_product = products[1]
print(first_product["product_name_fr"])

