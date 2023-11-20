from lexica import AsyncClient
import asyncio

async def main(url: str) -> dict:
    client = AsyncClient()
    response = await client.MediaDownloaders("instagram",url)
    return response

if __name__ == "__main__":
    print(asyncio.run(main("https://www.instagram.com/p/Cz2HsJ5NRDf/")))