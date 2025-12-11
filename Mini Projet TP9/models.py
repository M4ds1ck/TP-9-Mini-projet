from dataclasses import dataclass

@dataclass
class Produit:
    id: int = None
    nom: str = ""
    prix: float = 0.0
    def __str__(self):
        return f"Produit(id={self.id}, nom='{self.nom}', prix={self.prix})"

@dataclass
class Client:
    id: int = None
    nom: str = ""
    email: str = ""
    def __str__(self):
        return f"Client(id={self.id}, nom='{self.nom}', email='{self.email}')"
