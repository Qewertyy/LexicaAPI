# Copyright 2024 Qewertyy, MIT License

from lexica import Client

def main(image_url: str) -> dict:
    client = Client()
    response = client.AntiNsfw(image_url,29)
    print(response)
    if 'sfw' in response['content'] and response['content']['sfw'] == True:
        return "This image is safe for work."
    elif 'isNsfw' in response['content']:
        if response['content']['isNsfw'] == True:
            return "This image is not safe for work."
        else:
            return "This image is safe for work."
    else:
        return "This image is not safe for work."

if __name__ == "__main__":
    print(main("https://graph.org/file/de1888dd4fdfbc647c398.jpg"))