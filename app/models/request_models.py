from pydantic import BaseModel, Field
from typing import Optional

class PromptRequest(BaseModel):
    user_id: str = Field(..., description="User identifier")
    prompt: str = Field(..., min_length=1, description="User prompt")
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "prompt": "Hello, how are you?"
            }
        }