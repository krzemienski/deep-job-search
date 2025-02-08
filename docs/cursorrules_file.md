---

# .cursorrules

## Project Overview
- **Type:** cursorrules_file
- **Description:** Deep Job Search is an AI-powered platform that combines resume parsing with customizable job preference configurations to generate tailored job listings for tech professionals and recent graduates.
- **Primary Goal:** Streamline and personalize the job search process by leveraging AI to manage resume uploads, generate deep research prompts, and curate highly relevant job listings.

## Project Structure
### Framework-Specific Routing
- **Directory Rules:**
  - Next.js 14: Use the app/[route]/page.tsx conventions to structure a modern, responsive UI.
  - Example 1: "Next.js 14 (App Router)" → app/[route]/page.tsx conventions
  - Example 2: "Next.js (Pages Router)" → pages/[route].tsx pattern (not applied in this project)
  - Example 3: "React Router 6" → src/routes/ with createBrowserRouter (not applicable)

### Core Directories
- **Versioned Structure:**
  - app: Contains the Next.js 14 App Router based frontend including key pages such as Home, Resume Upload, Preferences, and Results.
  - backend: Holds the Python API implementation (using frameworks like Flask or FastAPI) for handling resume parsing, prompt generation, and job data aggregation.

### Key Files
- **Stack-Versioned Patterns:**
  - app/layout.tsx: Next.js 14 root layout for the entire UI.
  - app/[page].tsx: Page-specific components built using App Router conventions (e.g., Home, Resume Upload, Preferences, Results).
  - backend/main.py: Python entry point managing API endpoints such as /api/upload_resume and /api/deep_search.

## Tech Stack Rules
- **Version Enforcement:**
  - next@14: App Router required, disallowing the use of getInitialProps to enforce modern routing practices.
  - python@3.x: Utilize current Python standards with frameworks like Flask or FastAPI to ensure robust API handling.

## PRD Compliance
- **Non-Negotiable:**
  - "The Deep Job Search Platform is designed to help tech professionals and recent graduates quickly find job opportunities that match their skills, experiences, and preferences." : The system must streamline resume processing, allow precise configuration of job search criteria, and return curated job listings using AI.

## App Flow Integration
- **Stack-Aligned Flow:**
  - Next.js 14 Flow → app/home/page.tsx for the Landing page, app/upload/page.tsx for Resume Upload, app/preferences/page.tsx for job preference configuration, and app/results/page.tsx for displaying curated job listings.

---