from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv
from celery.result import AsyncResult
import tempfile
import boto3
import uuid
from io import BytesIO
import pdfplumber
from utils.parse_resume import parse_resume
from utils.summarization import summarize_resume
from tasks import deep_research_task
from config.aws_config import upload_to_s3

load_dotenv()

app = FastAPI(title="Deep Job Search API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobPreferences(BaseModel):
    location: str
    company_size: str
    role_type: str
    additional_info: Optional[str] = None

class DeepSearchRequest(BaseModel):
    resume_summary: dict
    preferences: JobPreferences

class TaskResponse(BaseModel):
    task_id: str
    status: str
    message: str

class TaskStatus(BaseModel):
    task_id: str
    status: str
    progress: Optional[int]
    result: Optional[dict]
    error: Optional[str]

@app.get("/")
async def read_root():
    return {"message": "Deep Job Search API is running"}

@app.get("/health")
async def health_check():
    """Health check endpoint for the backend service."""
    try:
        # Check Redis connection
        task = deep_research_task.delay(
            resume_summary={"test": "test"},
            preferences={"test": "test"}
        )
        task.revoke()
        
        return {
            "status": "healthy",
            "services": {
                "redis": "connected",
                "celery": "connected"
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Service unhealthy: {str(e)}"
        )

@app.post("/api/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Read file content
        content = await file.read()
        
        # For testing, we'll skip S3 upload and just process the file directly
        if os.getenv("TESTING") == "true":
            # Create a temporary file to store the content
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                temp_file.write(content)
                temp_path = temp_file.name
            
            # Process the resume
            with pdfplumber.open(temp_path) as pdf:
                resume_text = ""
                for page in pdf.pages:
                    resume_text += page.extract_text() + "\n"
            os.unlink(temp_path)  # Clean up temp file
            
            return {
                "summary": {
                    "text": resume_text,
                    "file_name": file.filename,
                    "content_type": file.content_type
                }
            }
        
        # For production, upload to S3
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        
        bucket_name = os.getenv('AWS_BUCKET_NAME', 'deep-job-search')
        file_key = f'resumes/{uuid.uuid4()}-{file.filename}'
        
        # Upload to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=content,
            ContentType=file.content_type
        )
        
        # Get the uploaded file from S3
        s3_response = s3.get_object(Bucket=bucket_name, Key=file_key)
        with pdfplumber.open(BytesIO(s3_response['Body'].read())) as pdf:
            resume_text = ""
            for page in pdf.pages:
                resume_text += page.extract_text() + "\n"
        
        return {
            "summary": {
                "text": resume_text,
                "file_name": file.filename,
                "content_type": file.content_type,
                "s3_key": file_key
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading to S3: {str(e)}")

@app.post("/api/deep_search", response_model=TaskResponse)
async def deep_search(request: DeepSearchRequest):
    try:
        # Start Celery task
        task = deep_research_task.delay(
            resume_summary=request.resume_summary,
            preferences=request.preferences.dict()
        )
        
        return {
            "task_id": task.id,
            "status": "PENDING",
            "message": "Deep research task started"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/task/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str):
    try:
        task_result = AsyncResult(task_id)
        
        result = {
            "task_id": task_id,
            "status": task_result.status,
            "progress": None,
            "result": None,
            "error": None
        }
        
        if task_result.status == 'PROGRESS':
            result["progress"] = task_result.info.get('progress', 0)
            result["result"] = {
                "current_jobs": task_result.info.get('current_jobs', []),
                "followup_questions": task_result.info.get('followup_questions', []),
                "status": task_result.info.get('status', '')
            }
        elif task_result.status == 'SUCCESS':
            result["progress"] = 100
            result["result"] = task_result.get()
        elif task_result.status == 'FAILURE':
            result["error"] = str(task_result.result)
            
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
