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