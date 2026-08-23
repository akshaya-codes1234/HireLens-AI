# HireLens AI

## Project Overview

HireLens AI is a Streamlit-based recruitment assistant prototype. It accepts conversational descriptions of a candidate's experience and technical skills, extracts recognized skills, suggests suitable job roles, calculates role-match percentages, explains matched skills, and identifies skill gaps.

The project is designed as a foundation for an AI recruiter that can help recruiters and candidates make faster, more informed hiring decisions without using an external LLM API key.

## Problem Statement

Recruiters often need to review large amounts of unstructured candidate information and compare it with multiple job roles. Manual review can be slow and inconsistent, while candidates may not know which roles best fit their experience.

HireLens addresses this problem by converting conversational experience descriptions into structured skill information and matching those skills against predefined job-role requirements.

The intended solution covers two parts:

1. **NLP extraction:** Extract skills, technologies, and programming languages from conversational input rather than requiring a structured resume.
2. **Candidate matching:** Automatically extract resume skills, suggest suitable job roles, and match candidates to job descriptions.

The current prototype implements conversational skill extraction and role matching. Resume upload, job-description matching, and separate technologies/languages extraction are planned extensions.

## Installation Instructions

### Prerequisites

- Python 3.9 or newer
- pip

### Setup

1. Open a terminal in the project directory:

   ```powershell
   cd HireLens
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux, activate it with:

   ```bash
   source .venv/bin/activate
   ```

3. Install Streamlit:

   ```bash
   pip install streamlit
   ```

4. Start the application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## Dataset Used

No external dataset is used in the current prototype. The application uses two small, hand-authored dictionaries in `app.py`:

- `skills_map`: supported skills and keyword variants.
- `role_requirements`: job roles and their required skills.

This keeps the prototype self-contained and avoids the need for an LLM API key. A future version should be evaluated with an anonymized resume and job-description dataset containing labeled skills, roles, and match outcomes.

## Methodology

1. The user enters a natural-language description, such as:

   > I worked in the AI/ML department and built CNN models using Python.

2. The input is normalized to lowercase.
3. The system searches for configured keyword variants and maps them to normalized skills.
4. The detected skills are displayed as structured JSON and readable skill labels.
5. Each job role receives a match score:

   `matched required skills / total required skills`

6. Roles with at least one matching skill are sorted by score.
7. The interface explains why each role was suggested and lists missing skills as skill gaps.

Example current output:

```json
{
  "skills": [
    "python",
    "machine learning",
    "ai",
    "deep learning"
  ]
}
```

## Technologies Used

- **Python** for application logic
- **Streamlit** for the interactive web interface
- **Keyword-based NLP** for lightweight entity and skill extraction
- **Dictionary-based matching** for job-role recommendations
- **JSON** for structured extraction output

No LLM API or external API key is required.

## Results

The prototype provides an end-to-end interactive workflow for conversational skill analysis:

- Extracts skills from supported natural-language descriptions.
- Returns extracted data in JSON format.
- Suggests roles such as Machine Learning Engineer, Data Scientist, Data Analyst, AI Engineer, Backend Developer, Frontend Developer, and Full Stack Developer when relevant skills are detected.
- Displays percentage-based role matches.
- Shows matched requirements and missing skills.

For example, an input mentioning Python and machine learning can produce a Machine Learning Engineer recommendation with a strong match score.

Because the current system uses a limited hand-authored vocabulary, results are deterministic and depend on the keywords currently defined in `app.py`.

## Challenges Faced

- Converting informal conversational descriptions into normalized skill names.
- Supporting keyword variations such as `ML` and `machine learning`.
- Avoiding recommendations when no configured skill matches the input.
- Making match scores understandable by showing both matched requirements and skill gaps.
- Building a useful no-API-key prototype while keeping the implementation simple and reproducible.
- The current keyword approach cannot yet reliably understand synonyms, context, experience level, or skills that are not in the configured dictionary.

## Future Improvements

- Add resume upload and text extraction for PDF and DOCX files.
- Extract separate `skills`, `technologies`, and `languages` fields from conversational input.
- Add job-description input and candidate-to-job matching.
- Replace exact keyword matching with a local NLP pipeline using tokenization, phrase matching, named-entity recognition, or embeddings.
- Add synonym handling, spelling tolerance, negation detection, and experience-level extraction.
- Expand the role and skill taxonomy with configurable data files or a database.
- Add candidate ranking, explainable match factors, and recruiter feedback.
- Introduce an anonymized labeled evaluation dataset and report precision, recall, F1 score, and ranking quality.
- Add automated tests for extraction, scoring, unknown skills, and duplicate keyword matches.
- Improve privacy controls, including local processing and removal of personally identifiable information from uploaded resumes.

## Screenshots

The current project is a local Streamlit prototype. Add screenshots here after launching the app with `streamlit run app.py`.

Suggested screenshots:

- Main HireLens input screen.
- JSON extraction and suggested roles for a sample candidate description.
- Skill gaps and role-match explanations.
