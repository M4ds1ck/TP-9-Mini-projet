# 🚀 TP9 Python — Mini Projet POO + SQLite & MySQL

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/) [![DB: SQLite | MySQL](https://img.shields.io/badge/DB-SQLite%20%7C%20MySQL-orange)](https://www.mysql.com/)  

Un mini-projet de TP pour mettre en pratique la Programmation Orientée Objet en Python et la connexion à deux types de bases de données : une base embarquée (SQLite) et une base distante (MySQL). L'objectif est d'avoir deux DAO interchangeables qui exposent la même interface pour gérer des Produits et des Clients.

---

## 📌 Table des matières
- [Objectif](#-objectif)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Configuration MySQL](#-configuration-mysql)
- [Utilisation](#-utilisation)
- [Exemples](#-exemples)
- [Bonnes pratiques / améliorations possibles](#-bonnes-pratiques--améliorations-possibles)
- [Auteur](#-auteur)
- [Licence](#-licence)

---

## 🎯 Objectif
Développer un système simple et clair capable de :
- Gérer des entités métier : Produits et Clients.
- Fournir deux backends (SQLite et MySQL) avec la même interface DAO.
- Permettre de tester les opérations via un menu CLI.

---

## ✅ Fonctionnalités implémentées
- Entités :
  - Produit : id, nom, prix
  - Client : id, nom, email
- DAO SQLite (`sqlite_dao.py`) :
  - Connexion automatique à `boutique.db`
  - Création des tables si elles n'existent pas
  - Opérations CRUD (ajouter, lister, modifier, rechercher)
- DAO MySQL (`mysql_dao.py`) :
  - Connexion via `mysql-connector-python`
  - Même interface et méthodes que le DAO SQLite
- Interface CLI (`main.py`) avec menu simple pour tester les opérations

---

## 📂 Structure du projet
