# TP9 Python – Mini Projet POO + SQLite & MySQL

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Database](https://img.shields.io/badge/DB-SQLite%20%7C%20MySQL-orange)]()

Ce dépôt contient le **Mini Projet du TP9** portant sur la **Programmation Orientée Objet** et la **connexion aux bases de données** en Python. Le but est de comparer deux types de stockage :

* **SQLite** (base embarquée)
* **MySQL** (base distante)

---

## 📌 Objectif du mini-projet

Développer un système complet capable de gérer des **Produits** et des **Clients**, avec :

* Une structure objet claire (classes `Produit` et `Client`)
* Deux modules DAO indépendants

  * `sqlite_dao.py`
  * `mysql_dao.py`
* Les mêmes méthodes CRUD pour les deux bases
* Un fichier principal `main.py` permettant de tester les opérations via un menu CLI

---

## 📂 Structure du projet

```
TP9/
│
├── produit.py
├── client.py
│
├── sqlite_dao.py
├── mysql_dao.py
│
├── main.py
│
└── README.md
```

---

## 🧱 Fonctionnalités implémentées

### ✔️ 1. Gestion des entités métier

* Classe **Produit** : `id`, `nom`, `prix`
* Classe **Client** : `id`, `nom`, `email`

### ✔️ 2. DAO SQLite (`sqlite_dao.py`)

* Connexion automatique à **boutique.db**
* Création des tables si nécessaires
* Opérations :

  * Ajouter produit / client
  * Lister produits / clients
  * Rechercher client par email
  * Modifier prix d’un produit

### ✔️ 3. DAO MySQL (`mysql_dao.py`)

* Connexion via `mysql-connector-python`
* Même interface et mêmes méthodes que SQLite
* Permet de passer de MySQL ↔ SQLite sans modifier `main.py`

### ✔️ 4. Menu terminal (`main.py`)

Permet de tester toutes les opérations CRUD :

```
1 - Ajouter produit
2 - Ajouter client
3 - Lister produits
4 - Lister clients
5 - Rechercher client par email
6 - Modifier prix d’un produit
0 - Quitter
```

---

## 🚀 Exécution

### 1️⃣ Installer les dépendances

`bash\pip install mysql-connector-python`

### 2️⃣ Exécuter le projet

```bash
python main.py
```

---

## 🧪 Exemple d’utilisation

### Ajout d’un produit

```
Nom : PC Portable
Prix : 7500
Produit ajouté avec succès.
```

### Liste des produits

```
1 | PC Portable | 7500.0
2 | Souris | 99.0
```

### Recherche d’un client

```
Email : test@mail.com
Client trouvé : test@mail.com (Mahmoud)
```

---

## 📘 Critères d’évaluation respectés

* ✔️ Structuration du code
* ✔️ Utilisation correcte des classes et objets
* ✔️ Implémentation des requêtes SQL
* ✔️ Deux backends DB interchangeables
* ✔️ Gestion des erreurs (connexion, requêtes)
* ✔️ Menu CLI fonctionnel

---

## 👤 Auteur

**Mahmoud Moukouch – 2333447**
[Email] [m.moukouch2471@uca.ac.ma](mailto:m.moukouch2471@uca.ac.ma)
**GitHub :** [https://github.com/M4ds1ck](https://github.com/M4ds1ck)

Projet : **TP9 – Mini Projet POO + Base de données**
