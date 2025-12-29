import streamlit as st

st.set_page_config(page_title="Mohamed Taïb SBIHI — CV", page_icon="🧩", layout="wide")

CSS = """
<style>
.block-container {padding-top: 2.2rem; padding-bottom: 2.2rem; max-width: 1180px;}
h1, h2, h3 {letter-spacing: -0.02em;}
.small {opacity: .78; font-size: 0.95rem;}
.kpi {border: 1px solid rgba(255,255,255,.10); border-radius: 18px; padding: 14px 16px;}
.card {border: 1px solid rgba(255,255,255,.10); border-radius: 18px; padding: 18px 18px; background: rgba(255,255,255,.02);}
.tag {display:inline-block; padding: 6px 10px; border: 1px solid rgba(255,255,255,.14); border-radius: 999px; margin: 4px 6px 0 0; font-size: .92rem; opacity: .9;}
hr {border: none; height: 1px; background: rgba(255,255,255,.10); margin: 18px 0;}
a {text-decoration: none;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

NAME = "Mohamed Taïb SBIHI"
TITLE = "Bachelor Marketing Digital & Data — 3ème année"
GOAL = "Étudiant en marketing digital orienté data, analyse de performance et outils digitaux."
CITY = "Paris / Île-de-France"
PHONE = "+33 7 66 10 58 56"
EMAIL = "taibsbihi1@gmail.com"

SKILLS = {
    "Data & Marketing analytics": ["Google Analytics", "Buffer", "Iconosquare"],
    "Data viz": ["Looker Studio"],
    "Dev": ["Python", "JavaScript", "HTML", "CSS"],
    "IA & Création": ["ChatGPT", "Midjourney", "Canva"],
    "Bureautique": ["Word", "Excel"],
}

LANGS = [("Français", "Bilingue"), ("Anglais", "C1"), ("Arabe", "Langue natale")]
SOFT = ["Esprit d’équipe", "Organisation", "Créativité", "Autonomie"]

EXPERIENCES = [
    {
        "role": "Chef de Projet Marketing Digital B2B (Stage)",
        "org": "Froidel",
        "when": "01/06/2024 → 01/08/2024",
        "points": [
            "Gestion des réseaux sociaux (LinkedIn, Facebook) pour cibler des clients professionnels en B2B",
            "Participation à la refonte complète du site web",
        ],
        "tags": ["B2B", "Social media", "Website"],
    },
    {
        "role": "Chef de projet Marketing & Évènementiel Digital (Stage)",
        "org": "Pôle Marketing du Morocco Mall",
        "when": "01/06/2023 → 01/08/2023",
        "points": [
            "Gestion des réseaux sociaux (Instagram)",
            "Participation à la coordination d’événements promotionnels",
            "Conception et mise en œuvre de l’évènement estival du centre commercial",
        ],
        "tags": ["Événementiel", "Instagram", "Coordination"],
    },
    {
        "role": "Conseiller Commercial (Stage)",
        "org": "Fnac",
        "when": "Avril 2018 (1 semaine)",
        "points": [
            "Aide à la vente et conseil client en magasin",
        ],
        "tags": ["Vente", "Relation client"],
    },
]

PROJECTS = [
    {
        "name": "Favorite Skin Picker",
        "type": "Projet personnel",
        "when": "2023 → 2024",
        "desc": "Site interactif permettant de sélectionner un personnage League of Legends à partir d’une base dynamique, avec génération de scripts assistée par IA.",
        "stack": ["JavaScript", "HTML", "CSS", "IA"],
    },
    {
        "name": "Analyse d’un jeu de données avec l’IA",
        "type": "Projet académique",
        "when": "1ère année",
        "desc": "Exploration et analyse d’un dataset avec une approche assistée par intelligence artificielle.",
        "stack": ["Analyse", "Data", "IA"],
    },
    {
        "name": "Stratégie marketing — méthode AARRR",
        "type": "Projet académique",
        "when": "2ème année",
        "desc": "Construction d’une stratégie marketing basée sur le framework AARRR.",
        "stack": ["Marketing", "AARRR", "Stratégie"],
    },
]

EDU = [
    {
        "school": "EFREI PARIS",
        "degree": "Bachelor en Ingénierie Marketing Digital",
        "details": "Data science, data analyse, data visualisation, IA, marketing digital, SEO/SEA",
    },
    {
        "
