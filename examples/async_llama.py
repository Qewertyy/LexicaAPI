# Copyright 2024 Qewertyy, MIT License

import asyncio
from lexica import AsyncClient, languageModels, Messages

async def async_main(prompt: str) -> dict:
    client = AsyncClient()
    response = await client.ChatCompletion([Messages(content=prompt,role="user")],languageModels.llama)
    return response

if __name__ == "__main__":
    print(asyncio.run(async_main("hello, who are you?")))