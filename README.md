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