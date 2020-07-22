"""Main file, contains program interaction with user"""



"""Ask user for which categories of food he wants to have alternatives"""

#pseudocode !!!

#mettre message bienvenue
#accueil ---> 1 categories, 2 favoris, 3 quitter

#first_request = input("Choisissez un catégorie parmi celles affichées (veuillez selectionner le nombre correspondant)")

#categories_list = "categories list"
#main_loop = True
#while main_loop:

print("<<< Bienvenue, l'application Pur Beurre vous permet de substituer vos aliments favoris par des alternatives plus saines. >>>")
print("Veuillez selectionner une option (entrez le chiffre correspondant):")
x = 0
selection = [". Categories", ". Favories", ". Quitter"]

for i in selection:
    x += 1
    print(str(x) + i)

"""def showscreen():

    print(first_request)
    print(categories_list)

def get_category():

    food_data = []
    for category in categories_list:
        if first_request == category.id:
            food_data = [category food data]
        else :
            print("Saisie incorrecte, veuillez saisir un nombre correspondant à la catégorie souahitée.")
            showscreen()"""

