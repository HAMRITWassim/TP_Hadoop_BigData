# TP2 : Analyse des Accidents de la Route avec PySpark

- **Auteur :** HAMRIT Wassim (5A FISE)

Ce projet présente une analyse de données massives concernant les accidents de la route en Australie-Méridionale entre 2012 et 2019, fournie par le DPTI. L'objectif principal est d'exploiter le framework Apache Spark pour interroger et manipuler ces données en comparant deux approches : l'API RDD (bas niveau) et l'API DataFrame (haut niveau).

## Données utilisées

- Fichiers CSV recensant les unités/véhicules impliqués (`units_data`).
- Fichiers CSV détaillant les caractéristiques des accidents (`crash_data`).

## Pipeline d'analyse et de modélisation

### Manipulation de base et partitionnement (API RDD)

- Chargement des fichiers textuels et nettoyage initial : suppression des en-têtes.
- Création d'un partitionnement personnalisé pour optimiser les traitements : les données sont divisées en deux partitions distinctes, une pour les véhicules d'Australie-Méridionale (« SA ») et une pour les autres États.
- Calculs statistiques de base :
  - détermination de l'âge moyen des conducteurs impliqués : 40,8 ans pour les hommes et 40,08 ans pour les femmes ;
  - identification des années de fabrication des véhicules extrêmes, du plus ancien datant de 1900 au plus récent de 2019.

### Exploration avancée et jointures (API DataFrame)

- Analyse des localisations et de la gravité :
  - extraction des accidents à Adélaïde causant plus de 3 victimes ;
  - identification des 10 accidents les plus graves toutes zones confondues.
- Agrégation des données meurtrières :
  - décompte du nombre de décès par type d'accident ;
  - révélation que les collisions avec des objets fixes (« Hit Fixed Object ») sont de loin les plus mortelles, avec 245 décès.
- Jointure entre les tables `crash_df` et `units_df` pour lier les accidents aux conducteurs :
  - identification des banlieues avec le plus de victimes causées par des conducteurs sans permis ;
  - Adélaïde étant en première position.

### Analyse d'impact : alcool et drogues

- Croisement de la présence de substances (alcool, drogues, les deux, ou aucune) avec la sévérité des accidents (`CSEF Severity`) via des calculs de pourcentages.
- Conclusion frappante :
  - la proportion d'accidents fatals bondit à 13,09 % lorsque le conducteur combine alcool et drogues, contre un infime 0,42 % pour les conducteurs à jeun ;
  - en l'absence de substances, la grande majorité des accidents (67,49 %) se limitent à de simples dégâts matériels (`1: PDO`).
- Conversion du DataFrame PySpark final en DataFrame Pandas afin de générer une visualisation, sous forme de graphique en barres avec Matplotlib, illustrant ces corrélations.
