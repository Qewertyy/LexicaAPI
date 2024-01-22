# Copyright 2024 Qewertyy, MIT License

from lexica import Client

def main(query: str) -> dict:
    client = Client()
    response = client.SearchImages(query)
    return response

if __name__ == "__main__":
    print(main("akeno himejima"))