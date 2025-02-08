import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

async def summarize_resume(text: str) -> dict:
    """
    Use OpenAI to summarize resume text into structured data
    """
    try:
        prompt = f"""
        Analyze the following resume and extract key information in JSON format:
        
        {text}
        
        Please provide a JSON response with the following structure:
        {{
            "skills": ["skill1", "skill2", ...],
            "experience": [
                {{
                    "title": "job title",
                    "company": "company name",
                    "duration": "duration",
                    "highlights": ["achievement1", "achievement2", ...]
                }}
            ],
            "education": [
                {{
                    "degree": "degree name",
                    "institution": "institution name",
                    "year": "graduation year"
                }}
            ],
            "summary": "brief professional summary"
        }}
        """
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional resume analyzer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        # Parse the response into JSON
        summary = json.loads(response.choices[0].message.content)
        return summary
    
    except Exception as e:
        raise Exception(f"Error summarizing resume: {str(e)}")
