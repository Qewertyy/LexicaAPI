Here are some projects which utilizes the LexicaAPI.

### AverageAI
- **Name:** [AverageAI](https://ai.qewertyy.dev)
- **Description:** Image Generations and LLMs.

### AverageImages
- **Name:** [AverageImages](https://images.qewertyy.dev)
- **Description:** Search Images on google and bing.

### Upscale
- **Name:** [Upscale](https://upscale.qewertyy.dev)
- **Description:** Upscale Images.

## AverageNews
- **Name:** [AverageNews](https://news.qewertyy.dev)
- **Description:** News App.


## Usages
LLM's
```python
from lexica import Client, languageModels

def main(prompt: str) -> dict:
    client = Client()
    response = client.palm(prompt,languageModels.palm2)
    return response

if __name__ == "__main__":
    print(main("hello world"))
```

Upscale an image.
```python
from lexica import Client

def main(image: bytes) -> bytes:
    client = Client()
    imageBytes = client.upscale(image)
    with open('upscaled.png', 'wb') as f:
        f.write(imageBytes)

if __name__ == "__main__":
    image = open('examples/images/image.png', 'rb').read()
    main(image)
```

Anti-NSFW
```python
from lexica import Client

def main(image_url: str) -> dict:
    client = Client()
    response = client.AntiNsfw(image_url)
    if response['content']['sfw'] == True:
        return "This image is safe for work."
    else:
        return "This image is not safe for work."

if __name__ == "__main__":
    print(main("https://graph.org/file/13e95c6cc932530823391.png"))
```
