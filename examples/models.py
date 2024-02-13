# Copyright 2024 Qewertyy, MIT License

# async usage

from lexica import AsyncClient
import asyncio

async def async_main() -> dict:
    client = AsyncClient()
    response = await client.models
    await client.close()
    return response

# sync usage

from lexica import Client

def main() -> dict:
    client = Client()
    return client.models


if __name__ == "__main__":
    #print(main())
    print(asyncio.run(async_main()))