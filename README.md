Simple Usage for palm

```python
from openapi import Client
import asyncio

async def main(prompt: str) -> dict:
    client = Client()
    response = await client.palm(prompt)
    return response

if __name__ == "__main__":
    print(asyncio.run(main("hemlo")))
```

Simple Usage for upscaling an image.

```python
from openapi import Client
import asyncio

async def main(image: bytes) -> bytes:
    client = Client()
    response = await client.upscale(image)
    with open('upscaled.png', 'wb') as f:
        f.write(imageBytes)


if __name__ == "__main__":
    with open('image.png', 'rb') as f:
        image = f.read()
    asyncio.run(main(image))
```