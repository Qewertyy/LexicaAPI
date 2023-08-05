from openapi import AsyncClient
import asyncio

async def async_main(image: bytes) -> bytes:
    client = AsyncClient()
    imageBytes = await client.upscale(image)
    await client.close()
    with open('upscaled.png', 'wb') as f:
        f.write(imageBytes)

if __name__ == "__main__":
    image = open('examples/images/image.png', 'rb').read()
    asyncio.run(async_main(image))