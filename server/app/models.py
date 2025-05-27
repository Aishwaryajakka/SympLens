from pydantic import BaseModel
from typing import Optional

# Use /generate
class SymptomRequest(BaseModel):
    user_id: Optional[str]
    symptom_text: str

# Use /generate 
class GeneratedImageResponse(BaseModel):
    image_url: str
    symptom: str

# Use in /feedback
class FeedbackRequest(BaseModel):
    user_id: Optional[str]
    image_id: str
    was_accurate: bool
    comment: Optional[str] = None
