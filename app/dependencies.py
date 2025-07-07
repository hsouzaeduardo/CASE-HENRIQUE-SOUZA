from functools import lru_cache
from app.config.settings import Settings
from app.repositories.prompt_repository import PromptRepository
from app.services.agent_service import AgentService
from app.services.database_service import DatabaseService
from fastapi import Depends

@lru_cache()
def get_settings() -> Settings:
    """Get application settings (cached)"""
    return Settings()

def get_prompt_repository(settings: Settings = Depends(get_settings)) -> PromptRepository:
    """Get prompt repository instance"""
    return PromptRepository(settings)

def get_agent_service(settings: Settings = Depends(get_settings)) -> AgentService:
    """Get agent service instance"""
    return AgentService(settings)

def get_database_service(
    prompt_repository: PromptRepository = Depends(get_prompt_repository)
) -> DatabaseService:
    """Get database service instance"""
    return DatabaseService(prompt_repository)