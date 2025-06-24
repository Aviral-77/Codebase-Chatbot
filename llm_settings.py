# llm_settings.py

from llama_index.llms.ollama import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.core import PromptHelper, Settings

def configure_llm():
    llm = Ollama(model="llama3", temperature=0.7)
    embed_model = HuggingFaceEmbeddings()
    prompt_helper = PromptHelper(context_window=4096, num_output=256, chunk_overlap_ratio=0.1)

    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.prompt_helper = prompt_helper
