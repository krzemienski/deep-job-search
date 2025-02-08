---

# .windsurfrules

## Project Overview
- **Type:** windsurf_file
- **Description:** This project outlines the Deep Job Search Platform, an application designed to simplify and personalize the job search process for tech professionals and recent graduates. The system leverages Next.js on the frontend and Python on the backend to enable users to upload and parse resumes, configure job preferences, generate a tailored job search prompt, and display curated job listings based on AI aggregation.
- **Primary Goal:** Streamline and personalize the job search experience by integrating AI-driven resume parsing and deep research task generation to deliver highly relevant job listings.

## Project Structure

### Framework-Specific Routing
- **Directory Rules:**
  - Next.js 14 (App Router): Use the `app/` directory with nested route folders following the `app/[route]/page.tsx` conventions.
  - Example 1: "Next.js 14 (App Router)" → `app/[route]/page.tsx` conventions
  - Example 2: "Next.js (Pages Router)" → `pages/[route].tsx` pattern (not applicable for this project)
  - Example 3: "React Router 6" → `src/routes/` with `createBrowserRouter` (alternative, not used here)

### Core Directories
- **Versioned Structure:**
  - app/api: Next.js 14 API routes using Route Handlers for managing resume uploads and deep research prompt generation.
  - app/resume: Contains components and pages for the resume upload and parsing functionality.
  - app/preferences: Houses forms and components for configuring user job preferences.
  - app/results: Hosts the UI for displaying curated job listings in a responsive and user-friendly layout.

### Key Files
- **Stack-Versioned Patterns:**
  - app/resume/page.tsx: Implements the resume upload interface with support for drag-and-drop and file input handling.
  - app/preferences/page.tsx: Contains the forms and logic to capture and manage user-defined job preferences.
  - app/results/page.tsx: Displays the curated job listings using modern card-based and responsive design patterns.

## Tech Stack Rules
- **Version Enforcement:**
  - next@14: Enforces the use of the App Router, ensuring no legacy routing methods like `getInitialProps` are used and nested routing is maintained.
  - python@3.x: For building backend API endpoints (using Flask or FastAPI) to securely process resume uploads, perform OCR, and generate AI prompts.

## PRD Compliance
- **Non-Negotiable:**
  - "The Deep Job Search Platform is designed to help tech professionals and recent graduates quickly find job opportunities that match their skills, experiences, and preferences." : This directive mandates the implementation of robust resume parsing, dynamic deep research task generation, and the delivery of a user-specific, curated list of job listings, in accordance with the PRD.

## App Flow Integration
- **Stack-Aligned Flow:**
  - Next.js 14 Core Flow → The application starts at `app/home/page.tsx` (Landing Page), flows to `app/resume/page.tsx` for resume uploads, continues with `app/preferences/page.tsx` for job preferences, and culminates at `app/results/page.tsx` where curated job listings are displayed using server actions and modern responsive design.

---