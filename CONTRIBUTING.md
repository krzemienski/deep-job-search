# Contributing to Deep Job Search

Thank you for your interest in contributing to Deep Job Search! This document provides guidelines and instructions for contributing to the project.

## Development Setup

### Prerequisites

- Python 3.9+
- Node.js 18+
- Docker and Docker Compose (recommended)
- AWS Account (for S3 storage)
- OpenAI API Key

### Local Development Environment

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/deep-job-search.git
cd deep-job-search
```

2. **Set Up Environment Variables**
```bash
# Backend
cp backend/.env.example backend/.env
# Edit backend/.env with your API keys

# Frontend
cp frontend/.env.example frontend/.env
# Edit frontend/.env if needed
```

3. **Using Docker (Recommended)**
```bash
docker-compose up --build
```

4. **Manual Setup**

Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## Testing

### Running Tests

1. **Backend Tests**
```bash
cd backend
pytest
```

2. **Frontend Tests**
```bash
cd frontend
npm test
```

3. **E2E Tests**
```bash
cd e2e
pytest
```

### Writing Tests

- Backend: Use pytest for unit tests
- Frontend: Use Jest and React Testing Library
- E2E: Use pytest with the provided test utilities

## Code Style

### Backend (Python)

- Follow PEP 8 guidelines
- Use Black for code formatting
- Use isort for import sorting
- Maximum line length: 88 characters (Black default)

### Frontend (TypeScript/JavaScript)

- Use Prettier for code formatting
- Follow ESLint configuration
- Use TypeScript for new components
- Follow React functional component patterns

## Pull Request Process

1. **Branch Naming**
   - Feature: `feature/description`
   - Bug Fix: `fix/description`
   - Documentation: `docs/description`

2. **Commit Messages**
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
   - Reference issues when applicable

3. **Before Submitting**
   - Update documentation if needed
   - Add tests for new features
   - Ensure all tests pass
   - Format code according to style guidelines

4. **PR Template**
   ```markdown
   ## Description
   [Describe your changes]

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Other (please specify)

   ## Testing
   [Describe how you tested your changes]

   ## Checklist
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] Code follows style guidelines
   - [ ] All tests passing
   ```

## Documentation

- Update README.md for significant changes
- Document new features in-code with docstrings
- Update API documentation when endpoints change
- Keep configuration examples up to date

## Getting Help

- Open an issue for bugs or feature requests
- Join discussions in existing issues
- Tag maintainers for urgent matters

## Code of Conduct

Please note that this project follows an open and inclusive Code of Conduct. We expect all contributors to:

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.
