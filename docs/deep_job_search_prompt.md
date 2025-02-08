# Deep Job Search Project Specification (Raw Markdown)

This document outlines a **high-level project overview** and **requirements** for building a **Deep Job Search** application. The front-end will be built with **Next.js** (or a comparable modern web framework), while the backend will be in **Python**. The goal is to parse a user’s resume, allow them to configure preferences, generate a “Deep Research Task” prompt, and retrieve curated job listings that match the user’s background.

---

## 1. Project Goals

1. **Resume Upload & Parsing**:  
   - Users can upload a resume (PDF/image).
   - The system should extract text (OCR if needed) and summarize the user’s experience, skills, and achievements using OpenAI’s APIs (or a similar LLM).

2. **Deep Research Task Generation**:  
   - Based on the parsed resume and user-defined preferences (location, role type, company size, etc.), the system creates a “Deep Research” prompt that tells an AI to locate relevant job openings.
   - The user can adjust parameters (e.g., how many jobs, which cities, ratio of large enterprises vs. startups).

3. **Curated Job Listing Results**:  
   - The system returns a structured list of potential job positions (title, company, link).
   - Results are displayed in a user-friendly interface with clickable links.

4. **Flexible Architecture**:  
   - Frontend: **Next.js** for UI, but the final technology choice for styling and interactivity is flexible (React, Tailwind, etc.).
   - Backend: **Python** for the main logic, including calls to OpenAI’s APIs.
   - The system design should allow easy substitution or expansion of AI/LLM providers, if needed.

---

## 2. High-Level Architecture

+———————+        +—————–+
|   Next.js Frontend  |  <—> |  Python Backend |
|  (UI & UX Layer)    |        | (Flask/FastAPI) |
+———————+        +—————–+
|                         |
|   REST/GraphQL/API      |
|———————––|
v
+————————+
|   OpenAI’s API (LLM)  |
| (Resume Parsing, etc.)|
+————————+

### 2.1 Frontend (Next.js)
- **Pages and Components**:
  - **Home Page**: Landing page with a brief overview and a call-to-action to begin the “Deep Job Search” process.
  - **Resume Upload Page**: Form for uploading PDF/image resumes. Possibly preview or drag-and-drop functionality.
  - **Preferences Page**: A set of fields and toggles (location, company size, remote vs. on-site, ratio of big vs. small companies, etc.).
  - **Results Page**: Displays the curated list of jobs with links to apply, plus any relevant details (title, company, location, etc.).

### 2.2 Backend (Python)
- **Endpoints** (examples):
  - **`POST /api/upload_resume`**: Receives the resume file, extracts text, calls OpenAI for summarization.
  - **`POST /api/deep_search`**: Accepts user preferences + parsed resume text, crafts a “Deep Research Task” prompt, sends it to OpenAI (or a custom aggregator), returns a list of jobs.
  - **`GET /api/jobs`**: (Optional) Could fetch or cache job listings from third-party sources if you integrate with external job APIs.

- **Key Functions**:
  - **`parse_resume(file)`**: Detect file type (PDF, image), perform OCR if needed, return raw text.
  - **`summarize_resume(text)`**: Send the text to OpenAI’s summarizer. The result is a structured summary (JSON with roles, skills, achievements, etc.).
  - **`create_deep_search_prompt(summary, preferences)`**: Generate a specialized job search prompt that instructs the LLM how many jobs to find, the ratio of big vs. small companies, etc.
  - **`call_openai_for_jobs(prompt)`**: Hit OpenAI’s endpoint with the compiled prompt; parse the response into a job listing structure.

---

## 3. Wireframes & User Flows

Below are rough wireframes illustrating the main screens. The styling is up to you (e.g., Tailwind, Material UI, or your own custom CSS).

### 3.1 Home / Landing

+————————————————+
|  [Header / Navbar]                             |
|                                                |
|  Welcome to Deep Job Search!                   |

