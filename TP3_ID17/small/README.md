# TP3_17 Small : Système de Recommandation d'Animes par Clustering d'Utilisateurs

- **Auteur :** HAMRIT Wassim (5A FISE)
- **Technologies :** Python 3.9+, Pandas, NumPy, Scikit-learn, Matplotlib, Jupyter Notebook

Ce projet implémente et analyse un système de recommandation d'animes basé sur le clustering de profils utilisateurs (K-Means). L'objectif est de combiner les notes attribuées par les utilisateurs et les métadonnées des animes (genres et formats) afin de regrouper les spectateurs aux goûts similaires et de leur proposer des recommandations pertinentes.

---

## 1. État d'exécution du notebook

- **État du notebook d'origine :** Incomplet sur plusieurs étapes du pipeline (`EDA`, critère de validation du clustering, `Evaluation`).
- **État du notebook rendu :** **Entièrement corrigé, complété et fonctionnel**.

---

## 2. Problèmes rencontrés et résolutions

- **Incompatibilité de types lors de l'encodage One-Hot (Pandas ≥ 2.0) :** Le code initial insérait des `np.nan` dans le résultat booléen de `pd.get_dummies(anime2['type'])`, générant des colonnes de type `object` (ou une `TypeError` sous Pandas 3) lors du calcul des moyennes par utilisateur.  
  *Résolution :* Forçage explicite du type numérique dès l'encodage (`dtype=float`) et conversion des colonnes d'attributs en `float`.
- **Style Matplotlib déprécié :** L'appel à `plt.style.use('seaborn')` provoquait une erreur d'exécution avec les versions récentes de Matplotlib (≥ 3.6).  
  *Résolution :* Remplacement par `plt.style.use('seaborn-v0_8')`.
- **Paramètre obsolète et non-reproductibilité dans K-Means (Scikit-learn ≥ 1.0) :** L'argument `n_jobs` a été supprimé de `KMeans`, faisant planter l'exécution, et aucun `random_state` n'était défini.  
  *Résolution :* Suppression du paramètre `n_jobs` et ajout d'un `random_state` fixe.
- **Choix du nombre de clusters `k` incomplet et coûteux :** Dans la boucle d'origine, la liste `scores = []` était initialisée mais jamais remplie, et la seule courbe d'inertie (méthode du coude) restait trop ambiguë.  
  *Résolution :* Implémentation du **score de silhouette** en complément de l'inertie, évalué sur un **échantillon de 10 000 utilisateurs** pour éviter un temps d'exécution trop long.
- **Forte proportion de notes `-1` (18,9 % du jeu de données) :** La valeur `-1` signifie que l'utilisateur a visionné l'anime sans le noter.  
  *Résolution :* Conservation de l'imputation par la note neutre `5` lors de la construction des profils (afin de distinguer un anime vu d'un anime non vu), en prenant soin de relever le biais introduit et le décalage avec l'algorithme de recommandation, qui ignore ces `-1`.
- **Anomalies dans les données brutes :** Détection de 7 doublons `(user_id, anime_id)`, de 10 lignes dans `rating.csv` référençant des `anime_id` absents de `anime.csv`, ainsi que de valeurs manquantes dans `anime.csv` (62 genres, 25 types, 230 notes, 340 épisodes `'Unknown'`).  
  *Résolution :* Suppression des doublons et gestion propre des `NaN` lors de la jointure et de l'agrégation.

---

## 3. Liste des modifications apportées

Le notebook a été restructuré et complété afin de respecter l'intégralité du pipeline **`Data → EDA → Prétraitement → Transformation → ML → Evaluation`** :

1. **Analyse Exploratoire des Données (`EDA` — étape ajoutée) :**
   - Analyse volumétrique : **7 813 737 notes**, **73 515 utilisateurs** et **12 294 animes** (dont 11 200 notés).
   - Quantification des valeurs manquantes, des doublons et de la part de notes `-1` (18,9 %).
   - Visualisations : distribution des notes (hors `-1`), distribution du nombre d'animes vus par utilisateur (échelle logarithmique), répartition des types (`TV`, `Movie`, `OVA`, etc.) et classement des 20 genres les plus fréquents.
2. **Prétraitement des données (`Prétraitement`) :**
   - Suppression des 7 doublons `(user_id, anime_id)` via `drop_duplicates`.
   - Correction de l'encodage One-Hot des 43 genres et 6 types (`dtype=float`).
   - Remplacement des notes `-1` par `5` et agrégation par utilisateur (note moyenne par catégorie, avec `fillna(0)` pour les catégories non visionnées).
3. **Transformation & Réduction de dimensionnalité (`Transformation`) :**
   - Application d'une PCA sur les 49 variables de profil utilisateur.
   - Calcul de l'information conservée : les **20 composantes** retenues conservent **77,5 %** de la variance totale (22 composantes étant nécessaires pour atteindre exactement 80 %).
   - Justification méthodologique des choix du notebook (pertinence de ne pas appliquer de `StandardScaler` sur des notes déjà bornées entre 0 et 10 afin de ne pas amplifier le bruit des genres rares et limites du `fillna(0)`).
4. **Modélisation, Recommandation et Évaluation (`ML` & `Evaluation`) :**
   - Correction et stabilisation de `KMeans`.
   - Analyse de l'inertie (coude) et du score de silhouette pour justifier le choix de `k`.
   - Génération des recommandations par cluster et ajout de l'étape d'évaluation du système.

---

## 4. Informations utiles & Guide d'exécution

### Structure des données attendue
Le notebook charge les fichiers depuis le sous-dossier `./anime_recommendations_dataset/` :
- `./anime_recommendations_dataset/rating.csv` : historique des interactions (`user_id`, `anime_id`, `rating`).
- `./anime_recommendations_dataset/anime.csv` : métadonnées des animes (`anime_id`, `name`, `genre`, `type`, `episodes`, `rating`, `members`).

### Prérequis techniques & Ressources
- **Python 3.9+**
- Installation des dépendances :
  ```bash
  pip install jupyter pandas numpy scikit-learn matplotlib

### Lancer le notebook

1. Cloner ce dépôt et ouvrir le fichier `.ipynb` dans Jupyter Notebook ou VS Code.
2. Exécuter toutes les cellules dans l'ordre.

