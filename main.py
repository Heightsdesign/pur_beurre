from db_and_objects.product import ProductParser
from db_and_objects.database import Database
from interface.userInterface import UserInterface


def main():

    print(
        "<<< Bienvenue, l'application Pur Beurre vous permet de substituer "
        "vos aliments favoris par des alternatives plus saines. >>>\n"
    )
    product_parser = ProductParser().parser()
    product_manager = Database(product_parser).database_constructor()
    UserInterface().run_user_interface()
    # launch application


if __name__ == "__main__":
    main()
