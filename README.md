# 💰 Prédiction d'Éligibilité à un Prêt Bancaire

Ce projet consiste en une **application web** qui prédit si un client est éligible à un **prêt bancaire**, sur la base de ses données personnelles. Il repose sur un **modèle de régression linéaire** développé après une analyse exploratoire complète des données.

## 🎯 Objectif

Permettre aux banques ou institutions financières de **filtrer automatiquement les demandes de prêt**, en estimant si un client peut potentiellement obtenir un crédit, grâce à une approche **data-driven**.

## 🛠️ Technologies utilisées

- Python, Pandas, NumPy  
- Scikit-learn (modèle de régression)  
- Jupyter Notebook (EDA et modélisation)  
- Streamlit / Flask (application web)  
- Matplotlib / Seaborn (visualisations)

## 📊 Fonctionnalités

- Analyse exploratoire des données clients  
- Prétraitement des données (nettoyage, encodage, scaling)  
- Modélisation par régression linéaire  
- Interface simple pour saisir les données d’un client  
- Prédiction en temps réel : **"Prêt accordé" ou "Prêt refusé"**

## 📁 Structure du projet

```
├── data/                # Données brutes et nettoyées
├── notebooks/           # Analyse exploratoire et modèle ML
├── app/                 # Code de l'application web
├── requirements.txt     # Dépendances Python
└── README.md            # Ce fichier
```

## 🚀 Lancer l'application

1. Cloner le dépôt :
```bash
git clone https://github.com/ton-utilisateur/nom-du-repo.git
cd nom-du-repo
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancer l'application (par exemple avec Streamlit) :
```bash
streamlit run main_credit.py
```