[Get Started] Button -> goes to Resume Upload


### 3.2 Resume Upload

+————————————————+
|  [Header / Navbar]                             |
|  Upload Your Resume                            |
|                                                |
|  [Drag & Drop Area / File Input]               |
|  [Submit] Button                               |
|                                                |

-> On submit, POST to /api/upload_resume


- **On success**: System returns a parsed resume summary or error if the file is invalid.  
- The user may see a short preview or summary result on the screen.

### 3.3 Preferences

+————————————————+
|  [Header / Navbar]                             |
|  Tell Us Your Job Preferences                  |
|                                                |
|  Location(s): [NY, Remote, etc.]              |
|  Company Size: [Slider or radio: “Startup” vs. “Enterprise”]
|  Roles: [Check/Dropdown for Eng. Manager, Sr. Dev, etc.]
|  Additional Requests: [Text box for any custom instructions]
|                                                |

[Continue / Next] Button


### 3.4 Results Page

+————————————————+
|  [Header / Navbar]                             |
|  Based on your profile, here are some matches: |
|                                                |
|  1) Job Title: Sr. Software Engineer           |
|     Company: ACME Inc.                         |
|     [Apply] Link -> (opens new tab)           |
|                                                |
|  2) Job Title: …                             |
|  …                                           |
|                                                |

[Refine Search] Button


- Display a list (or table, cards, etc.).  
- Each listing has the essential info plus a link to apply.

---

## 4. Requirements & Considerations

1. **Resume Parsing**:  
   - Must handle PDF, ideally images (OCR via Tesseract or similar).  
   - Could extend to handle .docx using python-docx if needed.

2. **OpenAI API Integration**:  
   - Provide a `.env` or environment variable for `OPENAI_API_KEY`.  
   - In production, store credentials securely.

3. **LLM Prompts**:  
   - **Resume Summarization Prompt**: “You are a resume parser…”  
   - **Deep Research Task Prompt**: “You are a job search engine…”  
   - Keep them modular so you can tweak or refine without rewriting the entire codebase.

4. **Scalability**:  
   - If the job search grows large (for instance, making many calls to an external API), consider caching results or adding a queue system.

5. **Error Handling & Logging**:  
   - Graceful handling of file upload errors, OCR failures, or network issues with OpenAI.

6. **Frontend Ambiguity**:  
   - We will definitely use Next.js, but the final styling and state management approach (Redux, React Context, etc.) is up to the implementer.

---

## 5. Sample “Deep Research” Prompt (Reference)

Below is a sample prompt to feed the LLM once the user’s resume is summarized and preferences are known. This is purely for reference; the final system can generate it dynamically:

You are a job search AI. The following JSON represents the candidate’s summarized experience and their job preferences:

Candidate Summary:
{resume_summary_json}

Preferences:
{user_preferences}

Using the candidate’s background in X, Y, Z, find suitable jobs within the United States (or user’s chosen location).
Return a JSON array of job postings with:
	•	title
	•	company
	•	url

Only include results that strongly match the candidate’s background.

---

## 6. Future Enhancements

- **Authenticating with External Job APIs**: Indeed, LinkedIn, etc. to return real-time postings.
- **Advanced Filtering**: Salary range, fully remote vs. hybrid, skill sets (React, Node, AWS, etc.).
- **User Accounts**: Store multiple resumes and track application statuses.
- **Analytics Dashboard**: Show how many times a user clicked on a job link, etc.

---

## 7. Conclusion

This **Deep Job Search** project enables users to upload a resume, specify preferences, and see curated job listings. The front-end is built in **Next.js** while the backend leverages **Python** for OpenAI calls. By using LLMs to parse resumes and craft search prompts, this application aims to streamline the job-hunting process.

**You can feed this specification into another AI** to generate detailed code (both for the front-end and backend). The final technology choices (e.g., Flask vs. FastAPI, Tailwind vs. other styling libraries) are flexible, but the core architecture remains the same.