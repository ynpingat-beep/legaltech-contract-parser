# 📄 LegalTech Contract Parser

A Django-based LegalTech application that automates contract analysis using Natural Language Processing (NLP). The system allows users to upload PDF contracts, extract text, identify important legal entities, detect governing law, categorize clauses, and flag high-risk terms.

---

## 🚀 Features

- 📤 Upload PDF Contracts
- 📄 Extract text using PyMuPDF
- 🧠 Named Entity Recognition (spaCy)
- 🏢 Detect Organizations
- 📅 Extract Important Dates
- ⚖️ Detect Governing Law
- 🚩 Risk Flag Detection
- 📑 Clause Categorization
- 🌐 REST API using Django REST Framework
- 🛠 Django Admin Dashboard
- 🎨 Responsive Bootstrap UI

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- spaCy
- PyMuPDF (fitz)
- Bootstrap 5
- SQLite (Current)
- PostgreSQL (Migration Planned)

---

## 📂 Project Structure

```
legaltech-contract-parser/
│
├── contracts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── utils.py
│   ├── admin.py
│   └── templates/
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/legaltech-contract-parser.git

cd legaltech-contract-parser
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## 📄 Usage

1. Open

```
http://127.0.0.1:8000/
```

2. Upload a PDF Contract

3. The application automatically:

- Extracts PDF text
- Detects Organizations
- Detects Dates
- Detects Governing Law
- Detects Risk Keywords
- Categorizes Clauses

4. View results on the Contract Details page.

---

## 🌐 REST API

### Upload Contract

```
POST /api/upload/
```

### List Contracts

```
GET /api/contracts/
```

### Contract Details

```
GET /api/contracts/<id>/
```

---

## 📸 Screenshots

### Home Dashboard

_Add Screenshot_

### Upload Page

_Add Screenshot_

### Contract Analysis

_Add Screenshot_

### Django Admin

_Add Screenshot_

---

## 📌 Future Improvements

- PostgreSQL Integration
- OCR Support for Scanned PDFs
- AI-powered Clause Summarization
- Contract Comparison
- User Authentication
- Cloud Storage Integration (AWS S3)

---

## 👨‍💻 Author

**Yash Pingat**

B.E. Computer Engineering

LegalTech Internship Project

---

## 📜 License

This project is developed for educational and internship purposes.