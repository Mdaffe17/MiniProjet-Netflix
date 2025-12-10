import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("../data/netflix_titles.csv")

    # Nettoyage de la date_added (corrige l'erreur !)
    df["date_added"] = (
        df["date_added"]
        .astype(str)
        .str.strip()
    )
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # Colonnes dérivées
    df["year_added"] = df["date_added"].dt.year
    df["main_country"] = df["country"].fillna("Inconnu").str.split(",").str[0].str.strip()

    return df


df = load_data()

st.set_page_config(page_title="Analyse Netflix – Mini Projet", layout="wide")
st.title("Analyse exploratoire du catalogue Netflix")

st.markdown("""
Application Streamlit pour le mini-projet 8PRO408 – Analyse des contenus Netflix.
""")

# ---- Sidebar ----
st.sidebar.header("Filtres")

type_filter = st.sidebar.multiselect(
    "Type de contenu",
    options=sorted(df["type"].unique()),
    default=list(df["type"].unique())
)

country_filter = st.sidebar.multiselect(
    "Pays principal",
    options=sorted(df["main_country"].unique()),
    default=[]
)

year_min, year_max = int(df["release_year"].min()), int(df["release_year"].max())
year_range = st.sidebar.slider(
    "Année de sortie",
    min_value=year_min,
    max_value=year_max,
    value=(2000, year_max)
)

df_filtered = df[df["type"].isin(type_filter)]
df_filtered = df_filtered[
    (df_filtered["release_year"] >= year_range[0]) &
    (df_filtered["release_year"] <= year_range[1])
]

if country_filter:
    df_filtered = df_filtered[df_filtered["main_country"].isin(country_filter)]

st.subheader("Aperçu des données filtrées")
st.write(f"Nombre de titres affichés : {len(df_filtered)}")
st.dataframe(df_filtered[["title", "type", "main_country", "release_year", "rating", "listed_in"]].head(50))

# ---- Colonne 1 : Films vs Séries par année ----
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Évolution du nombre de titres par année de sortie")
    df_year = (
        df_filtered.groupby(["release_year", "type"])["show_id"]
        .count()
        .reset_index(name="count")
    )
    fig_year = px.line(
        df_year,
        x="release_year",
        y="count",
        color="type",
        markers=True,
        labels={"release_year": "Année de sortie", "count": "Nombre de titres"},
        title="Films vs Séries par année de sortie"
    )
    st.plotly_chart(fig_year, use_container_width=True)

with col2:
    st.markdown("### Top pays représentés")
    top_countries = (
        df_filtered["main_country"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    top_countries.columns = ["country", "count"]
    fig_countries = px.bar(
        top_countries,
        x="country",
        y="count",
        title="Top 10 des pays (après filtres)",
        labels={"country": "Pays", "count": "Nombre de titres"}
    )
    fig_countries.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_countries, use_container_width=True)

# ---- Genres ----
st.markdown("### Genres les plus fréquents")

genres_series = (
    df_filtered["listed_in"]
    .fillna("Inconnu")
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = (
    genres_series.value_counts()
    .head(15)
    .reset_index()
)
top_genres.columns = ["genre", "count"]

fig_genres = px.bar(
    top_genres,
    x="genre",
    y="count",
    title="Top 15 des genres",
    labels={"genre": "Genre", "count": "Nombre de titres"}
)
fig_genres.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_genres, use_container_width=True)

# ---- Ratings ----
st.markdown("### Répartition des ratings")

rating_counts = (
    df_filtered["rating"]
    .fillna("Inconnu")
    .value_counts()
    .reset_index()
)
rating_counts.columns = ["rating", "count"]

fig_ratings = px.bar(
    rating_counts,
    x="rating",
    y="count",
    title="Répartition des ratings (classification d'âge)",
    labels={"rating": "Rating", "count": "Nombre de titres"}
)
fig_ratings.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_ratings, use_container_width=True)

st.markdown("---")
st.markdown("Mini-projet 8PRO408 – Analyse des contenus Netflix")
