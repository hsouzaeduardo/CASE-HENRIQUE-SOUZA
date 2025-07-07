from fastapi import APIRouter, HTTPException, Depends
from app.models.request_models import PromptRequest
from app.models.response_models import ChatResponse, ErrorResponse
from app.services.agent_service import AgentService
from app.services.database_service import DatabaseService
from app.dependencies import get_agent_service, get_database_service
from datetime import datetime
import json

router = APIRouter(prefix="/v1", tags=["chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat(
    prompt_request: PromptRequest,
    agent_service: AgentService = Depends(get_agent_service),
    database_service: DatabaseService = Depends(get_database_service)
):
    """Process chat request and return response"""
    try:
        # Get response from agent
        response_text = agent_service.run_prompt(prompt_request.prompt)
        
        # Save to database
        prompt_id = database_service.save_chat_interaction(
            user_id=prompt_request.user_id,
            prompt=prompt_request.prompt,
            response=response_text,
            model="gpt-4o"
        )

        return ChatResponse(
            id=prompt_id,
            prompt=prompt_request.prompt,
            response=response_text,
            model="gpt-4",
            timestamp=datetime.now().strftime("%H:%M:%S")
      )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))