from product import ProductParser
from database import Database
from userInterface import UserInterface


def main():

    print(
        "<<< Bienvenue, l'application Pur Beurre vous permet de substituer "
        "vos aliments favoris par des alternatives plus saines. >>>\n"
    )
    product_parser = ProductParser().parser()
    product_manager = Database(product_parser).database_constructor()
    UserInterface().run_user_interface()
    # lancer l'application


if __name__ == "__main__":
    main()
