"""Main file, contains program interaction with user"""

from mysql_connector import dbcursor
import product
import constants

"""constants.selection"""


class UserInterface:

    def __init__(self):
        self.productmanager = product.ProductManager("product")

    def menu_constructor(self, lst):

        print("\n") 

        self.lst = lst
        x = 0

        for i in self.lst:
            x += 1
            print("\t" + str(x) + ". " + str(i))

        print("\n")

    def home_menu(self):

        while True:

            #print("1 : Categories Menu \n")
            #print("2 : Favories \n")

            menu = input(
                "Veuillez selectionner une option (entrez le chiffre correspondant ou entrez q pour quitter): ")
            print("\n")
            try:
                if int(menu) == 1:
                    constants.menu_choice.append(1)
                    break
                elif int(menu) == 2:
                    constants.menu_choice.append(2)
                    break

            except ValueError:

                if str(menu) == 'q':
                    break
                else:
                    print(
                        "Saisie incorrecte, veuillez entrer le chiffre correspondant au menu souhaité. \n")
                    self.menu_constructor(self.lst)

    def menu_selector(self):

        if constants.menu_choice[0] == 1:
            print("\t" + "CATEGORIES")
            constants.categories_menu = 1
        elif constants.menu_choice[0] == 2:
            print("\t" + "FAVORIES")
            constants.favorites_menu = 1
        else:
            print("Merci d'avoir utlisé Pur Beurre, à bientôt :) \n")

    def categories_menu(self):

        while constants.categories_menu == 1:

            constants.categories_menu = input(
                "Veuillez séléctionner la catégorie d'aliments que vous souhaitez substituer (entrez le chiffre correspondant ou q pour quitter le programme): ")
            print("\n")

            if int(constants.categories_menu) > 0 and int(constants.categories_menu) < 10:

                products_category = self.productmanager.products_category_fetcher()
                num = 0
                self.products_num = []
                for prod in products_category:
                    num += 1
                    self.products_num.append(num)
                    print("\t" + str(num) + ". " + str(prod[1]))
                break

            elif constants.categories_menu == 'q':
                print("Merci d'avoir utlisé Pur Beurre, à bientôt :)")
                break

            else:
                print("Saisie incorrecte veuillez entrer un chiffre correspondant à la catégorie souhaitée ou entrez 10 pour quitter le programme")
        return self.products_num

    def product_selection(self):

        print("\n")

        while True:

            constants.product_input = input(
                "Veuillez séléctionner le produit que vous souhaitez substituer (Entrez le chiffre correspondant): ")

            if int(constants.product_input) in self.products_num:
                self.productmanager.get_product_substitutes()
                prodselect = self.productmanager.get_product_substitutes_2()

            else:

                print("wrong data")
            
            return prodselect

    def give_letter_value(self, arg):

        self.arg = arg
        for letter in arg:
            if letter in constants.nutriscore:
                score = constants.nutriscore[letter]

        return score

    def result_parser(self, prodselect):

        favorite = []
        self.nutriscore = str(self.productmanager.get_product_nutriscore()[0]).replace(',',"").replace("'","").replace("(","").replace(")","")
        self.nutriscore = self.give_letter_value(self.nutriscore)
        product_count = 0
        for result in prodselect:
            for attributes in result:
                if self.nutriscore < self.give_letter_value(attributes[3]) and self.give_letter_value(attributes[3]) <= self.nutriscore + 2:
                    product_count += 1
                    
                    favorite.append(result)

                    if product_count == 0 and self.give_letter_value(attributes[3]) < self.nutriscore + 3:
                        product_count += 1
                        favorite.append(result)

                    elif product_count == 0 and self.give_letter_value(attributes[3]) < self.nutriscore + 4:
                        product_count += 1
                        favorite.append(result)

                    elif product_count > 1:
                        favorite.pop(1)

        for product in favorite:
            for attribute in product :
                print("___________________________________________________________________________________________________________" + "\n")
                print("Nom: " + str(attribute[0]) + "\n")
                print("Code: " + str(attribute[1] ) + "\n")
                print("Ingredients: " + str(attribute[2]) + "\n")
                print("Nutriscore: " + str(attribute[3]) + "\n")
                print("URL: " + str(attribute[4]) + "\n")
                print("___________________________________________________________________________________________________________" + "\n")
                    
        #print(favorite)
        return favorite


    def favorites_menu(self):

        print("Favories")

    def run_user_interface(self):

        self.menu_constructor(constants.selection)
        self.home_menu()
        self.menu_selector()

        if constants.categories_menu == 1:
            self.menu_constructor(constants.categories_menu_list)
            self.categories_menu()
            prodselect = self.product_selection()
            self.result_parser(prodselect)

        else:
            self.favorites_menu()