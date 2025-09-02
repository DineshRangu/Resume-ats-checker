import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from keybert import KeyBERT

# Flask setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# KeyBERT model
kw_model = KeyBERT()

# PDF text extraction
def extract_pdf_text(filepath):
    try:
        return extract_text(filepath)
    except Exception as e:
        return f"Error extracting text: {e}"

# Compare keywords and calculate ATS score
def calculate_ats_score(resume_keywords, jd_keywords):
    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)
    matched = resume_set.intersection(jd_set)
    if len(jd_set) == 0:
        return 0, []
    score = (len(matched) / len(jd_set)) * 100
    return round(score, 2), matched

@app.route("/", methods=["GET", "POST"])
def index():
    ats_score = None
    matched = []
    resume_keywords = []
    jd_keywords = []

    if request.method == "POST":
        job_description = request.form.get("job_description")
        file = request.files["resume"]

        if file and job_description:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Extract text from resume
            resume_text = extract_pdf_text(filepath)

            # Extract keywords
            resume_keywords_raw = kw_model.extract_keywords(resume_text, top_n=10)
            jd_keywords_raw = kw_model.extract_keywords(job_description, top_n=10)

            # Keep only the keywords (drop scores)
            resume_keywords = [kw for kw, _ in resume_keywords_raw]
            jd_keywords = [kw for kw, _ in jd_keywords_raw]

            # ATS Score
            ats_score, matched = calculate_ats_score(resume_keywords, jd_keywords)

    return render_template(
        "index.html",
        ats_score=ats_score,
        matched=matched,
        resume_keywords=resume_keywords,
        jd_keywords=jd_keywords
    )

if __name__ == "__main__":
    app.run(debug=True)
