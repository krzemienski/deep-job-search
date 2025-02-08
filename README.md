# Deep Job Search Platform

An AI-powered job search platform that uses resume parsing and deep research to match tech professionals with relevant job opportunities.

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

## 🤖 Built with Windsurf

This entire project was built using Windsurf, the world's first agentic IDE. The `/docs` directory contains all the prompts and specifications used to create this project:

- `deep_job_search_prompt.md`: Initial project specification and requirements
- `tech_stack_document.md`: Technical stack decisions and architecture
- `implementation_plan.md`: Step-by-step implementation guide
- `app_flow_document.md`: User journey and application flow
- `backend_structure_document.md`: Backend architecture and API design
- `frontend_guidelines_document.md`: Frontend component structure and styling
- `file_structure_document.md`: Project organization and file layout
- `cursorrules_file.md`: IDE-specific configuration
- `windsurf_file.md`: Windsurf-specific settings and configurations

Watch how this project was built with Windsurf:
[🎥 Building Deep Job Search with Windsurf](https://youtu.be/FNO8ZIMsyGA)

### Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

For support, please open an issue in the GitHub repository.
