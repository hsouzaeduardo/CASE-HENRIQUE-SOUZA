import requests
from langchain.tools import tool

@tool
def get_dollar_price() -> str:
    """Consulta a cotação do dólar em uma API pública"""
    try:
        response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        data = response.json()
        price = data["USDBRL"]["bid"]
        return f"O dólar está valendo R$ {float(price):.2f} agora."
    except Exception as e:
        return f"Erro ao consultar cotação: {str(e)}"
    
@tool    
def get_euro_price() -> str:
    """Consulta a cotação do euro em uma API pública"""
    try:
        response = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-BRL")
        data = response.json()
        price = data["EURBRL"]["bid"]
        return f"O euro está valendo R$ {float(price):.2f} agora."
    except Exception as e:
        return f"Erro ao consultar cotação: {str(e)}"