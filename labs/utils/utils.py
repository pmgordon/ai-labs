from langchain_ollama import ChatOllama

LOCAL_LLM = 'llama3.2:3b-instruct-fp16'
LLM = ChatOllama(model=LOCAL_LLM, temperature=0)
LLM_JSON_MODEL = ChatOllama(model=LOCAL_LLM, temperature=0, format='json')

def get_llm():
    return LLM

def get_json_llm():
    return LLM_JSON_MODEL