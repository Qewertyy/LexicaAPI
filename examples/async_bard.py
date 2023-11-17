import asyncio
from lexica import AsyncClient

async def main(prompt: str) -> dict:
    client = AsyncClient()
    response = await client.bard(prompt)
    return response

if __name__ == "__main__":
    print(asyncio.run(main("hello, who are you?")))