import os
import json
from typing import Dict, List, Optional
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

def create_deep_search_prompt(resume_summary: Dict, preferences: Dict) -> str:
    """Create a prompt for the deep job search based on resume and preferences."""
    prompt = f"""
    Based on the following resume summary and job preferences, find relevant job opportunities:

    Resume Summary:
    {json.dumps(resume_summary, indent=2)}

    Job Preferences:
    - Location: {preferences.get('location', 'Any')}
    - Company Size: {preferences.get('company_size', 'Any')}
    - Role Type: {preferences.get('role_type', 'Any')}
    - Additional Info: {preferences.get('additional_info', 'None')}

    Please provide a list of job opportunities in the following JSON format:
    {{
        "jobs": [
            {{
                "title": "Job Title",
                "company": "Company Name",
                "location": "Job Location",
                "description": "Brief job description",
                "apply_link": "URL to apply",
                "match_score": "Score between 0-100 indicating match with resume"
            }}
        ],
        "followup_questions": [
            "Question 1 to refine search?",
            "Question 2 to refine search?"
        ]
    }}
    """
    return prompt

async def call_openai_for_jobs(prompt: str) -> Dict:
    """Call OpenAI API to get job recommendations."""
    try:
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("Error: OPENAI_API_KEY environment variable is not set")
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
        print(f"Using API key: {api_key[:6]}...")
        client = AsyncOpenAI(api_key=api_key)
        
        async with client:
            print("Making OpenAI API call...")
            response = await client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a job search assistant helping find relevant job opportunities."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            print("OpenAI API call successful")
        
        # Parse the response
        content = response.choices[0].message.content
        print(f"OpenAI response: {content[:200]}...")
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Failed to parse OpenAI response: {str(e)}")
            return {
                "jobs": [],
                "followup_questions": ["Could you provide more specific job requirements?"],
                "error": "Failed to parse OpenAI response"
            }
            
    except Exception as e:
        print(f"OpenAI API error: {str(e)}")
        return {
            "jobs": [],
            "followup_questions": ["Could you provide more specific job requirements?"],
            "error": f"OpenAI API error: {str(e)}"
        }
