# Microserviço LangChain com Azure OpenAI

## 🚀 Visão Geral

Este projeto implementa um microserviço cloud native em Python, utilizando FastAPI e LangChain Agent, integrado com Azure OpenAI e Azure Cosmos DB. O serviço persiste prompts e respostas para análises futuras e retorna respostas em tempo real ao usuário.

## 💻 Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- LangChain (Agent)
- Azure OpenAI (via AzureChatOpenAI)
- Azure Cosmos DB

## ⚙️ Como Executar

1. Clone o repositório:
git clone https://github.com/hsouzaeduardo/CASE-HENRIQUE-SOUZA.git

2. Crie e ative um ambiente virtual:
# Linux/Mac 
python -m venv venv source venv/bin/activate 
# Windows
venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

uvicorn main:app --reload

## 📦 Estrutura do Projeto

## 📝 Funcionalidades

- Recebe prompts via API REST.
- Processa prompts usando LangChain Agent e Azure OpenAI.
- Persiste prompts e respostas no Azure Cosmos DB.
- Retorna respostas em tempo real.

## Licença
Este projeto está sob a licença MIT.

## O que falta ?
Obervabilidade

##.ENV

## ========================================
## Azure OpenAI Configuration
## ========================================

AZURE_OPENAI_ENDPOINT=https://<seu-endpoint>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
AZURE_OPENAI_API_KEY=<sua-chave-aqui>

## ========================================
## Cosmos DB Configuration
## ========================================

COSMOS_ENDPOINT=https://<seu-endpoint-cosmos>.documents.azure.com:443/
COSMOS_KEY=<sua-chave-cosmos-aqui>
COSMOS_DATABASE_NAME=caseitau
COSMOS_CONTAINER_NAME=chats

## ========================================
## App Configuration
## ========================================

APP_NAME=AI Agent API
DEBUG=false

## ========================================
## Server Configuration
## ========================================

HOST=0.0.0.0
PORT=8000
RELOAD=false
LOG_LEVEL=info


