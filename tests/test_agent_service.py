import pytest
from unittest.mock import MagicMock, patch
from app.services.agent_service import AgentService, get_dollar_price
from app.config.settings import Settings

@pytest.fixture
def settings():
    class DummySettings:
        azure_openai_api_key = "fake-key"
        azure_openai_endpoint = "https://fake.openai.azure.com/"
        azure_openai_deployment_name = "fake-deployment"
        azure_openai_api_version = "2024-01-01"
    return DummySettings()

@pytest.fixture
def agent_service(settings):
    service = AgentService(settings)
    # Mock _create_agent to avoid real LLM calls
    service._agent = MagicMock()
    return service

def test_run_prompt_returns_content(agent_service):
    mock_response = MagicMock()
    mock_response.content = "Resposta do agente"
    agent_service._agent.invoke.return_value = mock_response
    result = agent_service.run_prompt("Olá!", session_id="sessao1")
    assert result == "Resposta do agente"
    agent_service._agent.invoke.assert_called_once()

def test_run_prompt_returns_str(agent_service):
    agent_service._agent.invoke.return_value = 123
    result = agent_service.run_prompt("Olá!", session_id="sessao2")
    assert result == "123"

def test_get_session_history_creates_and_returns(settings):
    service = AgentService(settings)
    history1 = service._get_session_history("abc")
    history2 = service._get_session_history("abc")
    assert history1 is history2
    history3 = service._get_session_history("def")
    assert history1 is not history3

def test_get_dollar_price_success():
    fake_response = MagicMock()
    fake_response.json.return_value = {"USDBRL": {"bid": "5.55"}}
    with patch("app.services.agent_service.requests.get", return_value=fake_response):
        result = get_dollar_price()
        assert "R$ 5.55" in result

def test_get_dollar_price_error():
    with patch("app.services.agent_service.requests.get", side_effect=Exception("Falha")):
        result = get_dollar_price()
        assert "Erro ao consultar cotação" in result
