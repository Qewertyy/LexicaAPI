# Copyright 2024 Qewertyy, MIT License

from lexica import Client

def main(imgUrl: str) -> dict:
    client = Client()
    response = client.ImageReverse(imgUrl)
    return response

if __name__ == "__main__":
    print(main("https://graph.org/file/abd8ff7611c2af0108b3d.jpg"))