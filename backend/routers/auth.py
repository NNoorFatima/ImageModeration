from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from datetime import datetime
import uuid

from database import tokens_collection

router = APIRouter()

# Token input model
class TokenRequest(BaseModel):
    isAdmin: bool = False

# Token output model
class TokenResponse(BaseModel):
    token: str
    isAdmin: bool
    createdAt: datetime

# Admin check helper
def is_admin(auth_header: str):
    token = auth_header.replace("Bearer ", "")
    entry = tokens_collection.find_one({"token": token})
    if not entry or not entry["isAdmin"]:
        raise HTTPException(status_code=403, detail="Admin privileges required")

# Generate token (Admin only)
@router.post("/tokens", response_model=TokenResponse)
def create_token(data: TokenRequest, authorization: str = Header(...)):
    is_admin(authorization)

    token = str(uuid.uuid4())
    token_data = {
        "token": token,
        "isAdmin": data.isAdmin,
        "createdAt": datetime.utcnow()
    }
    tokens_collection.insert_one(token_data)
    return token_data

# List all tokens (Admin only)
@router.get("/tokens", response_model=list[TokenResponse])
def list_tokens(authorization: str = Header(...)):
    is_admin(authorization)
    return list(tokens_collection.find({}, {"_id": 0}))

# Delete token (Admin only)
@router.delete("/tokens/{token}")
def delete_token(token: str, authorization: str = Header(...)):
    is_admin(authorization)
    result = tokens_collection.delete_one({"token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Token not found")
    return {"message": "Token deleted"}
