import pytest
from unittest.mock import MagicMock, patch
from app.services.database_service import DatabaseService

@pytest.fixture
def mock_prompt_repository():
    return MagicMock()

@pytest.fixture
def db_service(mock_prompt_repository):
    return DatabaseService(mock_prompt_repository)

def test_save_chat_interaction_calls_save_prompt(db_service, mock_prompt_repository):
    mock_prompt_repository.save_prompt.return_value = "abc-123"
    with patch("app.services.database_service.current_timestamp_iso", return_value="2024-01-01T12:00:00Z"):
        prompt_id = db_service.save_chat_interaction(
            user_id="user1",
            prompt="Oi!",
            response="Olá!",
            model="gpt-4o"
        )
    assert prompt_id == "abc-123"
    args, kwargs = mock_prompt_repository.save_prompt.call_args
    prompt_data = args[0]
    assert prompt_data["user_id"] == "user1"
    assert prompt_data["prompt"] == "Oi!"
    assert prompt_data["response"] == "Olá!"
    assert prompt_data["model"] == "gpt-4o"
    assert prompt_data["timestamp"] == "2024-01-01T12:00:00Z"

def test_get_chat_interaction_calls_get_prompt(db_service, mock_prompt_repository):
    mock_prompt_repository.get_prompt.return_value = {"id": "abc", "user_id": "user1"}
    result = db_service.get_chat_interaction("abc", "user1")
    mock_prompt_repository.get_prompt.assert_called_once_with("abc", "user1")
    assert result["id"] == "abc"
    assert result["user_id"] == "user1"
