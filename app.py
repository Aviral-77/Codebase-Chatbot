# app.py

import chainlit as cl
from index_manager import load_index

@cl.on_chat_start
async def on_chat_start():
    try:
        index = load_index()
        if index is None:
            await cl.Message(author="Assistant", content="❌ Failed to initialize the index.").send()
            return
        query_engine = index.as_query_engine(streaming=True, similarity_top_k=2)
        cl.user_session.set("query_engine", query_engine)
        await cl.Message(author="Assistant", content="Hello! How may I help you?").send()
    except Exception as e:
        await cl.Message(author="Assistant", content=f"❌ Error initializing index:\n{e}").send()

@cl.on_message
async def main(message: cl.Message):
    query_engine = cl.user_session.get("query_engine")
    if query_engine is None:
        await cl.Message(content="❌ Query engine not initialized. Try restarting.").send()
        return

    msg = cl.Message(content="", author="Assistant")
    res = query_engine.query(message.content)
    for token in res.response_gen:
        await msg.stream_token(token)
    await msg.send()
