# Resume-ats-checker
A Flask-based web application that extracts text from PDF resumes, uses KeyBERT to generate keywords, and compares them with job descriptions to calculate an ATS (Applicant Tracking System) score. The app highlights matched and missing keywords, helping job seekers optimize their resumes for better chances of passing ATS filters.

# ATS Resume Checker

This project is a **Flask-based web application** that analyzes resumes against job descriptions using **NLP keyword extraction**.  
It helps job seekers evaluate how well their resume matches a given job description by calculating an **ATS (Applicant Tracking System) score**.

---

## 🚀 Features
- Upload a **resume in PDF format**.
- Paste or type the **job description**.
- Extracts important **keywords** from both resume and job description using **KeyBERT**.
- Calculates **ATS Score** based on keyword matches:
ATS Score = (Matched Keywords / Total Job Description Keywords) * 100

yaml
Copy code
- Displays:
- ATS Score with progress bar
- Matched keywords
- Extracted resume keywords
- Extracted job description keywords

---

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, Bootstrap
- **NLP Model:** KeyBERT, Sentence-Transformers
- **PDF Parsing:** pdfminer.six

---

## 📂 Project Structure
ats-resume-checker/
│── app.py # Flask backend
│── templates/
│ └── index.html # Frontend HTML
│── uploads/ # Uploaded resumes
│── static/ # (Optional) CSS/JS assets
│── requirements.txt # Dependencies
│── README.md # Documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ats-resume-checker.git
   cd ats-resume-checker
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000/
📦 Example Requirements File (requirements.txt)
txt
Copy code
Flask
pdfminer.six
keybert
sentence-transformers
scikit-learn
transformers
