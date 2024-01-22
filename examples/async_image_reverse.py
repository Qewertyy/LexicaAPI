# Copyright 2024 Qewertyy, MIT License

from lexica import AsyncClient
import asyncio

async def main(imgUrl: str) -> dict:
    client = AsyncClient()
    response = await client.ImageReverse(imgUrl)
    return response

if __name__ == "__main__":
    print(asyncio.run(main("https://graph.org/file/abd8ff7611c2af0108b3d.jpg")))