
# 🧠 Projet Quizz - Générateur de Quizz Dynamique

Ce projet a été développé dans le cadre de ma formation en Data chez [Jedha Bootcamp](https://www.jedha.co/) pour **mettre en valeur mes compétences Python**.  
Il s'agit d'une application en ligne de commande qui génère des quizz personnalisés à partir d'une API publique selon les critères de l'utilisateur.

---

## 🎯 Objectifs pédagogiques

- Améliorer mes compétences en **programmation Python**
- Appliquer la **programmation orientée objet (POO)**
- Utiliser un **webscraper/API handler** pour construire dynamiquement des requêtes
- Gérer la **logique de quizz** avec score, validation, et suivi
- Organiser un projet avec une **structure propre et professionnelle**
- Préparer le terrain pour une potentielle version web (Flask/FastAPI)

---

## 🌐 API utilisée

Ce projet utilise l'API gratuite de [Open Trivia Database (OpenTDB)](https://opentdb.com/).

### Exemple d'URL :
```
https://opentdb.com/api.php?amount=5&category=18&difficulty=medium&type=multiple
```

- `amount` : nombre de questions
- `category` : thème (science, sport, etc.)
- `difficulty` : easy / medium / hard
- `type` : multiple choix ou vrai/faux

---

## ⚙️ Structure du projet

```
quiz_project/
├── app/
│   ├── __init__.py            # Package principal
│   ├── webscraper.py          # class WebScraper: construit et gère les requêtes API
│   ├── quiz_manager.py        # class QuizManager: logique de jeu, vérif des réponses
│   ├── user_interface.py      # class CLIInterface: interaction utilisateur
│   └── utils.py               # Fonctions utilitaires (ex: nettoyage HTML)
│
│
├── tests/
│   ├── test_api_handler.py
│   ├── test_quiz_manager.py
│   └── test_user_input.py
│
├── main.py                    # Point d'entrée du programme
├── requirements.txt           # Dépendances du projet
└── README.md                  # Fichier de documentation
```
---

## 🛠️ Technologies

- Python 3.x
- [OpenTDB API](https://opentdb.com/)
- POO (Programmation Orientée Objet)
- Web scraping léger
- Markdown pour la doc
- Organisation modulaire de projet

---

## 👨‍💻 Auteur
Hamza Ichkhakh
Projet réalisé dans le cadre de la formation **Fullstack & Lead Data chez Jedha Bootcamp**.

📎 GitHub : [https://github.com/Ichkhakh/jedha-data-bootcamps] [fullstack/01_python_programming]


---

## 📌 À venir

- Version web avec Flask ou FastAPI
- Ajout d'un timer par question
- Sauvegarde des scores et leaderboard
