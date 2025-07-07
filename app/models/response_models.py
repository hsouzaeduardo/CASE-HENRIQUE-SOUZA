from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatResponse(BaseModel):
    id: str
    prompt: str
    response: str
    model: str
    timestamp: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                
                "prompt": "Hello, qual a cotação do dolar?",
                "response": "Hoje o dolar está : R$5.50!",
                "model": "gpt-4o-mini",
                "timestamp": "2024-01-01T12:00:00Z"
            }
        }

class ErrorResponse(BaseModel):
    detail: str
    error_code: Optional[str] = None