from fastapi import FastAPI
from routers import auth, moderate

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(moderate.router, prefix="/moderate", tags=["Moderation"])
# app.include_router(moderate.router, prefix="/moderate", tags=["Moderation"])

@app.get("/")
def root():
    return {"message": "Image Moderation API is running"}
