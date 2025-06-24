# index_manager.py

import os
from llama_index.core import (
    StorageContext,
    load_index_from_storage,
    VectorStoreIndex,
)
from llm_settings import configure_llm
from github_loader import load_github_documents
from config import INDEX_DIR
import chainlit as cl

@cl.cache
def load_index():
    try:
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        index = load_index_from_storage(storage_context)
    except Exception as e:
        print(f"⚠️ Could not load existing index: {e}")
        print("➡️ Creating new index...")

        try:
            documents = load_github_documents()
            configure_llm()
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(INDEX_DIR)
            print("✅ New index created and saved.")
        except Exception as inner_e:
            print(f"❌ Failed to create index: {inner_e}")
            index = None

    return index
