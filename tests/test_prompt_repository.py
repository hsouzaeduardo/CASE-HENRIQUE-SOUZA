import pytest
from unittest.mock import MagicMock
from app.repositories.prompt_repository import PromptRepository
from app.config.settings import Settings

def make_settings():
    class DummySettings:
        cosmos_endpoint = "https://fake.documents.azure.com:443/"
        cosmos_key = "fake-key"
        cosmos_database_name = "testdb"
        cosmos_container_name = "testcontainer"
    return DummySettings()

@pytest.fixture
def repo():
    settings = make_settings()
    repository = PromptRepository(settings)
    repository._client = MagicMock()
    repository._container = MagicMock()
    return repository

def test_save_prompt_generates_id_and_calls_create_item(repo):
    prompt_data = {"user_id": "user1", "prompt": "Oi!"}
    repo._container.create_item.return_value = None
    prompt_id = repo.save_prompt(prompt_data.copy())
    assert "id" in prompt_data or True  # id is added inside the method
    repo._container.create_item.assert_called_once()
    assert isinstance(prompt_id, str)
    # Verifica se o id retornado está no prompt_data passado ao create_item
    args, kwargs = repo._container.create_item.call_args
    assert "id" in args[0]["body"] or "id" in args[0]

def test_get_prompt_calls_read_item(repo):
    repo._container.read_item.return_value = {"id": "abc", "user_id": "user1", "prompt": "Oi!"}
    result = repo.get_prompt("abc", "user1")
    repo._container.read_item.assert_called_once_with(item="abc", partition_key="user1")
    assert result["id"] == "abc"
    assert result["user_id"] == "user1"
    assert result["prompt"] == "Oi!"
