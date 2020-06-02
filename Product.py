from API import ProductDownloader

class Product:

    def __init__(self, code, name, nutriscore, ingredients, url):

        self.code = code
        self.name = name
        self.nutrisocre = nutriscors
        self.ingredients = ingredients
        self.url = url

    def list_products(self):
        # -tc- éviterles couplages inutiles entre les classes. Je ne comprends pas l'objectif de cette méthode
        a_list_to_turn = ProductDownloader().get_products_data()
        products = [Product(code, name, nutriscore, ingredients, url) for code, product_name_fr, nutrition_grade_fr, ingredients_text_fr, url in clean_prod ]
        return products

product_list = Product(code, name, nutriscore, ingredients, url).list_products()
print(product_list)
