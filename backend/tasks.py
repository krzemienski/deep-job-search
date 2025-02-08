from celery_app import celery_app
from utils.prompt_generator import create_deep_search_prompt, call_openai_for_jobs
import asyncio
from typing import Dict, Any

@celery_app.task(bind=True)
def deep_research_task(self, resume_summary: Dict[str, Any], preferences: Dict[str, Any]) -> Dict[str, Any]:
    """
    Celery task to perform deep research for job opportunities.
    Uses OpenAI to generate relevant job listings based on resume and preferences.
    """
    try:
        # Update initial state
        self.update_state(
            state='PROGRESS',
            meta={
                'progress': 0,
                'status': 'Starting job search...',
                'current_jobs': []
            }
        )

        # Create the search prompt
        prompt = create_deep_search_prompt(resume_summary, preferences)
        
        # Update state - prompt created
        self.update_state(
            state='PROGRESS',
            meta={
                'progress': 20,
                'status': 'Generated search criteria...',
                'current_jobs': []
            }
        )

        # Create event loop for async OpenAI call
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            # Call OpenAI API
            result = loop.run_until_complete(call_openai_for_jobs(prompt))
            
            # Update state with results
            self.update_state(
                state='PROGRESS',
                meta={
                    'progress': 90,
                    'status': 'Processing results...',
                    'current_jobs': result.get('jobs', [])
                }
            )

            # Process and validate results
            if not result.get('jobs'):
                result['jobs'] = []
            if not result.get('followup_questions'):
                result['followup_questions'] = [
                    "Would you like to specify any particular industry?",
                    "Are there specific technologies or skills you'd like to focus on?",
                    "Do you have any preferences regarding company culture?"
                ]

            return {
                'jobs': result['jobs'],
                'followup_questions': result['followup_questions']
            }

        finally:
            loop.close()

    except Exception as e:
        self.update_state(
            state='FAILURE',
            meta={
                'error': str(e),
                'status': 'Failed to complete job search'
            }
        )
        raise
