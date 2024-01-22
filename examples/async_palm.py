# Copyright 2024 Qewertyy, MIT License

from lexica import AsyncClient, languageModels
import asyncio

async def async_main(prompt: str) -> dict:
    client = AsyncClient()
    response = await client.ChatCompletion(prompt,languageModels.palm)
    await client.close()
    return response

if __name__ == "__main__":
    print(asyncio.run(async_main("hello, who are you?")))