import pytest
from pydantic import ValidationError
from app.models.request_models import PromptRequest

def test_prompt_request_valid():
    data = {"user_id": "user123", "prompt": "Olá!"}
    req = PromptRequest(**data)
    assert req.user_id == "user123"
    assert req.prompt == "Olá!"

def test_prompt_request_missing_user_id():
    data = {"prompt": "Olá!"}
    with pytest.raises(ValidationError) as exc:
        PromptRequest(**data)
    assert "user_id" in str(exc.value)

def test_prompt_request_missing_prompt():
    data = {"user_id": "user123"}
    with pytest.raises(ValidationError) as exc:
        PromptRequest(**data)
    assert "prompt" in str(exc.value)

def test_prompt_request_empty_prompt():
    data = {"user_id": "user123", "prompt": ""}
    with pytest.raises(ValidationError) as exc:
        PromptRequest(**data)
    assert "ensure this value has at least 1 characters" in str(exc.value)
