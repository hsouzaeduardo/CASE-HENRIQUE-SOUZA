from langchain_openai import AzureChatOpenAI
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from app.config.settings import Settings
import requests

class AgentService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._agent = None
        self._chat_histories = {}
    
    @property
    def agent(self):
        if self._agent is None:
            self._agent = self._create_agent()
        return self._agent
    
    def _create_agent(self):
        llm = AzureChatOpenAI(
            api_key=self.settings.azure_openai_api_key,
            azure_endpoint=self.settings.azure_openai_endpoint,
            azure_deployment=self.settings.azure_openai_deployment_name,
            api_version=self.settings.azure_openai_api_version,
            temperature=0.7,
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Use tools if needed."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")  
        ])
        
        agent = create_openai_functions_agent(
            llm,
            tools=[get_dollar_price],
            prompt=prompt
        )
        
        executor = AgentExecutor(agent=agent, tools=[get_dollar_price], verbose=True)
        
        # Wrap with history
        return RunnableWithMessageHistory(
            executor,
            self._get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history"
        )
    
    def _get_session_history(self, session_id: str):
        if session_id not in self._chat_histories:
            self._chat_histories[session_id] = ChatMessageHistory()
        return self._chat_histories[session_id]
    
    def run_prompt(self, prompt: str, session_id: str = "default") -> str:
        response = self.agent.invoke(
            {"input": prompt},
            config={"configurable": {"session_id": session_id}}
        )
        if hasattr(response, 'content'):
            return response.content
        else:
            return str(response)
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