import uuid
from typing import Dict, Any
from azure.cosmos import CosmosClient, PartitionKey
from app.config.settings import Settings

class PromptRepository:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._client = None
        self._container = None
    
    @property
    def client(self) -> CosmosClient:
        if self._client is None:
            self._client = CosmosClient(
                self.settings.cosmos_endpoint, 
                self.settings.cosmos_key
            )
        return self._client
    
    @property
    def container(self):
        if self._container is None:
            database = self.client.create_database_if_not_exists(
                id=self.settings.cosmos_database_name
            )
            self._container = database.create_container_if_not_exists(
                id=self.settings.cosmos_container_name,
                partition_key=PartitionKey(path="/user_id")
            )
        return self._container
    
    def save_prompt(self, prompt_data: Dict[str, Any]) -> str:
        """Save prompt data to Cosmos DB"""
        prompt_id = str(uuid.uuid4())
        prompt_data["id"] = prompt_id
        
        self.container.create_item(body=prompt_data)
        
        return prompt_id
    
    def get_prompt(self, prompt_id: str, user_id: str) -> Dict[str, Any]:
        """Get prompt by ID and user ID"""
        return self.container.read_item(
            item=prompt_id,
            partition_key=user_id
        )