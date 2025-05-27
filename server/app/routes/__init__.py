#init
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-frontend-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SymptomRequest(BaseModel):
    symptom: str
    duration: Optional[int] = None  # Duration in days

class FeedbackRequest(BaseModel):
    image_id: str
    was_accurate: bool
    comments: Optional[str] = None


@app.post("/generate")
async def generate_image(request: SymptomRequest):
#Simulating fake image url TODO: Replace with actual image generation logic
    print(f"Generating for: {request.symptom_text}")
    fake_image_url = "https://example.com/generated/fake_image.jpg"
    return {"image_url": fake_image_url}

@app.post("/feedback")
async def feedback(request: FeedbackRequest):
    print(f"Feedback received for image {request.image_id}: "
    f"Was accurate: {request.was_accurate}, Comments: {request.comments}")
    #TODO: Store feedback in a database or file
    return {"message": "Feedback received successfully"}

@app.get("/")
async def root():
    return {"message": "SymLens API is live."}
