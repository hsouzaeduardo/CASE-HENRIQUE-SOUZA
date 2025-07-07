rojeto: Microserviço LangChain com Azure OpenAI

🚀 Visão Geral

Este projeto implementa um microserviço cloud native em Python, usando FastAPI e LangChain Agent, integrado com Azure OpenAI e Cosmos DB. A solução persiste os prompts e respostas para futuras análises e retorna a resposta ao usuário em tempo real.

💻 Tecnologias utilizadas

Python 3.11+

FastAPI

LangChain (Agent)

Azure OpenAI (via AzureChatOpenAI)

Azure Cosmos DB

Application Insights (observabilidade)

⚙️ Fluxo da API

1️⃣ Cliente envia POST /v1/chat com userId e prompt2️⃣ O Agent do LangChain processa o prompt via Azure OpenAI3️⃣ O prompt e a resposta são salvos no Cosmos DB4️⃣ A API retorna ao usuário uma resposta estruturada

🗄️ Estrutura de diretórios

app/
├── main.py
├── agent.py
├── db.py
├── models.py
├── utils.py
requirements.txt

✉️ Exemplo de request

Endpoint

POST /v1/chat

Payload

{
  "userId": "12345",
  "prompt": "Como está a cotação do dólar hoje?"
}

Response

{
  "id": "uuid-gerado",
  "userId": "12345",
  "prompt": "Como está a cotação do dólar hoje?",
  "response": "A cotação do dólar hoje é R$5,10.",
  "model": "gpt-4o",
  "timestamp": "2025-07-06T15:32:00Z"
}

☁️ Infraestrutura no Azure

API Gateway: Azure API Management (opcional)

Compute: Azure App Service ou Container Apps

Banco de dados: Azure Cosmos DB

LLM: Azure OpenAI Service

Observabilidade: Application Insights

💾 Variáveis de ambiente

AZURE_OPENAI_API_KEY=xxxxxx
AZURE_OPENAI_ENDPOINT=https://<sua-instancia>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
COSMOS_ENDPOINT=https://<seu-endpoint>.documents.azure.com:443/
COSMOS_KEY=<sua-chave>

🏗️ Deploy no Azure

1️⃣ Configure as variáveis de ambiente no App Service ou Container App2️⃣ Crie o Cosmos DB e container Prompts3️⃣ Faça push do código ou deploy via CI/CD4️⃣ Habilite Application Insights para logs e métricas

🎨 Diagrama de arquitetura

[Usuário]
   ↓
[Azure API Management]
   ↓
[FastAPI (App Service / Container Container)]
   ↓                ↘
[Cosmos DB]      [Azure OpenAI]
   ↓
[Application Insights]

✅ Benefícios

Arquitetura cloud native

Fácil de escalar

Resiliente (retry, fallback)

Observável (logs, traces, métricas)

Pronto para produção no Azure

🟢 Próximos passos

Ajustar tokens e modelos conforme sua necessidade

Adicionar ferramentas extras no Agent se quiser funcionalidades adicionais (ex: consulta SQL, APIs externas)

💬 Dúvidas ou ajustes? Só pedir! 🚀

