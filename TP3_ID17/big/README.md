# TP3_17 Big : Système de Recommandation de Jeux Vidéo (Steam) avec PySpark

* **Auteur :** HAMRIT Wassim (5A FISE)
* **Technologies :** Python, Apache Spark (PySpark SQL & MLlib), Jupyter Notebook

---

## 1. État d'exécution du notebook

**Le notebook est fonctionnel et s'exécute intégralement** (de la récupération automatique des données jusqu'à l'entraînement du modèle et l'affichage des métriques d'évaluation).

---

## 2. Problèmes rencontrés et résolutions

* **Taille importante des données (~2 Go, +40 millions d'avis) :** Le chargement classique en mémoire avec Pandas saturait la RAM. **Résolution :** Passage complet du projet sous **PySpark**, qui répartit les calculs et ne les exécute qu'au moment nécessaire, évitant ainsi de surcharger la mémoire.
* **Données trop dispersées (trop peu d'avis par joueur ou par jeu) :** La majorité des joueurs et des jeux n'ont qu'une ou deux interactions, ce qui dégrade l'apprentissage collaboratif. **Résolution :** Application d'un filtrage par seuil minimal d'activité (≥ 5 avis par utilisateur et ≥ 20 avis par jeu).
* **Limite de la variable cible binaire (`is_recommended`) :** Un simple booléen (`True`/`False`) ne permet pas de nuancer l'intensité de l'intérêt d'un joueur. **Résolution :** Construction d'une note continue sur 5 (`rating_score`) pondérée par le temps de jeu relatif et l'utilité sociale des avis.
* **Limite de taille des fichiers sur GitHub (100 Mo) :** Impossible de versionner directement le dossier `dataset/` de 2 Go. **Résolution :** Exclusion des données brutes via `.gitignore` (tout en conservant l'arborescence avec `.gitkeep`) et ajout d'une cellule de téléchargement automatique via `kagglehub` au début du notebook.

---

## 3. Liste des modifications apportées

Le notebook a été structuré et complété selon le pipeline complet **Data · EDA · Prétraitement · Transformation · ML · Éval** :

1. **Récupération automatique des données (`Data`) :**
   * Ajout d'une cellule d'initialisation qui télécharge et extrait automatiquement les 4 fichiers (`games.csv`, `games_metadata.json`, `recommendations.csv`, `users.csv`) depuis Kaggle vers `./dataset/` s'ils ne sont pas déjà présents localement.
   * Configuration de la `SparkSession` et chargement distribué des tables en définissant la structure des tables.
2. **Exploration des données (`EDA`) :**
   * Analyse du nombre d'enregistrements (joueurs, jeux, avis), des distributions de temps de jeu (`hours`), du taux de recommandation globale et identification des valeurs aberrantes.
3. **Nettoyage et filtrage (`Prétraitement`) :**
   * Suppression des valeurs extrêmes de temps de jeu (`> 20 000 h`) et suppression des doublons sur les paires `(user_id, app_id)`.
   * Vérification de la cohérence des identifiants avec les tables `games` et `users` via des semi-jointures distribuées (`left_semi` join).
   * Filtrage des utilisateurs et des jeux trop peu actifs (≥ 5 avis/utilisateur, ≥ 20 avis/jeu), conservant plus de 22,3 millions d'avis exploitables.
4. **Création de nouvelles variables (`Transformation`) :**
   * Calcul d'un score d'appréciation `rating_score` (entre `1.0` et `5.0`) combinant `is_recommended`, le logarithme du temps de jeu normalisé par titre (`log1p(hours)`) et la pertinence de l'avis (`helpful`).
5. **Modélisation (`ML`) :**
   * Découpage aléatoire en jeu d'entraînement (80 % - 17,87 M avis) et jeu de test (20 % - 4,47 M avis).
   * Entraînement d'un modèle de filtrage collaboratif par factorisation de matrices **ALS** (`pyspark.ml.recommendation.ALS` avec `rank=16`, `regParam=0.1`).
   * Génération de recommandations personnalisées Top-N et association avec les titres des jeux.
6. **Évaluation et analyse (`Éval`) :**
   * Comparaison des performances face à une baseline naïve (prédiction de la moyenne globale) via les métriques **RMSE**, **MAE**, **AUC-ROC** et **Accuracy**.
   * Rédaction des analyses, conclusions et pistes d'amélioration (gestion du *Cold-Start* via une approche hybride avec `games_metadata.json` et validation croisée).

---

## 4. Informations utiles & Guide d'exécution

### Prérequis techniques
* **Python 3.9+** et **Java (JDK 8, 11 ou 17)** requis pour exécuter Apache Spark.
* Bibliothèques Python principales :
  ```bash
  pip install pyspark kagglehub jupyter pandas matplotlib seaborn


## Lancer le notebook

1. Cloner ce dépôt et ouvrir le fichier `.ipynb` dans Jupyter Notebook ou VS Code.
2. Exécuter toutes les cellules dans l'ordre.

> **Note :** Lors de la première exécution, la première cellule téléchargera automatiquement le dataset (~2 Go) dans le dossier `./dataset/`. Les exécutions suivantes réutiliseront directement les fichiers locaux.

## Résumé des résultats obtenus (jeu de test)

| Modèle | RMSE | MAE | AUC-ROC | Accuracy (seuil = 3.0) |
|---|---:|---:|---:|---:|
| Baseline (Moyenne globale) | 0.9845 | 0.6971 | 0.5000 (aléatoire) | - |
| PySpark ALS (rank=16, reg=0.1) | 0.9914 | 0.7568 | 0.7685 | 81.51 % |

**Interprétation :** Bien que le biais positif des avis Steam et la régularisation donnent un RMSE proche de la baseline, le modèle ALS démontre un fort pouvoir discriminant (AUC-ROC de 0,7685 et 81,51 % d'Accuracy), permettant de personnaliser efficacement les recommandations là où la baseline reste uniforme.