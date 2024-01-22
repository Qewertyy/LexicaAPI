# Copyright 2024 Qewertyy, MIT License

from lexica import Client

def main(image: bytes) -> bytes:
    client = Client()
    imageBytes = client.upscale(image)
    with open('examples/images/upscaled.png', 'wb') as f:
        f.write(imageBytes)

if __name__ == "__main__":
    image = open('examples/images/image.png', 'rb').read()
    main(image)