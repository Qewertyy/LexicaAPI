import asyncio
from lexica import AsyncClient
from lexica.constants import languageModels

async def async_main(prompt: str) -> dict:
    client = AsyncClient()
    response = await client.ChatCompletion(prompt,languageModels.bard)
    return response

if __name__ == "__main__":
    print(asyncio.run(async_main("hello, who are you?")))