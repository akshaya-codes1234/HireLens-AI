import streamlit as st

st.set_page_config(page_title="HireLens AI", layout="centered")

st.title("HireLens")
st.write("Your intelligent recruitment workspace")

st.header("HireLens AI Assistant")

user_message = st.text_input("Describe your skills:")
submit = st.button("Analyze")

skills_map = {
    "python": ["python", "py"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis"],
    "ai": ["ai", "artificial intelligence"],
    "deep learning": ["deep learning"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "react": ["react"],
    "node": ["node"],
    "excel": ["excel"]
}

role_requirements = {
    "Machine Learning Engineer": ["python", "machine learning"],
    "Data Scientist": ["python", "data analysis"],
    "Data Analyst": ["data analysis", "excel"],
    "AI Engineer": ["ai", "deep learning"],
    "Backend Developer": ["java"],
    "Frontend Developer": ["javascript", "react"],
    "Full Stack Developer": ["javascript", "node"]
}

if submit and user_message:

    user_message_lower = user_message.lower()
    extracted_skills = []

    for skill, keywords in skills_map.items():
        for word in keywords:
            if word in user_message_lower:
                extracted_skills.append(skill)
                break

    extracted_skills = list(set(extracted_skills))

    st.subheader("Structured Output (JSON)")
    st.json({"skills": extracted_skills})

    st.subheader("Extracted Skills")

    if extracted_skills:
        for skill in extracted_skills:
            st.success(skill.title())
    else:
        st.warning("No skills detected")

    job_roles = []
    role_scores = {}

    for role, required_skills in role_requirements.items():
        matched = [skill for skill in required_skills if skill in extracted_skills]
        score = len(matched) / len(required_skills)

        if score > 0:
            job_roles.append(role)
            role_scores[role] = score

    job_roles = sorted(job_roles, key=lambda x: role_scores[x], reverse=True)

    st.subheader("Suggested Job Roles")

    if job_roles:
        for role in job_roles:
            percent = int(role_scores[role] * 100)
            st.write(f"{role} — Match: {percent}%")
    else:
        st.warning("No matching job roles found")

    st.subheader("Why these roles?")

    for role in job_roles:
        matched = [skill for skill in role_requirements[role] if skill in extracted_skills]
        if matched:
            st.write(f"{role}: matched skills → {', '.join(matched)}")

    st.subheader("Skill Gaps")

    for role in job_roles:
        missing = [skill for skill in role_requirements[role] if skill not in extracted_skills]
        if missing:
            st.write(f"For {role}, improve: {', '.join(missing)}")

    st.subheader("HireLens Insight")

    if job_roles:
        best_role = job_roles[0]
        st.success(f"You are most suitable for {best_role}. Improve missing skills to grow further.")
    else:
        st.warning("Add more technical skills like Python, AI, Data Analysis.")

    st.success("Analysis Complete")