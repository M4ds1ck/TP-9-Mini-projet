import sqlite3
from models import Produit, Client

class SQLiteDAO:
    def __init__(self, db_path='boutique.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    def _create_tables(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS produit (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, prix REAL NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, email TEXT UNIQUE NOT NULL)")
        self.conn.commit()
    def ajouter_produit(self, produit: Produit):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO produit (nom, prix) VALUES (?, ?)", (produit.nom, produit.prix))
        self.conn.commit()
        produit.id = cur.lastrowid
        return produit
    def lister_produits(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, prix FROM produit")
        rows = cur.fetchall()
        return [Produit(id=r[0], nom=r[1], prix=r[2]) for r in rows]
    def ajouter_client(self, client: Client):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO client (nom, email) VALUES (?, ?)", (client.nom, client.email))
        self.conn.commit()
        client.id = cur.lastrowid
        return client
    def lister_clients(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, email FROM client")
        rows = cur.fetchall()
        return [Client(id=r[0], nom=r[1], email=r[2]) for r in rows]
    def rechercher_client_par_email(self, email: str):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, email FROM client WHERE email = ?", (email,))
        row = cur.fetchone()
        return None if row is None else Client(id=row[0], nom=row[1], email=row[2])
    def modifier_prix_produit(self, produit_id: int, nouveau_prix: float):
        cur = self.conn.cursor()
        cur.execute("UPDATE produit SET prix = ? WHERE id = ?", (nouveau_prix, produit_id))
        self.conn.commit()
        return cur.rowcount > 0
    def close(self):
        self.conn.close()
