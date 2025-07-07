import os
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Azure OpenAI
    azure_openai_deployment_name: str
    azure_openai_endpoint: str
    azure_openai_api_version: str
    azure_openai_api_key: str
    
    # Cosmos DB
    cosmos_endpoint: str
    cosmos_key: str
    cosmos_database_name: str
    cosmos_container_name: str
    
    # App settings
    app_name: str = "AI Agent API"
    debug: bool = False
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False
    log_level: str = "info"
    
    class Config:
        env_file = ".env"
        case_sensitive = False
