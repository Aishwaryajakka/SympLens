#generate
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.models import SymptomRequest

router = APIRouter()

class SymptomRequest(BaseModel):
    user_id: Optional[str]
    symptom_text: str

@router.post("/")
async def generate_image(request: SymptomRequest):
    # TODO: ADD HP AI Studio call
    print(f"[Generate] Symptom text: {request.symptom_text}")
    
    # Placeholder image res
    return {
        "image_url": "https://example.com/fake-image.jpg",
        "symptom": request.symptom_text
    }
