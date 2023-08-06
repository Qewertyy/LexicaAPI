Available Models

```python
from openapi import Client

def main() -> dict:
    client = Client()
    response = client.getModels()
    return response

if __name__ == "__main__":
    print(main())
```
output
```json
{
    text: [
      { id: 0, name: "models/text-bison-001" },
    ],
    chat: [
      { id: 1, name: "models/chat-bison-001" },
    ],
    image: [
      { id: 2, name: "MeinaMix" },
      { id: 3, name: "AnyLora" },
      { id: 4, name: "AnyThingV4" }
    ]
  }
```

Usage for palm

```python
from openapi import Client

def main(prompt: str) -> dict:
    client = Client()
    response = client.palm(prompt)
    return response

if __name__ == "__main__":
    print(main("hello world"))
```

Usage for upscaling an image.

```python
from openapi import Client

def main(image: bytes) -> bytes:
    client = Client()
    imageBytes = client.upscale(image)
    with open('upscaled.png', 'wb') as f:
        f.write(imageBytes)

if __name__ == "__main__":
    image = open('examples/images/image.png', 'rb').read()
    main(image)
```