# async usage

from openapi import AsyncClient
import asyncio

async def async_main() -> dict:
    client = AsyncClient()
    response = await client.getModels()
    await client.close()
    return response

# sync usage

from openapi import Client

def main() -> dict:
    client = Client()
    response = client.getModels()
    return response

if __name__ == "__main__":
    print(main())
    #print(asyncio.run(async_main()))