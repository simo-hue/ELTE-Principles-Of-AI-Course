# 🤖 ELTE Principles of AI — Course Materials & Study Resources

![University](https://img.shields.io/badge/University-ELTE_Budapest-0065BD?style=for-the-badge&logo=academia&logoColor=white)
![Program](https://img.shields.io/badge/Program-EIT_Digital_MSc_(AUSIR)-blueviolet?style=for-the-badge)
![Semester](https://img.shields.io/badge/Semester-2026%2F2027_Fall-brightgreen?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/Framework-TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Credits](https://img.shields.io/badge/Credits-6_ECTS-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-lightgrey?style=for-the-badge)

> **The most comprehensive open-source study resource for the Principles of AI course at [Eötvös Loránd University (ELTE)](https://www.elte.hu/en/), Budapest.**
> Labs, exercises, game AI implementations, NLP experiments, and neural network projects — all in one place.

---

## 📖 Table of Contents

- [About the Course](#-about-the-course)
- [Topics Covered](#-topics-covered)
- [Grading & Assessment](#-grading--assessment)
- [Repository Structure](#-repository-structure)
- [Progress Tracker](#-progress-tracker)
- [Tech Stack & Prerequisites](#-tech-stack--prerequisites)
- [External Resources](#-external-resources)
- [Disclaimer](#%EF%B8%8F-disclaimer)

---

## 📚 About the Course

| Detail | Info |
|---|---|
| **Course Name** | Principles of Artificial Intelligence (PAI) |
| **University** | Eötvös Loránd University (ELTE), Budapest, Hungary |
| **Faculty** | Faculty of Informatics |
| **Program** | EIT Digital Master School (AUSIR — Autonomous Systems) |
| **Semester** | 2026/2027 — 1st Semester (Fall) |
| **Credits** | 6 ECTS |
| **Textbook** | S. Russell, P. Norvig: *Artificial Intelligence. A Modern Approach.* |
| **Lectures** | Asynchronous online (weekly video lectures + quizzes) |
| **Practices** | In-person at the university |
| **Communication** | Teams group PAI 2026 (join code: `313droy`) |

This course provides a **broad introduction to Artificial Intelligence**, spanning both classic AI algorithms and modern machine learning. The first half covers fundamental AI techniques — backtracking, graph search, and minimax — applied to game AI. The second half transitions to machine learning, including deep learning and unsupervised learning through natural language processing applications.

**Key distinction**: Lectures are **asynchronous online** (watch video lectures weekly, then complete quizzes), while practices are **in-person** at the university.

---

## 🧠 Topics Covered

### Classic AI Algorithms
- **Backtracking** — Constraint satisfaction, search space exploration
- **Graph Search** — BFS, DFS, A* search, heuristic functions
- **Minimax Algorithm** — Game trees, adversarial search, alpha-beta pruning
- **Game AI** — Practical implementations for board games, maze solving, pathfinding

### Machine Learning & Deep Learning
- **Introduction to Machine Learning** — Supervised vs. unsupervised learning fundamentals
- **Deep Learning** — Neural network architectures, training, optimization
- **Neural Network Implementation** — Hands-on implementation for various tasks
- **Natural Language Processing (NLP)** — Text processing, word embeddings, language models
- **Unsupervised Learning** — Clustering, dimensionality reduction through NLP applications

---

## 📊 Grading & Assessment

### Point Breakdown (Total: 60 points)

| Component | Points | Details |
|---|---|---|
| **Lecture Quizzes** | 10 pts | Weekly quizzes (5 questions each). Perfect score (5/5) = +1 point, max 10 total. Unlimited attempts. Due by midnight before the next lecture. |
| **Practice Exercises** | 18 pts | 6 graded practices × 3 points each. Can be completed in class or submitted at home before next practice. |
| **Assignments** | 12 pts | 1 smaller assignment (3 pts) + 1 larger assignment with in-person presentation (9 pts). |
| **Final Exam** | 20 pts | In-person, during exam period (January). |

### Grade Thresholds

| Points | Grade |
|---|---|
| 50 – 60 | **5** (Excellent) |
| 40 – 49 | **4** (Good) |
| 30 – 39 | **3** (Satisfactory) |
| 20 – 29 | **2** (Pass) |
| 0 – 19 | **1** (Fail) |

> ⚠️ **Important**: The final exam is **in-person** at the university during the exam period in January. Plan your travel accordingly.

---

## 📂 Repository Structure

```
ELTE-Principles-Of-AI-Course/
├── README.md
├── LAB/
│   ├── __init__.py                      # Package initialization
│   ├── pixi.toml                        # Pixi package manager configuration
│   ├── pixi.lock                        # Dependency lock file
│   ├── 1/                               # Lab 1 — Python Fundamentals
│   │   ├── 01 - Python.ipynb            # Python basics notebook
│   │   ├── 02 - Python.ipynb            # Advanced Python notebook
│   │   ├── lambda.py                    # Lambda function exercises
│   │   ├── lambda_2.py                  # Lambda pattern matching
│   │   ├── lambda_3.py                  # Functional programming exercises
│   │   └── lambda_4.py                  # Lambda compositions
│   ├── framework/                       # Game AI Framework
│   │   ├── __init__.py                  # Package initialization
│   │   ├── board.py                     # Game board abstraction
│   │   ├── gui.py                       # GUI for game visualization
│   │   ├── managed_context/             # Context management utilities
│   │   └── test_suite_analysis/         # Test suite for algorithm validation
│   ├── labyrinths/                      # Maze/Labyrinth Test Cases
│   │   ├── 01_empty.txt – 05_maze.txt   # Basic labyrinth layouts
│   │   └── 06_empty_food.txt – 10_maze_food.txt  # Labyrinths with food items
│   └── tiles/                           # Game Tile Assets
│       ├── bear_scaled.png              # Bear game piece
│       ├── cat_scaled.png               # Cat game piece
│       ├── donut_scaled.png             # Donut/food item
│       ├── door_scaled.png              # Door/exit tile
│       ├── block_scaled.png             # Wall/block tile
│       ├── blank_scaled.png             # Empty tile
│       ├── queen_scaled.png             # Queen piece (N-Queens)
│       ├── gomoku_X/O_scaled.png        # Gomoku game pieces
│       ├── chess_blank_scaled.png       # Chess board blank
│       └── ... (+ shrinked variants)    # Smaller tile versions
```

---

## ✅ Progress Tracker

### Labs
- [x] Lab 1 — Python Fundamentals (notebooks + lambda exercises)
- [ ] Lab 2 — Game AI: Backtracking
- [ ] Lab 3 — Game AI: Graph Search
- [ ] Lab 4 — Game AI: Minimax
- [ ] Lab 5 — Machine Learning
- [ ] Lab 6 — Deep Learning / NLP

### Practice Exercises (Graded)
- [ ] Practice 1
- [ ] Practice 2
- [ ] Practice 3
- [ ] Practice 4
- [ ] Practice 5
- [ ] Practice 6

### Lecture Quizzes (10 total)
- [ ] Quiz 1
- [ ] Quiz 2
- [ ] Quiz 3
- [ ] Quiz 4
- [ ] Quiz 5
- [ ] Quiz 6
- [ ] Quiz 7
- [ ] Quiz 8
- [ ] Quiz 9
- [ ] Quiz 10

### Assignments
- [ ] Assignment 1 (smaller — 3 pts)
- [ ] Assignment 2 (larger — 9 pts, in-person presentation)

### Exam
- [ ] Final Exam (in-person, January)

---

## 🛠️ Tech Stack & Prerequisites

| Tool / Library | Purpose |
|---|---|
| **Python 3.12+** | Primary programming language |
| **TensorFlow 2.18+** | Deep learning framework |
| **NumPy 2.x** | Numerical computing |
| **SciPy** | Scientific computing |
| **scikit-learn** | Machine learning algorithms |
| **NLTK** | Natural language processing toolkit |
| **spaCy** | Industrial-strength NLP |
| **gensim** | Topic modeling and word embeddings (Word2Vec) |
| **Matplotlib** | Data visualization |
| **pandas** | Data manipulation and analysis |
| **Jupyter Lab** | Interactive development environment |
| **FreeSimpleGUI** | GUI for game visualizations |
| **Pixi** | Package manager (environment management) |

### Getting Started

```bash
# Clone the repository
git clone https://github.com/simo-hue/ELTE-Principles-Of-AI-Course.git

# Navigate to the project
cd ELTE-Principles-Of-AI-Course/LAB

# Option 1: Using Pixi (recommended — mirrors course setup)
pixi install
pixi shell

# Option 2: Using pip
pip install numpy scipy scikit-learn nltk spacy gensim matplotlib pandas \
    jupyterlab tensorflow freesimplegui openpyxl
```

---

## 🔗 External Resources

| Resource | Link |
|---|---|
| **ELTE Faculty of Informatics** | [inf.elte.hu](https://www.inf.elte.hu/en/) |
| **Textbook** | [S. Russell, P. Norvig: *Artificial Intelligence. A Modern Approach*](https://aima.cs.berkeley.edu/) |
| **Teams Group** | PAI 2026 — join with code: `313droy` |
| **TensorFlow Documentation** | [tensorflow.org](https://www.tensorflow.org/api_docs) |
| **scikit-learn Documentation** | [scikit-learn.org](https://scikit-learn.org/stable/) |
| **NLTK Documentation** | [nltk.org](https://www.nltk.org/) |
| **spaCy Documentation** | [spacy.io](https://spacy.io/) |

---

## ⚠️ Disclaimer

> This repository is intended **for educational purposes only**.
> All lecture materials, slides, frameworks, and course content belong to their respective authors and to **Eötvös Loránd University (ELTE)**, Budapest.
> Personal notes, exercise solutions, and code implementations are my own work.
> This repository is not officially affiliated with or endorsed by ELTE or the course staff.
>
> **Note on quizzes**: Lecture quizzes allow unlimited attempts — use the materials here to understand concepts, not to bypass learning.

---

## 🌟 Star This Repo

If you find these materials helpful for your studies, please consider giving this repository a ⭐ — it helps other ELTE students discover it!

---

<p align="center">
  Made with 🤖 by <a href="https://simo-hue.github.io">Simone Mattioli</a> for Principles of AI students at ELTE Budapest
</p>