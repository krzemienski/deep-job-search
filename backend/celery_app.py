import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Celery configuration
celery_app = Celery(
    'deep_job_search',
    broker=os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/0'),
    include=['tasks']  # Import tasks module
)

# Optional configurations
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=3600,  # 1 hour timeout
    worker_prefetch_multiplier=1,  # Process one task at a time
)

if __name__ == '__main__':
    celery_app.start()
