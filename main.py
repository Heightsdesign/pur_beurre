"""Main file, contains program interaction with user"""
from mysql_connector import dbcursor

#pseudocode !!!

#mettre message bienvenue
#accueil ---> 1 categories, 2 favoris, 3 quitter

#first_request = input("Choisissez un catégorie parmi celles affichées (veuillez selectionner le nombre correspondant)")

#categories_list = "categories list"

print("<<< Bienvenue, l'application Pur Beurre vous permet de substituer vos aliments favoris par des alternatives plus saines. >>>\n")
        

selection = [". Categories", ". Favories", ". Quitter"]
menu_choice = []
categories_menu = 0
categories_menu_list = ["Aliments d'origine vegetale", "Boissons", "Céréales", "Légumes", "Pains", "Produits Laitiers", "Produits à tartiner", "Sauces", "Snacks"]


while 1:

    x = 0

    for i in selection:
        x += 1
        print("\t" + str(x) + i)

    print("\n")

    menu = int(input("Veuillez selectionner une option (entrez le chiffre correspondant): "))
    print("\n")
    if menu == 1:
        print("Categories Menu \n")
        menu_choice.append(1)
        break
    elif menu == 2:
        print("favories")
        break
    elif menu == 3:
        print("Merci d'avoir utlisé Pur Beurre, à bientôt :)")
        break
    else:
        print("Saisie incorrecte, veuillez entrer le chiffre correspondant au menu souhaité. \n")
        break


if menu_choice[0] == 1 :
    categories_menu = 1

while categories_menu == 1:

    y = 0
    for category in categories_menu_list:
        y += 1
        print("\t" + str(y) + ". " + category)
    print("\n")
    
    categories_menu = int(input("Veuillez séléctionner la catégorie d'aliments que vous souhaitez substituer (entrez le chiffre correspondant): "))
    if categories_menu > 0 and categories_menu < 10 :
        index = categories_menu - 1
        dbcursor.execute("USE pur_beurre")
        dbcursor.execute(
    "SELECT products.name AS prodname "
    "FROM products "
    "INNER JOIN product_categories ON product_categories.idproduct = products.id "
    "INNER JOIN categories ON product_categories.idcategory = categories.id "
    "WHERE categories.name = %(category)s",
    {'category' : categories_menu_list[index]})

        result = dbcursor.fetchall()

        for product in result:
            print(product)
            break
        
    elif categories_menu == 10 : 
        print("Merci d'avoir utlisé Pur Beurre, à bientôt :)")
        break


