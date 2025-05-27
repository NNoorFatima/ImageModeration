from fastapi import APIRouter, File, UploadFile, Header, HTTPException
from database import tokens_collection, usages_collection
from datetime import datetime
import random

router = APIRouter()

# Helper: Check if token is valid
def validate_token(authorization: str):
    token = authorization.replace("Bearer ", "")
    token_doc = tokens_collection.find_one({"token": token})
    if not token_doc:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return token

# Endpoint: POST /moderate
@router.post("/")
async def moderate_image(file: UploadFile = File(...), authorization: str = Header(...)):
    token = validate_token(authorization)

    # Log usage
    usages_collection.insert_one({
        "token": token,
        "endpoint": "/moderate",
        "timestamp": datetime.utcnow()
    })

    # Fake moderation logic (random probabilities)
    fake_report = {
        "nudity": round(random.uniform(0, 1), 2),
        "violence": round(random.uniform(0, 1), 2),
        "self_harm": round(random.uniform(0, 1), 2),
        "hate_symbol": round(random.uniform(0, 1), 2),
    }

    return {
        "filename": file.filename,
        "result": fake_report
    }
