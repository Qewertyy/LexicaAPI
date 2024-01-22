# Copyright 2024 Qewertyy, MIT License

from lexica import AsyncClient
import asyncio

async def main(image_url: str) -> dict:
    client = AsyncClient()
    response = await client.AntiNsfw(image_url)
    await client.close()
    if response['content']['sfw'] == True:
        return "This image is safe for work."
    else:
        return "This image is not safe for work."

if __name__ == "__main__":
    print(asyncio.run(main("https://graph.org/file/13e95c6cc932530823391.png")))