# ATS Resume Checker

This project is a **Flask-based web application** that analyzes resumes against job descriptions using **NLP keyword extraction**.  
It helps job seekers evaluate how well their resume matches a given job description by calculating an **ATS (Applicant Tracking System) score**.

---

## 🚀 Features
- Upload a **resume in PDF format**.
- Paste or type the **job description**.
- Extracts important **keywords** from both resume and job description using **KeyBERT**.
- Calculates **ATS Score** based on keyword matches:
  ```
  ATS Score = (Matched Keywords / Total Job Description Keywords) * 100
  ```
- Displays:
  - ATS Score with progress bar
  - Matched keywords
  - Extracted resume keywords
  - Extracted job description keywords

---

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, TailwindCss
- **NLP Model:** KeyBERT, Sentence-Transformers
- **PDF Parsing:** pdfminer.six

---

## 📂 Project Structure
```
ats-resume-checker/
│── app.py                # Flask backend
│── templates/
│   └── index.html        # Frontend HTML
│── uploads/              # Uploaded resumes
│── static/               # (Optional) CSS/JS assets
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## ⚙️ Installation & Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📦 Example Requirements File (`requirements.txt`)

```txt
Flask
pdfminer.six
keybert
sentence-transformers
scikit-learn
transformers
```

---

## 🎯 Future Improvements
- Support for **DOCX** resumes
- More advanced NLP matching (semantic similarity instead of only keywords)
- User authentication and saving ATS history
- Deploy to **Heroku / AWS**

---
