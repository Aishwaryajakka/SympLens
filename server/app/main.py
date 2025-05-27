from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import generate, feedback

app = FastAPI(
    title="SymLens API",
    description="Backend service for generating and evaluating visual symptom simulations.",
    version="1.0.0"
)

# CORS setup 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route includes
app.include_router(generate.router, prefix="/generate", tags=["Generate"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])

@app.get("/")
async def root():
    return {"message": "SymLens API is live."}
