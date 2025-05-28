from fastapi import FastAPI
from backend.routers import auth, moderate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development: allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(moderate.router, prefix="/moderate", tags=["Moderation"])
# app.include_router(moderate.router, prefix="/moderate", tags=["Moderation"])

@app.get("/")
def root():
    return {"message": "Image Moderation API is running"}
