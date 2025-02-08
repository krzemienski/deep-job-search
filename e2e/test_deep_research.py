import os
import pytest
import requests
import time
from pathlib import Path

# Constants
BASE_URL = "http://localhost:8000"
SAMPLE_CV_PATH = Path(__file__).parent.parent / "docs" / "artifacts" / "Nick_Krzemienski_072024_cv.pdf"
MAX_WAIT_TIME = 300  # 5 minutes timeout
POLL_INTERVAL = 5  # 5 seconds between polls

def test_deep_research_flow():
    """
    Test the complete flow of uploading a resume and getting job recommendations.
    Uses the sample CV provided in docs/artifacts directory.
    """
    assert SAMPLE_CV_PATH.exists(), f"Sample CV not found at {SAMPLE_CV_PATH}"
    
    # Step 1: Upload Resume
    files = {
        'file': ('resume.pdf', open(SAMPLE_CV_PATH, 'rb'), 'application/pdf')
    }
    upload_response = requests.post(
        f"{BASE_URL}/api/upload_resume",
        files=files
    )
    assert upload_response.status_code == 200, f"Upload failed: {upload_response.text}"
    resume_data = upload_response.json()
    assert 'summary' in resume_data, "Resume summary not found in response"
    
    # Step 2: Submit Job Preferences and Start Task
    preferences = {
        "location": "Remote",
        "company_size": "Any",
        "role_type": "Software Engineering",
        "additional_info": "Interested in AI/ML positions"
    }
    
    search_response = requests.post(
        f"{BASE_URL}/api/deep_search",
        json={
            "resume_summary": resume_data['summary'],
            "preferences": preferences
        }
    )
    assert search_response.status_code == 200, f"Search request failed: {search_response.text}"
    
    task_data = search_response.json()
    assert 'task_id' in task_data, "Task ID not found in response"
    task_id = task_data['task_id']
    
    # Step 3: Poll for Task Status
    start_time = time.time()
    final_result = None
    
    while time.time() - start_time < MAX_WAIT_TIME:
        status_response = requests.get(f"{BASE_URL}/api/task/{task_id}")
        assert status_response.status_code == 200, f"Status check failed: {status_response.text}"
        
        status_data = status_response.json()
        print(f"Task Status: {status_data['status']}, Progress: {status_data.get('progress', 0)}%")
        
        if status_data['status'] == 'SUCCESS':
            final_result = status_data['result']
            break
        elif status_data['status'] == 'FAILURE':
            raise AssertionError(f"Task failed: {status_data.get('error', 'Unknown error')}")
        
        # Show intermediate results if available
        if status_data.get('result', {}).get('current_jobs'):
            print(f"Found {len(status_data['result']['current_jobs'])} jobs so far")
        
        time.sleep(POLL_INTERVAL)
    
    assert final_result is not None, "Task did not complete within timeout"
    
    # Step 4: Validate Results
    assert 'jobs' in final_result, "No jobs in final result"
    assert len(final_result['jobs']) > 0, "No jobs found"
    
    # Validate job listing structure
    first_job = final_result['jobs'][0]
    required_fields = ['title', 'company', 'location', 'description', 'apply_link']
    for field in required_fields:
        assert field in first_job, f"Required field '{field}' missing from job listing"
    
    # Validate follow-up questions
    assert 'followup_questions' in final_result, "No follow-up questions in result"
    assert len(final_result['followup_questions']) > 0, "No follow-up questions generated"

if __name__ == "__main__":
    pytest.main([__file__])
