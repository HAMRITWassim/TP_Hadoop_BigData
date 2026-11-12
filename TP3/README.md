# TP3 : Système de Recommandation d'Animes par Clustering d'Utilisateurs

Ce projet implémente un système de recommandation d'animes en se basant sur le clustering des profils utilisateurs. L'objectif est d'exploiter les notes des utilisateurs et les caractéristiques des animes pour regrouper les profils similaires. Le pipeline de traitement des données suit une approche structurée allant de l'exploration des données brutes jusqu'à l'entraînement et l'évaluation du modèle d'apprentissage automatique.

### Données utilisées

- Notes attribuées par les utilisateurs aux animes.
- Caractéristiques descriptives des animes : genres, types, nombre d'épisodes, etc.

### Pipeline d'analyse et de modélisation

#### 1. Analyse Exploratoire des Données (EDA)

- Analyse de la taille du jeu de données et identification de la forte proportion de notes `-1` (environ 19 %, signifiant « vu mais pas noté »).
- Analyse de la répartition du nombre de visionnages par utilisateur et de la distribution des genres et types d'animes.
- Identification des valeurs manquantes et des incohérences de référencement entre les tables.

#### 2. Prétraitement des données

- Suppression des doublons : même utilisateur, même anime.
- Gestion des notes manquantes : remplacement arbitraire des valeurs `-1` par `5` afin de différencier les animes vus mais non notés des animes non visionnés.
- Encodage One-Hot des variables catégorielles (`genre` et `type`) avec correction explicite du type de données (cast numérique) pour éviter les erreurs avec les versions récentes de Pandas.
- Agrégation des données pour créer des profils utilisateurs basés sur la note moyenne par genre et par type. Les catégories jamais visionnées sont remplies par des zéros.

#### 3. Transformation : réduction de dimensionnalité

- Application d'une Analyse en Composantes Principales (PCA) sur les profils utilisateurs pour réduire la dimensionnalité tout en conservant l'information essentielle.
- Sélection de 20 composantes principales, ce qui permet d'expliquer environ 77,5 % à 80 % de la variance totale du jeu de données.

#### 4. Machine Learning : clustering K-Means

- Utilisation de l'algorithme K-Means pour segmenter les utilisateurs en groupes de goûts similaires.
- Amélioration de la sélection du nombre de clusters k: ajout du calcul du score de silhouette pour valider la pertinence des clusters, la méthode du coude s'avérant insuffisante à elle seule.
- Mise à jour du code pour la compatibilité scikit-learn : suppression du paramètre déprécié `n_jobs` et ajout d'un `random_state` pour garantir la reproductibilité des résultats.
