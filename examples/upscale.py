from openapi import Client
import asyncio

async def main(image: bytes) -> bytes:
    client = Client()
    response = await client.upscale(image)
    return response


if __name__ == "__main__":
    with open('image.png', 'rb') as f:
        image = f.read()
    asyncio.run(main(image))