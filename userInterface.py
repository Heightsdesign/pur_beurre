"""Main file, contains program interaction with user"""

from mysql_connector import dbcursor
import product
import constants

"""constants.selection"""


class UserInterface:

    def __init__(self):
        self.productmanager = product.ProductManager("product")

    def menu_constructor(self, lst):

        self.lst = lst
        x = 0

        for i in self.lst:
            x += 1
            print("\t" + str(x) + ". " + str(i))

        print("\n")

    def home_menu(self):

        while True:

            print("1 : Categories Menu \n")
            print("2 : Favories \n")

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
            constants.categories_menu = 1
        elif constants.menu_choice[0] == 2:
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
                    print("\t" + str(num) + ". " + str(prod))
                break

            elif constants.categories_menu == 'q':
                print("Merci d'avoir utlisé Pur Beurre, à bientôt :)")
                break

            else:
                print("Saisie incorrecte veuillez entrer un chiffre correspondant à la catégorie souhaitée ou entrez 10 pour quitter le programme")
        return self.products_num

    def product_selection(self):

        while True:


            constants.product_input = input(
                "Veuillez séléctionner le produit que vous souhaitez substituer (Entrez le chiffre correspondant): ")

            if int(constants.product_input) in self.products_num:
                self.productmanager.get_product_substitutes()
                prodselect = self.productmanager.get_product_substitutes_2()

            else:

                print("wrong data")
            
            return prodselect

    def result_parser(self, prodselect):

        for result in prodselect:
            for attributes in result:
                if str(attributes[3]) in constants.nutriscore:
                    print("___________________________________________________________________________________________________________" + "\n")
                    print("Nom: " + str(attributes[0]) + "\n")
                    print("Code: " + str(attributes[1] ) + "\n")
                    print("Ingredients: " + str(attributes[2]) + "\n")
                    print("Nutriscore: " + str(attributes[3]) + "\n")
                    print("URL: " + str(attributes[4]) + "\n")
                    #à faire : n'afficher que 5 substitus et les trier par nutriscore

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
            print("Favories")