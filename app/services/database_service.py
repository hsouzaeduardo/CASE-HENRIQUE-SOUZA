from typing import Dict, Any
from app.repositories.prompt_repository import PromptRepository
from app.utils.datetime_utils import current_timestamp_iso

class DatabaseService:
    def __init__(self, prompt_repository: PromptRepository):
        self.prompt_repository = prompt_repository
    
    def save_chat_interaction(
        self, 
        user_id: str, 
        prompt: str, 
        response: str, 
        model: str
    ) -> str:
        """Save chat interaction to database"""
        prompt_data = {
            "user_id": user_id,
            "prompt": prompt,
            "response": response,
            "model": model,
            "timestamp": current_timestamp_iso(),
        }
        
        return self.prompt_repository.save_prompt(prompt_data)
    
    def get_chat_interaction(self, prompt_id: str, user_id: str) -> Dict[str, Any]:
        """Get chat interaction from database"""
        return self.prompt_repository.get_prompt(prompt_id, user_id)