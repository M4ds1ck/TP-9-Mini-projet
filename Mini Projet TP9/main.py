from models import Produit, Client
from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO

def choisir_dao():
    print("Choisir le backend (1=SQLite, 2=MySQL)")
    choix = input("Votre choix: ").strip()
    if choix == '2':
        host = input("MySQL host [localhost]: ").strip() or 'localhost'
        user = input("MySQL user [root]: ").strip() or 'root'
        password = input("MySQL password []: ")
        database = input("MySQL database [boutique]: ").strip() or 'boutique'
        return MySQLDAO(host=host, user=user, password=password, database=database)
    return SQLiteDAO()

def menu(dao):
    actions = {
        '1': 'Ajouter produit',
        '2': 'Lister produits',
        '3': 'Modifier prix produit',
        '4': 'Ajouter client',
        '5': 'Lister clients',
        '6': "Rechercher client par email",
        '0': 'Quitter'
    }
    while True:
        for k, v in actions.items():
            print(k, v)
        choix = input("Choix: ").strip()
        if choix == '1':
            nom = input("Nom produit: ").strip()
            prix = float(input("Prix: ").strip())
            p = Produit(nom=nom, prix=prix)
            dao.ajouter_produit(p)
            print("Ajouté:", p)
        elif choix == '2':
            for p in dao.lister_produits():
                print(p)
        elif choix == '3':
            pid = int(input("ID produit: ").strip())
            np = float(input("Nouveau prix: ").strip())
            ok = dao.modifier_prix_produit(pid, np)
            print("Modifié" if ok else "Produit non trouvé")
        elif choix == '4':
            nom = input("Nom client: ").strip()
            email = input("Email: ").strip()
            c = Client(nom=nom, email=email)
            dao.ajouter_client(c)
            print("Ajouté:", c)
        elif choix == '5':
            for c in dao.lister_clients():
                print(c)
        elif choix == '6':
            email = input("Email à rechercher: ").strip()
            c = dao.rechercher_client_par_email(email)
            print(c if c else "Aucun client")
        elif choix == '0':
            dao.close()
            break

if __name__ == '__main__':
    dao = choisir_dao()
    menu(dao)
