# Calculateur de Hachage SHA256

## Description

Ce projet consiste en une application web qui permet de calculer des hachages pour une chaîne de caractères donnée en entrée. Par défaut, l'algorithme utilisé est le SHA256, mais l'utilisateur peut choisir un autre algorithme de hachage. Les résultats sont ensuite sauvegardés dans un historique consultable via une interface web.

L'application utilise Flask pour le serveur web, Docker pour l'encapsulation et l'exécution de l'application, et hashlib pour les calculs de hachage.

## Fonctionnalités

- Calcul du hachage : L'utilisateur peut soumettre une chaîne de caractères et obtenir son hachage (SHA256 par défaut).
- Choix de l'algorithme : Il est possible de choisir un autre algorithme de hachage (comme MD5, SHA1, etc.).
- Historique des hachages : L'application conserve un historique des hachages calculés et permet de le consulter à tout moment via l'API.
- Interface utilisateur : Une page web permet de soumettre des chaînes de caractères et de voir les résultats du hachage.

## Prérequis

- Python 3.x
- Flask pour l'application web
- Docker pour la conteneurisation

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone <url-du-dépôt>

2- Accédez au répertoire du projet :
cd docker_hash_app

3- Installez les dépendances :
pip install -r requirements.txt

4- Lancer l'application
Option 1 : Avec Docker 
Construisez l'image Docker : docker-compose build
L'application sera disponible à l'adresse suivante : http://127.0.0.1:5000

- app.py : Fichier principal qui définit l'application Flask et les routes.
- templates/index.html : Page d'accueil avec un formulaire pour calculer les hachages.
- Dockerfile : Fichier de configuration pour Docker.
- docker-compose.yml : Fichier de configuration pour Docker Compose.
- requirements.txt : Liste des dépendances Python pour l'application.
