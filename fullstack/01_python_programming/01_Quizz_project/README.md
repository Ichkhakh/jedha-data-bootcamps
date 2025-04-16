
# 🧠 Quiz Project – Dynamic Quiz Generator

This project was developed as part of my Data training at [Jedha Bootcamp](https://www.jedha.co/) to **demonstrate my Python skills**.  
It is a command-line application that generates customized quizzes using a public API based on user-selected parameters.

---

## 🎯 Learning Objectives

- Improve my skills in **Python programming**
- Apply **Object-Oriented Programming (OOP)**
- Use a **webscraper/API handler** to dynamically build queries
- Handle the **quiz logic**, including scoring and answer validation
- Organize the project with a **clean, modular architecture**
- Lay the groundwork for a future **web version (Flask/FastAPI)**

---

## 🌐 API Used

This project uses the free API from [Open Trivia Database (OpenTDB)](https://opentdb.com/).

### Example URL:
```
https://opentdb.com/api.php?amount=5&category=18&difficulty=medium&type=multiple
```

- `amount`: number of questions
- `category`: quiz category (science, sports, etc.)
- `difficulty`: easy / medium / hard
- `type`: multiple choice or true/false

---

## ⚙️ Project Structure

```
quiz_project/
├── app/
│   ├── __init__.py            # Package initializer
│   ├── webscraper.py          # WebScraper class: builds and manages API requests
│   ├── quiz_manager.py        # QuizManager class: handles game logic and scoring
│   ├── user_interface.py      # CLIInterface class: user interaction logic
│   └── utils.py               # Utility functions (e.g., HTML decoding)
│
├── tests/
│   ├── test_api_handler.py
│   ├── test_quiz_manager.py
│   └── test_user_input.py
│
├── main.py                    # Entry point of the program
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 🛠️ Technologies

- Python 3.x
- [OpenTDB API](https://opentdb.com/)
- Object-Oriented Programming (OOP)
- Light web scraping
- Markdown for documentation
- Modular Python project architecture

---

## 👨‍💻 Author
**Hamza Ichkhakh**  
This project was created as part of the **Fullstack & Lead Data program at Jedha Bootcamp**.

📎 GitHub: [https://github.com/Ichkhakh/jedha-data-bootcamps](https://github.com/Ichkhakh/jedha-data-bootcamps)  
🗂️ Folder: `fullstack/01_python_programming/01_Quizz_project`

---

## 📌 Coming Soon

- Web version using Flask or FastAPI
- Timer per question
- Score saving and leaderboard
