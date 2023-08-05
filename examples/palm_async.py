from openapi import AsyncClient
import asyncio

async def async_main(prompt: str) -> dict:
    client = AsyncClient()
    response = await client.palm(prompt)
    await client.close()
    return response

if __name__ == "__main__":
    print(asyncio.run(async_main("hello world")))