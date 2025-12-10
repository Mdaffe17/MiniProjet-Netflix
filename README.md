# Mini Projet Netflix – Analyse Exploratoire & Application Streamlit

Ce projet a été réalisé dans le cadre du cours d'initiation à la Data Science.  
L’objectif est de mener une **analyse exploratoire complète (EDA)** du dataset *Netflix Titles* et de proposer une **application web interactive** permettant d’explorer les données grâce à **Streamlit**.

---

## Accès à l'application Streamlit

Cliquez ici pour accéder à l'application en ligne :  
 https://miniprojet-netflix-etypknyhqd2n7vzfcfj8gr.streamlit.app


---

## Description du projet

Le dataset utilisé provient de Kaggle :  
**Netflix Movies and TV Shows Dataset**

Il contient des informations sur les films et séries présents sur Netflix :
- Titre  
- Type (Movie / TV Show)  
- Réalisateur, casting  
- Pays d’origine  
- Date d’ajout  
- Année de sortie  
- Classification (rating)  
- Genres (listed_in)  
- Description  

---

## Étapes de l'analyse (EDA)

L’analyse inclut :

###  1. Exploration initiale
- Dimensions du dataset  
- Types de données  
- Valeurs manquantes  
- Nettoyage des colonnes texte  

###  2. Nettoyage
- Correction du format des dates (`date_added`)  
- Extraction de l’année et du mois d’ajout  
- Normalisation du pays principal  
- Gestion des genres (explosion de la colonne `listed_in`)  
- Transformation des durées :
  - Films → `duration_min`
  - Séries → `seasons`

###  3. Visualisations
Différents graphiques (Matplotlib, Seaborn, Plotly) :

- Répartition des films vs séries  
- Nombre de titres par année de sortie  
- Durée des films  
- Nombre de saisons (TV Shows)  
- Top 10 des genres  
- Répartition des ratings  
- Distribution temporelle des ajouts Netflix  

###  4. Conclusion
# Conclusion

Dans ce mini-projet, nous avons réalisé une analyse exploratoire du catalogue Netflix à partir d'un jeu de données public Kaggle.  
Les principaux résultats sont :

- Netflix propose **plus de films que de séries**, mais le nombre de séries a fortement augmenté après 2015.
- La majorité des contenus sont **récents**, avec une forte concentration à partir des années 2000.
- Les **États-Unis** dominent le catalogue en nombre de titres, mais de nombreux autres pays sont représentés, ce qui montre une certaine diversité géographique.
- Les genres les plus fréquents incluent notamment *International Movies*, *Dramas*, *Comedies*, etc.
- Les ratings les plus courants sont **TV-MA**, **TV-14** et **TV-PG**, suggérant une offre large pour un public adolescent / adulte.
- Les films ont une durée typique comprise entre **80 et 120 minutes**, tandis que la majorité des séries comptent peu de saisons (1 à 3).

Nous avons également mis en évidence certaines **limites** :
- Le dataset ne contient pas d'information sur la popularité réelle (nombre de vues, notes des utilisateurs, etc.).
- Les dates d'ajout sont parfois manquantes ou partielles.
- Certaines colonnes textuelles (cast, listed_in, country) sont difficiles à exploiter pleinement sans un prétraitement plus avancé (NLP, regroupement de catégories, etc.).

Ces analyses constituent une bonne base pour de futurs travaux, par exemple :
- la recommandation de contenus,
- la prédiction de succès d'un titre,
- ou l'étude plus fine des préférences par pays.


---

##  Application Streamlit

L’application web interactive permet :

- d’afficher le dataset  
- de filtrer selon plusieurs critères  
- de visualiser :
  - histogrammes interactifs  
  - distributions par type  
  - top genres  
  - ratings  
  - années d’ajout  

L’app est accessible directement en ligne (voir lien plus haut).

---

## Structure du projet
MiniProjet-Netflix/
│── data/
│ └── netflix_titles.csv
│
│── notebook/
│ └── netflix_eda.ipynb
│
│── streamlit/
│ └── app.py
│
│── report/
│ └── rapport.pdf (si fourni)
│
│── requirements.txt
│── README.md

## Technologies utilisées

- **Python 3**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Plotly**
- **Streamlit**

---

##  Installation locale pour tester 

### 1. Cloner le dépôt
```bash
git clone https://github.com/Mdaffe17/MiniProjet-Netflix
cd miniprojet-netflix
### 2. Installer les dépendances
```bash
pip install -r requirements.txt
### 3. Lancer Streamlit
```bash
cd streamlit
streamlit run app.py

## Auteur
Projet réalisé par Mouctar Daffe dans le cadre du module d’analyse de données.