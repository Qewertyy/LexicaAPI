# Copyright 2024 Qewertyy, MIT License

from lexica import AsyncClient
import asyncio

async def main(query: str) -> dict:
    client = AsyncClient()
    response = await client.SearchImages(query)
    return response

if __name__ == "__main__":
    print(asyncio.run(main("akeno himejima")))