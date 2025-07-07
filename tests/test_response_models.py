import pytest
from pydantic import ValidationError
from app.models.response_models import ChatResponse, ErrorResponse

def test_chat_response_valid():
    data = {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "prompt": "Qual a cotação do dólar?",
        "response": "Hoje o dólar está: R$5.50!",
        "model": "gpt-4o-mini",
        "timestamp": "2024-01-01T12:00:00Z"
    }
    resp = ChatResponse(**data)
    assert resp.id == data["id"]
    assert resp.prompt == data["prompt"]
    assert resp.response == data["response"]
    assert resp.model == data["model"]
    assert resp.timestamp == data["timestamp"]

def test_chat_response_missing_field():
    data = {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "prompt": "Qual a cotação do dólar?",
        "response": "Hoje o dólar está: R$5.50!",
        "model": "gpt-4o-mini"
        # falta timestamp
    }
    with pytest.raises(ValidationError) as exc:
        ChatResponse(**data)
    assert "timestamp" in str(exc.value)

def test_error_response_valid():
    data = {"detail": "Erro de validação", "error_code": "400"}
    err = ErrorResponse(**data)
    assert err.detail == "Erro de validação"
    assert err.error_code == "400"

def test_error_response_optional_error_code():
    data = {"detail": "Erro sem código"}
    err = ErrorResponse(**data)
    assert err.detail == "Erro sem código"
    assert err.error_code is None
