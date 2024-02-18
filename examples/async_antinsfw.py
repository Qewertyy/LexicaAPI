# Copyright 2024 Qewertyy, MIT License

from lexica import AsyncClient
import asyncio

async def main(image_url: str) -> dict:
    client = AsyncClient()
    response = await client.AntiNsfw(image_url,29)
    await client.close()
    print(response)
    if 'sfw' in response['content'] and response['content']['sfw'] == True:
        return "This image is safe for work."
    elif 'isNsfw' in response['content']:
        if response['content']['isNsfw'] == True:
            return "This image is not safe for work."
        else:
            return "This image is safe for work."
    else:
        return "This image is not safe for work."

if __name__ == "__main__":
    print(asyncio.run(main("https://graph.org/file/a642e642fe01a917fd5b5.jpg")))