import pytesseract
from PIL import Image
import io
from fastapi import UploadFile
import PyPDF2

async def parse_resume(file: UploadFile) -> str:
    """
    Parse text from a resume file (PDF or image)
    """
    content = await file.read()
    text = ""
    
    try:
        if file.filename.lower().endswith('.pdf'):
            # Parse PDF
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        
        elif file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Parse image using OCR
            image = Image.open(io.BytesIO(content))
            text = pytesseract.image_to_string(image)
        
        else:
            raise ValueError("Unsupported file format")
        
        return text.strip()
    
    except Exception as e:
        raise Exception(f"Error parsing resume: {str(e)}")
    finally:
        await file.seek(0)  # Reset file pointer for subsequent reads
