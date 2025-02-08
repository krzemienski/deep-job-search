import boto3
import os
from fastapi import UploadFile
from datetime import datetime

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
)

BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

async def upload_to_s3(file: UploadFile) -> str:
    """
    Upload a file to AWS S3 and return the file path
    """
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{file.filename}"
        
        # Read file content
        content = await file.read()
        
        # Upload to S3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=f"resumes/{filename}",
            Body=content,
            ContentType=file.content_type
        )
        
        # Return the S3 path
        return f"s3://{BUCKET_NAME}/resumes/{filename}"
    
    except Exception as e:
        raise Exception(f"Error uploading to S3: {str(e)}")
    finally:
        await file.seek(0)  # Reset file pointer for subsequent reads
