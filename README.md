# BookBot

BookBot est un outil d'analyse de texte en Python qui permet de compter les mots et la fréquence d'apparition des caractères dans un fichier texte.

Ce projet fait partie du parcour de développeur Back-End de [**Boot-Dev**](https://www.boot.dev/tracks/backend)

## Fonctionnalités

- Lecture de fichiers texte
- Comptage du nombre total de mots
- Analyse de la fréquence d'apparition de chaque lettre
- Tri des résultats par ordre décroissant d'occurrences
- Génération d'un rapport détaillé

## Structure du Code

Le projet est composé de plusieurs fonctions :

- `get_content_file()` : Lit le contenu d'un fichier texte
- `counter_word()` : Compte le nombre de mots dans le texte
- `get_number_cara()` : Compte la fréquence de chaque caractère
- `get_letter()` : Vérifie si un caractère est une lettre
- `convert_to_list_dict()` : Convertit les données en liste de dictionnaires pour le tri
- `sort_on()` : Fonction de tri pour les résultats

## Installation

Clonez le repository

```shell
git clone https://github.com/VotreUsername/bookbot.git
cd bookbot
```

Assurez-vous d'avoir Python 3.x installé

## Utilisation

Placez votre fichier texte dans le dossier `books/`

Exécutez le script :

```shell
python3 main.py
```

### Format de Sortie

Le script génère un rapport au format suivant :

```py
--- Begin report of [chemin_du_fichier] ---
[nombre] words found in the document
The '[lettre]' character was found [nombre] times
...
--- End report ---
```

## Structure du Projet

```shell
Copybookbot/
├── main.py
├── books/
│ └── frankenstein.txt
└── README.md
```

## À Venir

- Support de plusieurs fichiers
- Analyses statistiques supplémentaires
- Interface en ligne de commande pour le choix du fichier

## Licence

Ce projet est sous licence libre. N'hésitez pas à l'utiliser et à le modifier selon vos besoins.
