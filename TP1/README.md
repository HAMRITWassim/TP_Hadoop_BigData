# TP1 : Analyse des performances de comptage de mots (Word Count)

## Description du projet
Ce projet a pour objectif d'évaluer et de comparer les temps d'exécution de différentes approches de traitement de données (locales et distribuées) sur un cas d'usage classique : le comptage de mots (Word Count). L'étude illustre les défis du traitement Big Data et l'impact de l'architecture choisie face à l'augmentation du volume de données.

## Génération des données
Le script `generer_textes.py` a été utilisé pour créer le jeu de données.
* **Fichiers générés :** Quatre fichiers de test de tailles variables (de 100 lignes à 50 millions de lignes).
* **Vocabulaire :** Restreint à 5 mots ("chat", "voiture", "maison", "chien", "arbre").
* **Méthode :** Duplication de blocs de texte pour simuler une montée en charge rapide et contrôlée.

## Méthodes évaluées et Résultats

Le tableau ci-dessous résume les performances obtenues sur le plus gros fichier généré (**50 millions de lignes**) :

| Méthode de traitement | Temps d'exécution | Analyse des performances |
| :--- | :--- | :--- |
| **1. Python Séquentiel** | **7,6 s** | Offre d'excellents temps d'exécution sur ce volume de données. Limite : l'approche n'est pas scalable et saturera la mémoire (RAM) sur des fichiers de taille Big Data (Go/To). |
| **2. PySpark** | **8,71 s** | Méthode distribuée la plus performante. PySpark optimise le traitement en conservant les données en mémoire vive (RAM) via les DataFrames, ce qui réduit drastiquement les accès disque. |
| **3. Python Pseudo-MapReduce** | **23,3 s** | Méthode locale simulant le paradigme MapReduce. Bien plus lente en pratique que l'approche séquentielle classique en raison de la surcharge liée à la séparation des tâches. |
| **4. Hadoop MapReduce** | **25,5 s** | Méthode la plus lente sur ce volume. Les performances sont pénalisées par la latence au démarrage du cluster et par l'écriture systématique des résultats intermédiaires sur le disque dur entre les étapes Map et Reduce. |

## Conclusion
Pour un volume de données modéré (50 millions de lignes de 5 mots), l'approche séquentielle classique reste la plus rapide car elle s'exécute intégralement en mémoire locale sans surcharge de framework. 

Dans l'écosystème distribué, **PySpark** surpasse largement **Hadoop MapReduce**. Le jeu de données utilisé n'est pas assez massif pour compenser la lourdeur d'Hadoop (latence réseau et I/O disque). PySpark démontre ici toute la force de son traitement *in-memory*.

## Instructions d'exécution

*Prérequis : Python 3.x, environnement Hadoop configuré, PySpark installé.*

1. **Générer les données :**
   ```bash
   python generer_textes.py

2 **Lancer les scripts d'analyse**

Adapter selon le nom exact de vos fichiers :

```bash
# Exemple pour le mode séquentiel
python count_sequential.py

# Exemple pour PySpark
spark-submit count_pyspark.py
```
