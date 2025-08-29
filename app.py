import streamlit as st
import PyPDF2
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Define skills to check
# ---------------------------
SKILLS = ["Python", "Machine Learning", "Deep Learning", "SQL", "Excel", "Data Science", "NLP", "C++", "Java"]

# ---------------------------
# Title
# ---------------------------
st.title("📄 AI Resume Analyzer (Advanced Version)")
st.write("Upload your resume (PDF/TXT) → Extract text → Analyze skills → Show graph 🚀")

# ---------------------------
# Upload Resume
# ---------------------------
uploaded_file = st.file_uploader("📂 Upload your Resume", type=["pdf", "txt"])

if uploaded_file is not None:
    text = ""

    # Extract text from PDF
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    # Extract text from TXT
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")

    st.success("✅ Resume uploaded successfully!")

    # Show extracted text (hidden inside expander)
    with st.expander("📑 View Extracted Resume Text"):
        st.write(text)

    # ---------------------------
    # Skills Analysis
    # ---------------------------
    found_skills = [skill for skill in SKILLS if skill.lower() in text.lower()]
    missing_skills = [skill for skill in SKILLS if skill.lower() not in text.lower()]

    # Show results
    st.subheader("💡 Skills Found in Resume")
    if found_skills:
        st.success(", ".join(found_skills))
    else:
        st.warning("⚠ No matching skills found!")

    st.subheader("📌 Suggested Skills to Add")
    if missing_skills:
        st.info(", ".join(missing_skills))

    # ---------------------------
    # Skill Frequency Graph
    # ---------------------------
    st.subheader("📊 Skill Match Visualization")

    data = {"Skills": SKILLS, "Present": [1 if skill in found_skills else 0 for skill in SKILLS]}
    import pandas as pd
    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["Skills"], df["Present"])
    ax.set_xlabel("Skills")
    ax.set_ylabel("Presence (1 = Found, 0 = Missing)")
    ax.set_title("Resume Skills Analysis")
    plt.xticks(rotation=45)

    st.pyplot(fig)
