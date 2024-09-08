#text_generation.py
from transformers import pipeline
import asyncio

generator = pipeline('text-generation', model='gpt2')

async def get_llm_response_async(prompt):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: generator(prompt, max_length=100, num_return_sequences=1))
    return response[0]['generated_text'].strip()
