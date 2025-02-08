#!/bin/bash

# Run backend tests
echo "Running backend tests..."
cd backend
python -m pytest

# Run frontend tests
echo "Running frontend tests..."
cd ../frontend
npm test

# Run E2E tests
echo "Running E2E tests..."
cd ../e2e
python -m pytest

echo "All tests completed!"
