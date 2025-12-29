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
GOAL = "À la recherche d’un contrat d’apprentissage (1 an) à partir de Septembre 2025 • Rythme : 2 semaines entreprise / 1 semaine école"
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
            "Participation à la coordination d’événements promotionnels pour augmenter la fréquentation du centre",
            "Conception et mise en œuvre de l’ensemble de l’évènement estival du centre commercial",
        ],
        "tags": ["Événementiel", "Instagram", "Coordination"],
    },
    {
        "role": "Conseiller Commercial (Stage)",
        "org": "Fnac",
        "when": "Avril 2018 (1 semaine)",
        "points": [
            "Aide à la vente en magasin (conseils aux clients, accompagnement)",
        ],
        "tags": ["Vente", "Relation client"],
    },
]

PROJECTS = [
    {
        "name": "Favorite Skin Picker",
        "type": "Projet personnel",
        "when": "2023 → 2024",
        "desc": "Site interactif : sélection d’un personnage League of Legends depuis une base dynamique, avec des ramifications personnalisées, en s’appuyant sur l’IA pour générer des scripts (JS/HTML).",
        "stack": ["JavaScript", "HTML", "CSS", "IA"],
        "link_url": "",
    },
    {
        "name": "Analyse d’un jeu de données avec l’IA",
        "type": "Projet académique",
        "when": "1ère année",
        "desc": "Exploration et analyse d’un dataset avec une approche assistée par IA (nettoyage, interprétation, restitution).",
        "stack": ["Analyse", "Data", "IA"],
        "link_url": "",
    },
    {
        "name": "Stratégie marketing — méthode AARRR",
        "type": "Projet académique",
        "when": "2ème année (2023–2024)",
        "desc": "Élaboration d’une stratégie marketing structurée via le framework AARRR (Acquisition, Activation, Rétention, Revenu, Recommandation).",
        "stack": ["Marketing", "AARRR", "Stratégie"],
        "link_url": "",
    },
]

EDU = [
    {
        "school": "EFREI PARIS",
        "degree": "Bachelor en Ingénierie Marketing Digital",
        "details": "Data science, data analyse, data visualisation, data marketing, IA, neurosciences, développement informatique, marketing digital, E-business, SEO/SEA",
    },
    {
        "school": "Université Paris 1 Panthéon-Sorbonne",
        "degree": "Licence 1 — Économie",
        "details": "Mathématiques appliquées à l’économie, statistiques",
    },
    {
        "school": "Collège-Lycée Léon l’Africain (Casablanca)",
        "degree": "Baccalauréat Général AEFE",
        "details": "Spécialités Mathématiques et Physique-chimie",
    },
]

def pill_tags(tags):
    if not tags:
        return
    st.markdown("".join([f"<span class='tag'>{t}</span>" for t in tags]), unsafe_allow_html=True)

def section_header(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"<div class='small'>{subtitle}</div>", unsafe_allow_html=True)
    st.write("")

# --- Header ---
left, right = st.columns([2.6, 1.4], vertical_alignment="center")
with left:
    st.title(NAME)
    st.markdown(f"**{TITLE}**")
    st.markdown(f"<div class='small'>{GOAL}</div>", unsafe_allow_html=True)
with right:
    st.markdown(
        f"""
        <div class="kpi">
            <div><b>📍</b> {CITY}</div>
            <div><b>✉️</b> {EMAIL}</div>
            <div><b>📞</b> {PHONE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr/>", unsafe_allow_html=True)

# --- Sidebar navigation ---
pages = ["Profil", "Expériences", "Projets", "Compétences", "Formation", "Langues"]
page = st.sidebar.radio("Navigation", pages)

if page == "Profil":
    section_header("Profil")
    st.markdown(
        """
        <div class="card">
            Étudiant en <b>Marketing Digital & Data</b>, je m’intéresse à l’analyse de données appliquée au marketing,
            à l’optimisation de la performance (acquisition, conversion, rétention) et aux outils digitaux.
            J’aime construire des supports clairs (reporting, dashboards, contenus) et exécuter des projets concrets.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><b>🎯 Cible</b><br/>Marketing digital / Data marketing</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><b>🗓️ Disponibilité</b><br/>Septembre 2025 • 1 an</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><b>🔁 Rythme</b><br/>2 semaines / 1 semaine</div>', unsafe_allow_html=True)

elif page == "Expériences":
    section_header("Expériences")
    for exp in EXPERIENCES:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap;">
                        <div>
                            <div style="font-size:1.08rem;"><b>{exp["role"]}</b></div>
                            <div class="small">{exp["org"]}</div>
                        </div>
                        <div class="small" style="white-space:nowrap;">{exp["when"]}</div>
                    </div>
                    <div style="margin-top:10px;">
                        {"".join([f"<div>• {p}</div>" for p in exp["points"]])}
                    </div>
                    <div style="margin-top:10px;">
                        {"".join([f"<span class='tag'>{t}</span>" for t in exp.get("tags", [])])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")

elif page == "Projets":
    section_header("Projets")
    filt = st.multiselect("Filtrer par mot-clé", sorted({t for p in PROJECTS for t in p["stack"]}))
    for p in PROJECTS:
        if filt and not set(filt).intersection(set(p["stack"])):
            continue
        st.markdown(
            f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap;">
                    <div>
                        <div style="font-size:1.08rem;"><b>{p["name"]}</b> <span class="small">• {p["type"]}</span></div>
                        <div class="small">{p["when"]}</div>
                    </div>
                </div>
                <div style="margin-top:10px;">{p["desc"]}</div>
                <div style="margin-top:10px;">
                    {"".join([f"<span class='tag'>{t}</span>" for t in p["stack"]])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")

elif page == "Compétences":
    section_header("Compétences")
    for cat, items in SKILLS.items():
        st.markdown(f"### {cat}")
        st.markdown("".join([f"<span class='tag'>{x}</span>" for x in items]), unsafe_allow_html=True)
        st.write("")

    st.markdown("### Soft skills")
    st.markdown("".join([f"<span class='tag'>{x}</span>" for x in SOFT]), unsafe_allow_html=True)

elif page == "Formation":
    section_header("Formation")
    for e in EDU:
        st.markdown(
            f"""
            <div class="card">
                <div style="font-size:1.06rem;"><b>{e["degree"]}</b></div>
                <div class="small">{e["school"]}</div>
                <div style="margin-top:10px;" class="small">{e["details"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")

elif page == "Langues":
    section_header("Langues")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    for lang, lvl in LANGS:
        st.markdown(f"**{lang}** — {lvl}")
    st.markdown("</div>", unsafe_allow_html=True)

