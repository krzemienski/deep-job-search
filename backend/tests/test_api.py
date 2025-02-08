import pytest
from fastapi.testclient import TestClient
from main import app
import os
import json
from pathlib import Path

client = TestClient(app)

# Test data paths
SAMPLE_CV_PATH = Path("../docs/artifacts/Nick_Krzemienski_072024_cv.pdf")

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Deep Job Search API is running"}

def test_upload_resume():
    """Test resume upload endpoint"""
    assert SAMPLE_CV_PATH.exists(), f"Sample CV not found at {SAMPLE_CV_PATH}"
    
    with open(SAMPLE_CV_PATH, "rb") as f:
        files = {"file": ("resume.pdf", f, "application/pdf")}
        response = client.post("/api/upload_resume", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "file_path" in data
    assert data["message"] == "Resume processed successfully"

def test_deep_search():
    """Test deep search endpoint"""
    # First upload a resume to get the summary
    with open(SAMPLE_CV_PATH, "rb") as f:
        files = {"file": ("resume.pdf", f, "application/pdf")}
        upload_response = client.post("/api/upload_resume", files=files)
    
    assert upload_response.status_code == 200
    resume_data = upload_response.json()
    
    # Now test the deep search
    search_data = {
        "resume_summary": resume_data["summary"],
        "preferences": {
            "location": "Remote",
            "company_size": "Any",
            "role_type": "Software Engineering",
            "additional_info": "Interested in AI/ML positions"
        }
    }
    
    response = client.post("/api/deep_search", json=search_data)
    assert response.status_code == 200
    
    jobs = response.json()
    assert isinstance(jobs, list)
    assert len(jobs) > 0
    
    # Validate job structure
    first_job = jobs[0]
    required_fields = ['title', 'company', 'location', 'description', 'apply_link']
    for field in required_fields:
        assert field in first_job

def test_invalid_file_upload():
    """Test upload with invalid file type"""
    # Create a text file
    with open("test.txt", "w") as f:
        f.write("test content")
    
    with open("test.txt", "rb") as f:
        files = {"file": ("test.txt", f, "text/plain")}
        response = client.post("/api/upload_resume", files=files)
    
    assert response.status_code == 400
    assert "Unsupported file format" in response.json()["detail"]
    
    # Clean up
    os.remove("test.txt")

def test_invalid_deep_search_request():
    """Test deep search with invalid data"""
    invalid_data = {
        "resume_summary": {},  # Empty summary
        "preferences": {
            "location": "",    # Missing required field
            "company_size": "Any",
            "role_type": "",   # Missing required field
        }
    }
    
    response = client.post("/api/deep_search", json=invalid_data)
    assert response.status_code == 422  # Validation error
