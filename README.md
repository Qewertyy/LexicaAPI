Simple Usage for palm

```python
from openapi import Client

def main(prompt: str) -> dict:
    client = Client()
    response = client.palm(prompt)
    return response

if __name__ == "__main__":
    print(main("hello world"))
```

Simple Usage for upscaling an image.

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