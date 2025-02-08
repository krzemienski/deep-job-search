#!/bin/bash
set -e

# Get the project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Function to check if a service is healthy
check_service() {
    local service=$1
    local max_attempts=30
    local attempt=1
    
    echo "Waiting for $service to be ready..."
    while [ $attempt -le $max_attempts ]; do
        if curl -s "http://localhost:$2/health" > /dev/null; then
            echo "$service is ready!"
            return 0
        fi
        echo "Attempt $attempt/$max_attempts: $service not ready yet..."
        sleep 2
        attempt=$((attempt + 1))
    done
    
    echo "$service failed to become ready"
    return 1
}

# Create necessary directories and ensure proper permissions
echo "Setting up test environment..."
mkdir -p "${PROJECT_ROOT}/docs/artifacts"
chmod -R 777 "${PROJECT_ROOT}/docs/artifacts"

# Set up environment files
echo "Creating environment files..."

# Create directories and base files
mkdir -p "${PROJECT_ROOT}/frontend" "${PROJECT_ROOT}/backend"

# Create test environment files first
echo "TESTING=true" > "${PROJECT_ROOT}/frontend/.env.test"
echo "TESTING=true" > "${PROJECT_ROOT}/backend/.env.test"

# Check if OPENAI_API_KEY is set
if [ -z "${OPENAI_API_KEY}" ]; then
    echo "Error: OPENAI_API_KEY environment variable is not set"
    echo "Please set it by running: export OPENAI_API_KEY=your_api_key"
    exit 1
fi

# Add required environment variables for testing
cat > "${PROJECT_ROOT}/backend/.env" << EOL
OPENAI_API_KEY=${OPENAI_API_KEY}
REDIS_URL=redis://redis:6379/0
AWS_ACCESS_KEY_ID=dummy_key
AWS_SECRET_ACCESS_KEY=dummy_key
AWS_BUCKET_NAME=test-bucket
TESTING=true
EOL

cat > "${PROJECT_ROOT}/frontend/.env" << EOL
NEXT_PUBLIC_API_URL=http://localhost:8000
TESTING=true
EOL

# Ensure we have a clean state
echo "Cleaning up previous containers..."
cd "${PROJECT_ROOT}"
docker-compose down -v

# Start all services with test environment
echo "Starting services..."
TESTING=true docker-compose up -d

# Wait for services to be healthy
check_service "Backend" 8000
check_service "Frontend" 3000

# Run the tests
echo "Running tests..."
TESTING=true /Users/nick/Library/Python/3.12/bin/pytest "${PROJECT_ROOT}/e2e/test_deep_research.py" -v

# Cleanup
echo "Cleaning up..."
docker-compose down
rm "${PROJECT_ROOT}/backend/.env.test" "${PROJECT_ROOT}/frontend/.env.test"
