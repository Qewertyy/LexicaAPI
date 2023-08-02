from openapi import Client
import asyncio

async def main(image: bytes) -> bytes:
    client = Client()
    imageBytes = await client.upscale(image)
    with open('upscaled.png', 'wb') as f:
        f.write(imageBytes)

if __name__ == "__main__":
    image = open('examples/images/image.png', 'rb').read()
    asyncio.run(main(image))