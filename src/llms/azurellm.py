import os
from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.chat_models import init_chat_model


class AzureLLM:
    def __init__(self):
        load_dotenv()
    
    def get_llm(self) -> BaseChatModel:
        try:
            llm = init_chat_model("azure_openai:gpt-4o-mini")
            return llm
        except Exception as e:
            raise Exception(f"Failed to initialize Azure LLM: {e}")