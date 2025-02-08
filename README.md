# Deep Job Search Platform

An AI-powered job search platform that uses resume parsing and deep research to match tech professionals with relevant job opportunities.

# 🤖 Built with Windsurf - The World's First Agentic IDE

> **Watch the Build Process**: [🎥 Building Deep Job Search with Windsurf](https://youtu.be/FNO8ZIMsyGA)

This entire project was built using Windsurf, demonstrating the power of AI-assisted development. Every aspect of the application - from architecture to implementation - was created through structured prompts and specifications found in the `/docs` directory.

## 📚 Project Documentation and Prompts

Each file in the `/docs` directory serves a specific purpose in guiding Windsurf to build the application:

### Core Project Definition
| File | Purpose | Description |
|------|---------|-------------|
| `deep_job_search_prompt.md` | 📋 Initial Project Specification | The foundational prompt that defines the project's goals, features, and requirements. This document guided Windsurf in understanding what we wanted to build: a resume-parsing job search platform with AI-powered recommendations. |
| `tech_stack_document.md` | 🏗️ Technology Decisions | Specifies our technical choices (Next.js, FastAPI, Celery, etc.) and explains why each technology was chosen. This helped Windsurf understand our technical constraints and preferences. |
| `implementation_plan.md` | 📅 Development Roadmap | A step-by-step guide for building the application, breaking down complex features into manageable tasks. This document helped Windsurf prioritize work and maintain a clear development path. |

### Architecture and Design
| File | Purpose | Description |
|------|---------|-------------|
| `app_flow_document.md` | 🔄 User Journey Design | Maps out the complete user experience, from uploading a resume to receiving job recommendations. This guided Windsurf in creating intuitive user flows and interfaces. |
| `backend_structure_document.md` | ⚙️ Backend Architecture | Details the API design, database schema, and service architecture. This document helped Windsurf implement a clean, maintainable backend with proper separation of concerns. |
| `frontend_guidelines_document.md` | 🎨 Frontend Architecture | Defines component structure, styling guidelines, and state management approaches. This ensured Windsurf created a consistent, modern UI with reusable components. |

### Project Organization
| File | Purpose | Description |
|------|---------|-------------|
| `file_structure_document.md` | 📁 Project Layout | Defines the organization of code, assets, and configuration files. This helped Windsurf maintain a clean, scalable project structure. |
| `cursorrules_file.md` | ⌨️ IDE Configuration | Contains IDE-specific settings for code formatting, linting, and editor behavior. This ensured consistent code style across the project. |
| `windsurf_file.md` | 🛠️ Windsurf Settings | Configures Windsurf's behavior, including AI model preferences and development workflow settings. This optimized Windsurf's assistance for our specific needs. |

### How These Prompts Work Together

1. **Project Definition Phase**
   - `deep_job_search_prompt.md` sets the overall vision
   - `tech_stack_document.md` defines our technical approach
   - `implementation_plan.md` creates our roadmap

2. **Architecture Phase**
   - `backend_structure_document.md` designs our server architecture
   - `frontend_guidelines_document.md` establishes our UI/UX patterns
   - `app_flow_document.md` connects frontend and backend through user journeys

3. **Implementation Phase**
   - `file_structure_document.md` organizes our codebase
   - `cursorrules_file.md` maintains code quality
   - `windsurf_file.md` optimizes the development experience

This structured approach to AI-assisted development demonstrates how Windsurf can transform high-level requirements into a fully functional application through well-defined prompts and specifications.

---

## 🌟 Features

- **Resume Upload & Parsing**: Support for PDF and image formats with OCR capabilities
- **AI-Powered Analysis**: Leverages OpenAI's API for resume summarization and job matching
- **Customizable Job Preferences**: Filter by location, company size, and role type
- **Curated Job Listings**: AI-generated deep research for personalized job recommendations

## 🚀 Quick Start

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/deep-job-search.git
cd deep-job-search
```

2. Create a `.env` file in the root directory:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Manual Setup

#### Prerequisites
- Python 3.9+
- Node.js 18+
- AWS Account (for S3 storage)
- OpenAI API Key

#### Backend Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend:
```bash
cd backend
uvicorn main:app --reload
```

#### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run dev
```

## 🔧 Configuration

### Required Environment Variables

```env
# OpenAI Configuration
OPENAI_API_KEY=your_api_key_here

# AWS Configuration
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET_NAME=your_bucket_name

# Backend Configuration
BACKEND_URL=http://localhost:8000
ALLOWED_ORIGINS=http://localhost:3000

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🧪 Testing

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test

# E2E tests
cd e2e
pytest
```

### Functional Test

A sample resume (`docs/artifacts/Nick_Krzemienski_072024_cv.pdf`) is included for testing. To run the functional test:

```bash
cd e2e
pytest test_deep_research.py
```

## 📁 Project Structure

```
.
├── frontend/               # Next.js frontend application
│   ├── pages/             # Page components
│   ├── components/        # Reusable React components
│   ├── styles/            # CSS and styling
│   └── tests/             # Frontend tests
├── backend/               # FastAPI backend
│   ├── main.py           # Main application entry
│   ├── utils/            # Utility functions
│   ├── config/           # Configuration
│   └── tests/            # Backend tests
├── e2e/                  # End-to-end tests
├── docs/                 # Documentation
│   └── artifacts/        # Test artifacts
└── docker/               # Docker configuration
```

## 🛠️ Development

### API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Code Style

- Backend: Black formatter, isort for imports
- Frontend: Prettier, ESLint

## 🤝 Support

For support, please open an issue in the GitHub repository.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
