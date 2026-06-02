import os
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Request, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="Smart Campus - AI Vision API", version="0.3.0")

# Security
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "local-dev-token").strip()

def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer ") or authorization.split(" ")[1] != AUTH_TOKEN:
        return JSONResponse(
            status_code=401,
            content={
                "type": "https://smart-campus.local/problems/unauthorized",
                "title": "Unauthorized",
                "status": 401,
                "detail": "Missing or invalid bearer token",
                "instance": "/detect"
            }
        )
    return authorization

class DetectionRequest(BaseModel):
    camera_id: str
    image_url: Optional[HttpUrl] = None
    image_base64: Optional[str] = None

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ai-vision",
        "version": "0.3.0"
    }

@app.post("/detect")
def detect_image(request: DetectionRequest, token: str = Depends(verify_token)):
    if isinstance(token, JSONResponse):
        return token
        
    if not request.image_url and not request.image_base64:
        return JSONResponse(
            status_code=400,
            content={
                "type": "https://smart-campus.local/problems/invalid-image",
                "title": "Invalid image",
                "status": 400,
                "detail": "image_url or image_base64 is required",
                "instance": "/detect"
            }
        )
        
    return {
        "detection_id": "DET001",
        "camera_id": request.camera_id,
        "label": "person",
        "confidence": 0.91,
        "risk_level": "medium"
    }
