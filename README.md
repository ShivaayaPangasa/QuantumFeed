# QuantumFeed
### AI-Driven Science & Technology News Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![NLP](https://img.shields.io/badge/NLP-BART%20%7C%20TF--IDF%20%7C%20LSA-green?style=for-the-badge)

</p>

---

## Overview

QuantumFeed is an AI-powered Science & Technology news intelligence platform that automatically aggregates, summarizes, stores, and presents real-time news articles using Natural Language Processing and Transformer-based AI.

The platform retrieves live news from **The Guardian API**, generates concise summaries using **Facebook BART**, stores processed articles in a **SQLite** database, and serves them through a **Flask-based web application** with a clean and responsive interface.

To complement modern transformer models, the project also explores traditional NLP techniques such as **TF-IDF** and **Latent Semantic Analysis (LSA)** for extractive summarization, providing a comparative understanding of classical and modern approaches to text summarization.

An experimental **Fake News Detection** module further extends the platform by combining transformer-based classification, sentiment analysis, clickbait detection, and source credibility analysis to estimate article trustworthiness.

---

# Problem Statement

Thousands of science and technology articles are published daily across multiple platforms, making it increasingly difficult to identify reliable and relevant information quickly.

Traditional news platforms require users to read lengthy articles, resulting in:

- 📚 Information overload
- ⏳ Time-consuming reading
- 🔁 Duplicate news across sources
- 🔍 Difficulty identifying important breakthroughs
- 📰 Lack of intelligent summarization

QuantumFeed addresses these challenges through AI-powered news summarization and intelligent information processing.

---

# Features

- 📰 Real-time Science & Technology News Aggregation
- 🤖 AI-Powered Abstractive Summarization (Facebook BART)
- 📊 Traditional NLP Summarization (TF-IDF + LSA)
- 💾 SQLite Database Integration
- 🌐 Flask Backend Architecture
- 🎨 Responsive Tailwind CSS Interface
- ⚡ Automated News Processing Pipeline
- 🛡 Experimental Fake News Detection
- 🔄 One-click News Refresh

---

# AI Pipeline

```text
          Guardian News API
                  │
                  ▼
          News Collection Layer
            (Python Requests)
                  │
                  ▼
        Text Cleaning & Processing
                  │
                  ▼
   Facebook BART Transformer Model
                  │
                  ▼
         AI Summary Generation
                  │
                  ▼
          SQLite Database Storage
                  │
                  ▼
            Flask Backend Server
                  │
                  ▼
      HTML + Tailwind CSS Frontend
                  │
                  ▼
                 End User
```

---

# Classical NLP Pipeline (Research Module)

```text
BBC News Dataset
        │
        ▼
 Text Preprocessing
        │
        ▼
 TF-IDF Feature Extraction
        │
        ▼
 Latent Semantic Analysis
        │
        ▼
 Semantic Ranking
        │
        ▼
 Extractive Summary
```

This module was implemented to explore traditional NLP techniques and compare extractive summarization with transformer-based abstractive summarization.

---

# Technology Stack

## Programming Languages

- Python
- JavaScript

## Backend

- Flask

## Frontend

- HTML
- Tailwind CSS
- Jinja2

## Artificial Intelligence

- Hugging Face Transformers
- Facebook BART
- BERT Mini (Fake News Classification)

## Natural Language Processing

- TF-IDF
- Latent Semantic Analysis (LSA)
- NLTK
- TextBlob

## Machine Learning Libraries

- Scikit-learn
- Torch
- Transformers

## Database

- SQLite

## Data Processing

- Pandas
- NumPy

## APIs

- The Guardian Content API

## Version Control

- Git
- GitHub

---

# Project Structure

```
QuantumFeed
│
├── app
│   ├── services
│   │   ├── fetcher.py
│   │   └── articles.db
│   │
│   ├── templates
│   │   └── index.html
│   │
│   ├── routes.py
│   └── __init__.py
│
├── models
│   ├── Summarizer.py
│   └── fake_news_detector.py
│
├── bbcnews.csv
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

# Applications

- AI News Platforms
- Research Portals
- Educational Platforms
- Technology Media
- Scientific Knowledge Management
- Enterprise Knowledge Bases
- Government Information Platforms

---

# 🌍 United Nations Sustainable Development Goals

This project contributes towards:

🎓 **SDG 4 – Quality Education**

Promotes easier access to scientific and technological knowledge.

🏗 **SDG 9 – Industry, Innovation & Infrastructure**

Demonstrates AI-driven digital innovation using Natural Language Processing.

⚖ **SDG 16 – Peace, Justice & Strong Institutions**

Encourages informed decision-making through improved access to reliable information.

---

# Future Enhancements

- Personalized News Recommendations
- Semantic Search using Sentence Transformers
- Multilingual Summarization
- Explainable AI for Summary Generation
- Voice-enabled News Assistant
- Real-time Trending Topic Detection
- Docker & Cloud Deployment
- Mobile Application
- Conversational AI using Large Language Models

---

# Learning Outcomes

Through QuantumFeed, I gained practical experience in:

- Natural Language Processing
- Transformer Models
- Text Summarization
- Information Retrieval
- REST API Integration
- Flask Backend Development
- SQLite Database Management
- AI System Design
- Classical NLP Techniques
- End-to-End AI Pipeline Development

---

# 🤝 Acknowledgements

QuantumFeed originated as a collaborative hackathon project.

Special thanks to **Hritvika Chandra** for collaborating on the project. This repository is maintained as my portfolio version to showcase the implementation and continue future enhancements.

---

# 📄 License

Licensed under the Apache License 2.0.

---

## ⭐ If you found this project interesting, consider starring the repository!
