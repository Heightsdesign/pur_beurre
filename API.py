import requests

"""imports products from api"""
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

        return requests.get(self.url, params=self.params)

    def response(self):

        response = self.request()
        self.data = response.json()
        return self.data

    def get_products_data(self):
   
        products_data = self.data["products"]
        return products_data



class ProductParser:

    def __init__(self, parameter):

        self.parameter = parameter
        self.data = ProductDownloader().response()

    def parser(self):
         
        cleanproducts = []
        rawproducts = self.data["products"]
        for product in rawproducts:
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
clean_prod = ProductParser(param_1).parser()

param_2 = ProductDownloader().get_products_by_category("pizza").response()
clean_prod_by_cat = ProductParser(param_2).parser()

#print(clean_prod_by_cat)