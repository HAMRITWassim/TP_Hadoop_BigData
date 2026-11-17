# TPs Big Data

## TP1 : Analyse des performances de comptage de mots (Word Count)
Ce projet a pour objectif d'évaluer et de comparer les temps d'exécution de différentes approches de traitement de données (locales et distribuées) sur un cas d'usage classique : le comptage de mots (Word Count). L'étude illustre les défis du traitement Big Data et l'impact de l'architecture choisie face à l'augmentation du volume de données.

## TP2 : Analyse des Accidents de la Route avec PySpark

Ce projet présente une analyse de données massives concernant les accidents de la route en Australie-Méridionale entre 2012 et 2019, fournie par le DPTI. L'objectif principal est d'exploiter le framework Apache Spark pour interroger et manipuler ces données en comparant deux approches : l'API RDD (bas niveau) et l'API DataFrame (haut niveau).

## TP3 : Systèmes de Recommandation (Adaptation de projets Kaggle au pipeline Data Science)
L'objectif de ce TP est d'exploiter des jeux de données et des notebooks issus de Kaggle afin de se les approprier, de corriger leurs limites et de les restructurer selon un pipeline complet (**Data → EDA → Prétraitement → Transformation → ML → Évaluation**) :
- **Partie Small (Animes — Scikit-learn) :** Adaptation en local d'un système de recommandation par clustering de profils utilisateurs (PCA + K-Means) sur un dataset de 7,8 millions de notes.
- **Partie Big (Jeux Steam — PySpark) :** Passage à l'échelle sur un dataset massif (~2 Go, plus de 40 millions d'avis) via un filtrage collaboratif distribué par factorisation de matrices (**ALS** avec PySpark MLlib).
