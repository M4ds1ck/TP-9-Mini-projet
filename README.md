# TP8 Python – Gestionnaires de Contexte (Context Managers)

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

Ce projet regroupe **les trois exercices du TP8**, dédiés à la maîtrise des **gestionnaires de contexte** en Python : utilisation de `__enter__` / `__exit__`, du module **contextlib**, et de la classe **ExitStack** pour gérer plusieurs ressources.

---

## 📂 Contenu du TP

Le TP8 est organisé en trois exercices :

* **EXERCICE 1 : Gestionnaires de contexte fondamentaux**
* **EXERCICE 2 : Context managers avancés + ExitStack**
* **EXERCICE 3 : Traitement de fichiers CSV avec logs automatiques**

Chaque exercice possède :

* un dossier dédié,
* les fichiers Python nécessaires,
* un script de test `test.py` pour valider le comportement.

---

# 🧪 EXERCICE 1 — Gestionnaires de contexte fondamentaux

### 🎯 Objectif

Comprendre comment créer un gestionnaire de contexte à la main (`__enter__` & `__exit__`) puis le réécrire avec `contextlib.contextmanager`. Enfin, apprendre à gérer plusieurs fichiers simultanément avec `ExitStack`.

---

## 📌 Partie 1 — Implémentation manuelle

Création de `TempFileWriter` :

* ouverture d’un fichier temporaire,
* écriture,
* suppression automatique à la sortie du bloc `with`.

Le test affiche :

```
Testing TempFileWriter
TempFileWriter test completed.
```

---

## 📌 Partie 2 — Version contextlib

Réécriture sous forme de générateur décoré avec `@contextmanager`.

Test :

```
Testing temp_file context manager
temp_file test completed.
```

---

## 📌 Partie 3 — Gestion multiple avec ExitStack

`ExitStack` permet d’ouvrir **n fichiers dynamiquement** et garantit leur fermeture même en cas d’erreur.

Résultat du test :

```
File a.txt created successfully
File b.txt created successfully
File c.txt created successfully
```

---

# 🧪 EXERCICE 2 — Combinaison Connexion + Logs + ExitStack

### 🎯 Objectif

Créer un gestionnaire de contexte simulant une **connexion à un service** tout en écrivant des logs.
Utilisation avancée de `ExitStack` pour composer plusieurs ressources.

---

## 📌 Partie 1 — ConnectionManager

Ce gestionnaire :

* affiche un message de connexion,
* retourne l’objet lui-même,
* affiche un message de déconnexion même si une erreur survient.

Sortie :

```
[2025-12-11 21:38:51] Connexion à Serveur X établie.
[2025-12-11 21:38:51] Déconnexion de Serveur X.
```

---

## 📌 Partie 2 — ExitStack avec logs

On ouvre simultanément :

* un fichier log,
* une connexion simulée.

Le test confirme :

```
task_with_logging completed
--- log.txt content ---
[...] Tâche effectuée sur Serveur X
```

---

## 📌 Partie 3 — Gestion des erreurs

Le test force une exception volontaire :

```
Caught exception as expected: Erreur de traitement
```

Les logs montrent que la connexion est tout de même fermée proprement :

```
Erreur détectée : RuntimeError — Erreur de traitement
Déconnexion de Base Y.
```

---

# 🧪 EXERCICE 3 — Traitement CSV + Logs

### 🎯 Objectif

Créer un système complet :

* lecture d’un fichier CSV,
* exécution d’opérations (add, subtract, multiply, divide),
* gestion d’inconnues,
* journalisation automatique ligne par ligne.

---

## 📌 Fonctionnalités principales

* Ouverture du CSV via un gestionnaire de contexte
* Création d’un fichier journal `journal.log`
* Enregistrement de chaque ligne traitée
* Gestion d’erreurs métier (opération inconnue)

Extrait du test :

```
Traitement add(10.0) -> 15.0
Traitement subtract(5.0) -> 3.0
Traitement multiply(3.0) -> 30.0
Traitement divide(2.0) -> 1.0
```

Journal généré :

```
[2025-12-11] Ligne traitée (4): ['multiply', '3']
[2025-12-11] Erreur traitement ligne 6: Opération inconnue: unknown
```

---

# 📘 Points pédagogiques du TP

✔ Compréhension fine de la mécanique `__enter__` / `__exit__`
✔ Usage du module standard `contextlib`
✔ Gestions avancées avec `ExitStack`
✔ Garanties de fermeture automatique des ressources
✔ Gestion propre des erreurs dans les blocs `with`
✔ Production de journaux pendant le traitement de tâches

---

# 💡 Extensions proposées

* Ajout de décorateurs pour automatiser les logs
* Mixins pour horodatage automatique
* Gestion parallèle de plusieurs connexions
* Système complet d’audit avec rotation des logs

---

# 👨‍💻 Auteur

**Nom :** Mahmoud Moukouch – 2333447
**Email :** [m.moukouch2471@uca.ac.ma](mailto:m.moukouch2471@uca.ac.ma)

**Projet :** TP8 Python — Gestionnaires de Contexte
